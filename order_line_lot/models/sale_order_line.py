# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            # Logic for splitting sale order lines
            for line in order.order_line:
                product = line.product_id
                if product.tracking == 'lot':
                    values = line._prepare_procurement_values(group_id=False)
                    rule = self.env['procurement.group']._get_rule(
                        line.product_id, self.partner_shipping_id.property_stock_customer, values)

                    # Get the stock quants for the product, FIFO ordered
                    quants = self.env['stock.quant'].search([
                        ('product_id', '=', line.product_id.id),
                        ('quantity', '>', 0),
                        ('location_id', '=', rule.location_src_id.id)
                    ], order='in_date ASC')

                    total_qty = line.product_uom_qty
                    for quant in quants:
                        if total_qty <= 0:
                            break  # All product quantity has been assigned

                        lot_qty = min(quant.quantity, total_qty)
                        total_qty -= lot_qty

                        # Create a new sale order line with the lot and the lot_qty
                        self.env['sale.order.line'].create({
                            'order_id': order.id,
                            'product_id': product.id,
                            'product_uom_qty': lot_qty,
                            'x_studio_lote': quant.lot_id.id,
                            'x_studio_fecha_de_caducidad': quant.lot_id.expiration_date,
                            # Add other necessary fields here
                        })

                    # Either reduce the quantity of the original line or delete it
                    if total_qty <= 0:
                        line.unlink()  # Delete the line if fully split
                    else:
                        line.write({'product_uom_qty': total_qty})

            # Call the original confirm action at the end
            super(SaleOrder, order).action_confirm()
        return True
