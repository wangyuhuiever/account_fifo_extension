# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockValuationLayer(models.Model):
    _inherit = "stock.valuation.layer"

    def create(self, vals_list):
        res = super(StockValuationLayer, self).create(vals_list)
        for vals in vals_list:
            if 'stock_move_id' in vals and vals['quantity'] > 0:
                move = self.env['stock.move'].browse(vals['stock_move_id'])
                for ml in move.mapped('move_line_ids'):
                    ml.lot_id.cost = vals['unit_cost']
        return res

