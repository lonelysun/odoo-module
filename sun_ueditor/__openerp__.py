# -*- coding: utf-8 -*-
##############################################################################
#  COMPANY: BORN
#  AUTHOR: SongHb
#  EMAIL: songhaibin1990@gmail.com
#  VERSION : 1.0   NEW  2015/08/20
#  UPDATE : NONE
#  Copyright (C) 2011-2015 www.wevip.com All Rights Reserved
##############################################################################
{
    'name': '富文本编辑器',  # 模块名称
    'summary': '富文本编辑器',  # 摘要
    'version': '1.0',  # 版本
    'category': 'BORN',  # 分类
    'sequence': 1,  # 排序
    'author': 'SongHb',  # 作者
    'website': 'http://www.wevip.com',  # 网址
    "depends": [
        'web',
    ],
    "data": [
        'views/view.xml',
    ],
    "qweb": [
        'static/src/xml/*.xml',
    ],
    "installable" : True,
    "active" : True,
    
    
    "description": u"""
    名称：富文本编辑器ueditor
        """,
}

