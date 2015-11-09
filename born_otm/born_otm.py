# -*- coding: utf-8 -*-
##############################################################################
#  COMPANY: BORN
#  AUTHOR: LH
#  EMAIL: arborous@gmail.com
#  VERSION : 1.0   NEW  2015/10/22
#  UPDATE : NONE
#  Copyright (C) 2011-2015 www.wevip.com All Rights Reserved
##############################################################################
from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp

try:
    from openerp import SUPERUSER_ID
except ImportError:
    SUPERUSER_ID = SUPERUSER_ID

class born_otm(osv.osv):
    _name = "born.otm"
    _columns = {
                'name' : fields.char(u'名称',required=True),
                'image' : fields.binary(u'图片'),
                'category_id' : fields.many2one('otm.category',u'类型'),
                'table_ids': fields.one2many('born.table','table_id',u'当前状况'),

    }
    
class born_table(osv.osv):
    _name = "born.table"
    _columns = {
                'table_id' : fields.many2one('born.otm',string='厅'),
                'name' : fields.char(u'桌'),
                'size' : fields.integer(u'可容纳人数'),
                'number' : fields.integer(u'现有量'),
                'state' : fields.selection([('reservations', u'预定'), ('done', u'就坐'),('draft', u'空台')], u'状态', ),
    }
    
#分类
class otm_category(osv.osv):
    _name = "otm.category"
    _columns = {
        'name': fields.char('名称', required=True),
    }
    

    