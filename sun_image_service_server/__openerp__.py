# -*- coding: utf-8 -*-
##############################################################################
#  COMPANY: BORN
#  AUTHOR: LH
#  EMAIL: arborous@gmail.com
#  VERSION : 1.0   NEW  2014/07/21
#  UPDATE : NONE
#  Copyright (C) 2011-2014 www.wevip.com All Rights Reserved
##############################################################################

{
    'name': "图片服务",
    'author': 'BORN',
    'summary': 'BORN',
    'description': """
     """,
    'category': 'BORN',
    'sequence': 0,
    'website': 'http://www.wevip.com',
    'images': [],
    'depends': ['base','web'],
 
    'demo': [],
    'init_xml': [],
    'data': [
        'views/born_image_service_server.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'auto_install': False,
    'application': True,
    'installable': True,
}
