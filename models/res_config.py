# -*- coding: utf-8 -*-

import time
import datetime
from dateutil.relativedelta import relativedelta

import openerp
from openerp import SUPERUSER_ID
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from openerp import api, fields, models, _
from openerp.exceptions import UserError

class PurchaseSubscriptionConfigSettings(models.TransientModel):
    _name = 'purchase.subscription.config.settings'
    _inherit = 'res.config.settings'
    
    @api.model
    def _default_has_default_company(self):
        count = self.env['res.company'].search_count([])
        return bool(count == 1)

    company_id = fields.Many2one('res.company', string='Company', required=True,
        default=lambda self: self.env.user.company_id)
    has_default_company = fields.Boolean(readonly=True,
        default=lambda self: self._default_has_default_company())
