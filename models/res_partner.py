# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    po_subscription_count  = fields.Integer(string='Purchase Subscriptions', compute='_po_subscription_count')

    @api.multi
    def _po_subscription_count(self):
        for partner in self:
            partner.po_subscription_count = self.env['purchase.subscription'].search_count([('partner_id', "=", partner.id)])

    @api.multi
    def purchase_subscription_action_res_partner(self):
        for partner in self:
            return {
                "type": "ir.actions.act_window",
                "res_model": "purchase.subscription",
                "views": [[False, "tree"], [False, "form"]],
                "domain": [["partner_id", "=", partner.id]],
                "context": {"create": False},
                "name": "Purchase Subscriptions",
            }
