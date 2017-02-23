# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    recurring_invoice_po = fields.Boolean('Purchase Subscription')
