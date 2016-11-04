# -*- coding: utf-8 -*-
{
    'name' : 'Purchase Subcription',
    'installable' : True,
    'application' : True,
    'depends' : ['base', 'account', 'analytic'],
    'data' : [
                'data/purchase_contract_data.xml',
                'views/account_analytic_account_views.xml',
                'views/product_template_views.xml',
                'views/res_partner_views.xml',
                'views/purchase_subscription_views.xml',
             ],
    'author' : 'sudokeys',
}
