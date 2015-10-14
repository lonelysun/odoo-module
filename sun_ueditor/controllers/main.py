# -*- coding: utf-8 -*-
##############################################################################
#  COMPANY: BORN
#  AUTHOR: SongHb
#  EMAIL: songhaibin1990@gmail.com
#  VERSION : 1.0   NEW  2015/08/20
#  UPDATE : NONE
#  Copyright (C) 2011-2015 www.wevip.com All Rights Reserved
##############################################################################

# import random
# import string
# 
# from mako import exceptions
# from openerp.http import request
# from lxml import etree
# from dateutil.relativedelta import relativedelta

import os
import json
import logging
import time
import openerp
import simplejson
import werkzeug.utils
from mako import exceptions
from openerp.http import request
from openerp import SUPERUSER_ID
from openerp.addons.web import http
from datetime import datetime,timedelta
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT  
from openerp import tools

from ueditor_config import config


_logger = logging.getLogger(__name__)


#动态切换数据库
def ensure_db(db=False,redirect='/except'):
    if not db:
        db = request.params.get('db')

    if db and db not in http.db_filter([db]):
        db = None
    
    if not db and request.session.db and http.db_filter([request.session.db]):
        db = request.session.db
        
    if not db:
        werkzeug.exceptions.abort(werkzeug.utils.redirect(redirect, 303))

    request.session.db = db


class Ueditor(http.Controller):
    
    @http.route(['/ueditor/controller'], type='http', auth='user')
    def ueditor_controller(self, debug=True, **post):
        print post
        print "GET"
        action = post.get('action', '')
        #初始化读取配置信息
        if action == 'config':
            return json.dumps(config)
        #图片上传
        elif action == 'uploadimage':
            pass
        #上传文件
        elif action == 'uploadfile':
            pass
        #列出指定目录下的图片
        elif action == 'listimage':
            pass
        #列出指定目录下的文件
        elif action == 'listfile':
            pass
        #上传视频
        elif action == 'uploadvideo':
            pass
        #涂鸦图片
        elif action == 'uploadscrawl':
            pass
        #抓取远程图片
        elif action == 'catchimage':
            pass
        else:
            pass
        print "POST"
        res = {
               "state": "SUCCESS",
               "url": "upload/demo.jpg",
               "title": "demo.jpg",
               "original": "demo.jpg"
        }
        return simplejson.dumps(res)

#         registry = openerp.modules.registry.RegistryManager.get(request.session.db)
#         user_pool = registry.get('res.users')
#         facilities_pool = registry.get('product.product')#房间、设施
#         type_pool = registry.get('born.facilities.type')#类型
#         uid = request.session.uid
#         context = request.session.context
#         with registry.cursor() as cr:
#             company_id = user_pool.browse(cr, uid, uid, context).company_id.id
#             user = user_pool.browse(cr, uid, uid, context)
#             if user.shop_id:
#                 shop_id =  user.shop_id.id
#             else:
#                 shop_id = False
#             showRoom = True
#             type_ids = type_pool.search(cr, uid,
#                                        [('book_ok', '=', True),('company_id', '=', company_id),('shop_id', '=', shop_id)])
#             if  type_ids:
#                 room_ids = facilities_pool.search(cr, uid,[('company_id', '=', company_id), 
#                                                                ('active', '=', True),
#                                                                ('shop_id', '=', shop_id),
#                                                                ('is_room', '=', True),
#                                                                ('born_category', '=', 2)])
#                 if room_ids:
#                     pass
#                 else:
#                     showRoom = False
#             else:
#                     showRoom = False
#             
#             return simplejson.dumps({"flag":showRoom})
            



        
        
        