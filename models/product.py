# -*- coding: utf-8 -*-
from openerp import models, fields, api


class product_template(models.Model):
    _inherit = "product.template"

    recurring_invoice_po = fields.Boolean('Purchase Subscription')
