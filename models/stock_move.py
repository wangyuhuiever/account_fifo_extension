# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools import float_is_zero


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _create_out_svl(self, forced_quantity=None):
        """Create a `stock.valuation.layer` from `self`.

        :param forced_quantity: under some circunstances, the quantity to value is different than
            the initial demand of the move (Default value = None)
        """
        svl_vals_list = []
        for move in self:
            move = move.with_context(force_company=move.company_id.id)
            valued_move_lines = move._get_out_move_lines()
            # valued_quantity = 0
            for valued_move_line in valued_move_lines:
                valued_quantity = valued_move_line.product_uom_id._compute_quantity(valued_move_line.qty_done, move.product_id.uom_id)

                if float_is_zero(forced_quantity or valued_quantity, precision_rounding=move.product_id.uom_id.rounding):
                    continue
                svl_val = move.product_id._prepare_out_svl_vals(forced_quantity or valued_quantity, move.company_id, valued_move_line.lot_id)
                svl_val.update(move._prepare_common_svl_vals())
            # svl_vals = move.product_id._prepare_out_svl_vals(forced_quantity or valued_quantity, move.company_id)
            # svl_vals.update(move._prepare_common_svl_vals())
                if forced_quantity:
                    svl_val['description'] = 'Correction of %s (modification of past move)' % move.picking_id.name or move.name
                svl_vals_list.append(svl_val)
        return self.env['stock.valuation.layer'].sudo().create(svl_vals_list)


