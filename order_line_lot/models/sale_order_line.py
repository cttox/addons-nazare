# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, api, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    lot_id = fields.Many2one(
        'stock.lot',
        string='Lot number',
    )

    date_expiry = fields.Date(
        string='Date expiration',
        related='lot_id.expiration_date',
    )


    @api.onchange('product_id', 'product_uom_qty')
    def _onchange_product_quantity(self):
        lot_list = []
        remaining_qty = self.product_uom_qty
        if self.product_id:
            # Get the stock quants for the product, FIFO ordered
            quants = self.env['stock.quant'].search([
                ('product_id', '=', self.product_id.id),
                ('quantity', '>', 0)
            ], order='in_date ASC')

            # Loop through the quants to fulfill the order line quantity using FIFO
            for quant in quants:
                if remaining_qty <= 0:
                    break
                quant_qty = quant.quantity
                if quant_qty <= remaining_qty:
                    lot_list.append((quant.lot_id, quant_qty))
                    remaining_qty -= quant_qty
                else:
                    lot_list.append((quant.lot_id, remaining_qty))
                    remaining_qty = 0

            # Now, you can use lot_list to update lot information in your order line
            # Note: You will have to consider how to handle displaying multiple lots in your view.
            # This could involve adding a One2many field to handle lot details.

            # lot_names = ', '.join([lot.name for lot, qty in lot_list])
            if lot_list:
                self.update({'lot_id': lot_list[0][0].id})

                # self.update({'x_studio_lote': lot_list[0][0].id,
                #              'x_studio_fecha_de_caducidad': lot_list[0][0].expiration_date})
