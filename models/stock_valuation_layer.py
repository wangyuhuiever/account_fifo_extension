# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockValuationLayer(models.Model):
    _inherit = "stock.valuation.layer"

    move_lines = fields.One2many(related='stock_move_id.move_line_ids')

    @api.constrains('move_lines')
    def constraint_lot_cost(self):
        for rec in self:
            if rec.quantity > 0 and rec.move_lines:
                for ml in rec.move_lines:
                    ml.lot_id.cost = rec.unit_cost

