# -*- coding: utf-8 -*-
##############################################################################
# OpenERP Connector
# Copyright 2013 BORN <Author:SongHb>
##############################################################################

{
    'name': '图片截取',  # 模块名称
    'summary': '图片截取',  # 摘要
    'version': '1.0',  # 版本
    'category': 'BORN',  # 分类
    'sequence': 0,  # 排序
    'author': 'SongHb',  # 作者
    'website': 'http://www.wevip.com',  # 网址
    'depends' : ['base', 'web'], # 关联模块
    'data': [
#         'data/born_init_data.xml',
#         'security/ir.model.access.csv',
#         'security/im_security.xml',
# 'wizard/init_wizard.xml',
         'views/born_image_crop.xml',
#         'born_init_wizard.xml',
    ],
    
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,  # 是否可安装
    'application': True,  # 是否认证
    'auto_install': False,  # 是否自动安装
    'description': '''
    '''
}