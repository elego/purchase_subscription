# -*- coding: utf-8 -*-
{
    'name': 'Purchase Subscription',
    'installable': True,
    'application': True,
    'depends': ['base', 'account', 'analytic', 'purchase'],
    'data': [
        'data/purchase_contract_data.xml',
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/res_partner_views.xml',
        'views/purchase_subscription_views.xml',
    ],
    'author': 'sudokeys',
    'description':
    """
        This module is used to trigger a recurrency provider invoice :
            - rent
            - Telephone/ internet subscription
            - Any other regular payment that needs a recurrent invoice.
    """
}
