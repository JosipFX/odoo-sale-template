{
    'name': 'Sale and Account Customization',
    'summary': """Sale Product Extension""",
    'description': '''This module enables multiple features in products and Sales
        1: Customized Invoice pdf
        2: Custom Sale Quotation report
    ''',
    'category': 'Sale',
    'version': '18.0.1.0.0',
    'author': 'Josip & simpit GmbH',
    'company': 'Herr Inf & simpit GmbH',
    'website': "https://simpit.ch",
    'depends': ['base', 'sale', 'account', 'sale_management'],
    'data': [
        'report/web_layout.xml',
        'report/sale_order_templates.xml',
        'report/ir_actions_report.xml',
        'report/invoice_report_templates.xml',

        'views/sale_order_view.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
# -*- coding: utf-8 -*-
