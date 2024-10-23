# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def action_open_lot_generator_wizard(self):
        self.ensure_one()
        if self.tracking != 'lot':
            return

        return {
            'name': 'Generate Custom Lot',
            'type': 'ir.actions.act_window',
            'res_model': 'generate.lot.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_product_id': self.id},
        }
