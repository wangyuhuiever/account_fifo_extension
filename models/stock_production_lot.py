# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockProductionLot(models.Model):
    _inherit = "stock.production.lot"

    cost = fields.Float('Cost')

