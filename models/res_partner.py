# -*- coding: utf-8 -*-

from openerp import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    po_subscription_count   = fields.Integer(string='Purchase Subscriptions', compute='_po_subscription_count')

    def _po_subscription_count(self):
        subscription_data = self.env['purchase.subscription'].read_group(domain=[('partner_id', 'in', self.ids)],
                                                                         fields=['partner_id'],
                                                                         groupby=['partner_id'])
        mapped_data = dict([(m['partner_id'][0], m['partner_id_count']) for m in subscription_data])
        for partner in self:
            partner.subscription_count = mapped_data.get(partner.id, 0)
    
    @api.multi
    def purchase_subscription_action_res_partner(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "purchase.subscription",
            "views": [[False, "tree"], [False, "form"]],
            "domain": [["partner_id", "=", active_id]],
            "context": {"create": False},
            "name": "Purchase Subscriptions",
        }
    