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

from openerp.osv import osv, fields
import mimetypes
from openerp import SUPERUSER_ID
import boto3,os
import base64
import openerp
from io import BytesIO

class ir_attachment(osv.osv):
    _inherit = "ir.attachment"
    __bucketname=openerp.tools.config['s3_bucketname']
    __region = openerp.tools.config['s3_region']
    __aws_access_key_id = openerp.tools.config['s3_access_key_id']
    __aws_secret_access_key = openerp.tools.config['s3_secret_access_key']
    __session = boto3.Session(aws_access_key_id=__aws_access_key_id,
                  aws_secret_access_key=__aws_secret_access_key,
                  region_name=__region)
    __s3=__session.resource('s3')
    
 
    _columns = {
        'mimetype': fields.char('Mime Type', readonly=True),
        's3target' : fields.char('target'),
        'imgsize' : fields.integer('imgsize')
    }
    
    

    def _add_mimetype_if_needed(self, values):
        if values.get('datas_fname'):
            values['mimetype'] = mimetypes.guess_type(values.get('datas_fname'))[0] or 'application/octet-stream'


    def create(self, cr, uid, values, context=None):
        self._add_mimetype_if_needed(values)
        
        return super(ir_attachment, self).create(cr, uid, values, context=context)

    def write(self, cr, uid, ids, values, context=None):
        self._add_mimetype_if_needed(values)
        return super(ir_attachment, self).write(cr, uid, ids, values, context=context)
    
    def upload_image(self, cr,uid, fielname,ufile,size,type,context=None):
        permision="public-read"
        dir = "born_image_service"
        uploadfile=dir.strip()+"/"+fielname
        bol = self.isexists(uploadfile)
        ob=self.__s3.Object(self.__bucketname, uploadfile)
        f = BytesIO()
        f.write(base64.b64decode(ufile))
        f.seek(0)
        result=ob.put(Body=f,ServerSideEncryption='AES256',StorageClass='STANDARD',ACL=permision)
        f.close()
        try:
            if not bol:
                attachment_id = self.create(cr,uid,{
                    'name': fielname,
                    'datas_fname': fielname,
                    'imgsize': size,
                    'url' : 'https://s3.cn-north-1.amazonaws.com.cn/'+self.__bucketname+'/'+uploadfile,
                    's3target' : 's3Upload',
                    'type' : "url"
                }, context=context)
            else:
                attachment_id = self.search(cr, uid,[('name','=',fielname)],context=None )
                print "attachment"+attachment_id
                self.write(cr, uid, attachment_id, {'size':size}, context)
            args = {
                'filename': ufile.name,
                'url' : 'https://s3.cn-north-1.amazonaws.com.cn/'+self.__bucketname+'/'+uploadfile,
            }
        except Exception:
            args = {'error': "Something horrible happened"}
        return args
    
    def isexists(self,uploadfile):
        try:
            self.__s3.Object(self.__bucketname,uploadfile).get()
            return True
        except:
            return False
            

    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
