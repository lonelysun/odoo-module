# -*- coding: utf-8 -*-
##############################################################################
#
#    Better WYSIWYG Cleditor
#    Copyright 2014 wangbuke <wangbuke@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.addons.web.http import Controller, route, request
import boto3,os
import datetime,time
import simplejson
import hashlib
import base64
import openerp
from io import BytesIO

class ImageListController(Controller):

    @route('/web/ir_attachment/imagelist', type='json', auth="user")
    def imagelist(self, **data):
        attachment_obj = request.registry['ir.attachment']
        cr, uid, context = request.cr, request.uid, request.context
        imagelist = []
        attachment_ids = attachment_obj.search(cr, uid, [("s3target","=","s3")])
        urllist = attachment_obj.read(cr, uid, attachment_ids,['url'],context={})
        for urldic in urllist:
            imagelist.append(urldic["url"])
        return imagelist

class BornS3Client(Controller):
    
    def __init__(self):
        
        self.__bucketname = openerp.tools.config['s3_bucketname']
        self.__region = openerp.tools.config['s3_region']
        self.__aws_access_key_id = openerp.tools.config['s3_access_key_id']
        self.__aws_secret_access_key = openerp.tools.config['s3_secret_access_key']
        self.__session = boto3.Session(aws_access_key_id=self.__aws_access_key_id,
                                  aws_secret_access_key=self.__aws_secret_access_key,
                                  region_name=self.__region)
        self.__s3 = self.__session.resource('s3')
    
    @route('/web/binary/upload_s3', type='http', auth="user")
    def upload(self, callback, model, id, ufile,permision="public-read"):
        if(permision not in ("public-read","private","bucket-owner-read")):
            return "指定的权限不存在！"
        pngtype = ufile.filename.split('.')[1]
        datas = base64.encodestring(ufile.read())

        sha = hashlib.sha1(datas).hexdigest()
        uid = request.session.uid
        company_id = request.registry['res.users'].browse(request.cr, uid, uid, context=request.context).company_id.id
        born_uuid = request.registry['res.company'].browse(request.cr,uid,company_id,context=request.context).born_uuid
        dir = born_uuid
        cname = sha
        uploadfile=dir.strip()+"/"+cname.strip()+"."+pngtype
        ob=self.__s3.Object(self.__bucketname, uploadfile)
        bol = self.isexists(uploadfile)
        ufile.seek(0)
        result=ob.put(Body=ufile.stream,ServerSideEncryption='AES256',StorageClass='STANDARD',ACL=permision)
        Model = request.session.model('ir.attachment')
        out = """<script language="javascript" type="text/javascript">
                    var win = window.top.window;
                    win.jQuery(win).trigger(%s, %s);
                </script>"""
        try:
            if not bol:
                attachment_id = Model.create({
                    'name': ufile.filename,
                    'datas_fname': ufile.filename,
                    'imgsize': len(datas.decode('base64')),
                    'res_id': int(id),
                    'url' : 'https://s3.cn-north-1.amazonaws.com.cn/'+self.__bucketname+'/'+uploadfile,
                    's3target' : 's3',
                    'type' : 'url'
                }, request.context)
            args = {
                'filename': ufile.filename,
                'url' : 'https://s3.cn-north-1.amazonaws.com.cn/'+self.__bucketname+'/'+uploadfile,
            }
        except Exception:
            args = {'error': "Something horrible happened"}
        return out % (simplejson.dumps(callback), simplejson.dumps(args))
        
    def isexists(self,uploadfile):
        try:
            self.__s3.Object(self.__bucketname,uploadfile).get()
            return True
        except:
            return False
        

    