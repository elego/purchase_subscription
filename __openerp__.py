# -*- coding: utf-8 -*-
{
    'name' : 'Purchase Subcription',
    'installable' : True,
    'application' : True,
    'depends' : ['base', 'account', 'analytic', 'purchase'],
    'data' : [
                'data/purchase_contract_data.xml',
                'security/ir.model.access.csv',
                'views/product_template_views.xml',
                'views/res_partner_views.xml',
                'views/purchase_subscription_views.xml',
             ],
    'author' : 'sudokeys',
    'description': """
        Ce module permet de déclencher une facturation fournisseur récurrente :
            - loyer
            - Abonnement téléphonique / internet
            - Tout autre paiement régulier donnant lieu à une facture founisseur de façon récurente
    """
}
