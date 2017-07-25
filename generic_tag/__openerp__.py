# -*- coding: utf-8 -*-
{
    'name': "Generic Tag",

    'summary': """
        Generic tag management.
    """,

    'author': "Management and Accounting Online",
    'website': "https://maao.com.ua",

    'category': 'Uncategorized',
    'version': '10.0.0.1.0',

    "depends": [
        "base",
        "base_action_rule",
    ],

    "data": [
        'security/base_security.xml',
        'security/ir.model.access.csv',
        'views/generic_tag_view.xml',
        'views/base_action_rule_view.xml',
    ],
    "installable": True,
    "active": True,
    'license': 'Other proprietary',
}