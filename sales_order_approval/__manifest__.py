# -*- coding: utf-8 -*-
{
    'name': 'Sales Order Approval',
    'version': '17.0.1.0.0',
    'category': 'Sales',
    'summary': """ "Sales Order Approval" is a process that requires two separate approvals for a sales order, ensuring accuracy, compliance, and minimizing the risk of errors and fraud. """,
    'description': """ "Sales Order Approval" is a process where a sales order must be reviewed and approved by two separate individuals or departments before finalization. This procedure is designed to ensure accuracy, compliance, and minimize the risk of errors and fraud in sales transactions.""",
    'author': 'Hi Spark Solutions',
    'company': 'Hi Spark Solutions',
    'maintainer': 'Hi Spark Solutions',
    'website': 'https://www.hisparksolutions.com/',
    'depends': ['base', 'sale_management'],
    'data': [
        'views/res_company_views.xml',
        'views/res_config_settings_views.xml',
        'views/sale_order_views.xml'
    ],
    'images': [
        'static/description/banner.jpg',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
    "price": "10",
    "currency": "USD",
}
