# -*- coding: utf-8 -*-
{
    'name': "account_fifo_extension",

    'summary': """
        Account by lot cost when cost method is fifo""",

    'description': """
        1. Add product cost to lot.
        2. Account by every lot cost when cost method is fifo.
    """,

    'author': "Yuhui",
    'website': "http://www.wangyuhui.top",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock_account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_production_lot_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
