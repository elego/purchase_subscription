# -*- coding: utf-8 -*-

from openerp import api, fields, models


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    name                    = fields.Char(string='Analytic Account', index=True, required=True, default='New')
    code                    = fields.Char(string='Reference', index=True, default=lambda self: self.env['ir.sequence'].next_by_code('purchase.subscription') or 'New')
    po_subscription_ids     = fields.One2many('purchase.subscription', 'analytic_account_id', string='Purchase Subscriptions')
    po_subscription_count   = fields.Integer(compute='_compute_po_subscription_count', string='Purchase Susbcription Count')

    @api.multi
    def _compute_po_subscription_count(self):
        for account in self:
            account.subscription_count = len(account.po_subscription_ids)

    @api.multi
    def po_subscriptions_action(self):
        subscription_ids = self.po_subscription_ids.ids
        result = {
            "type": "ir.actions.act_window",
            "res_model": "purchase.subscription",
            "views": [[False, "tree"], [False, "form"]],
            "domain": [["id", "in", subscription_ids]],
            "context": {"create": False},
            "name": "Purchase Subscriptions",
        }
        if len(subscription_ids) == 1:
            result['views'] = [(False, "form")]
            result['res_id'] = subscription_ids[0]
        return result