# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Purchase Subscription',
    'summary': "An easy way to manage your provider's subscriptions.",
    'installable': True,
    'application': True,
    'licence' : "AGPL-3",
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
