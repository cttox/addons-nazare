# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields, api
from datetime import datetime

class GenerateLotWizard(models.TransientModel):
    _name = 'generate.lot.wizard'
    _description = 'Generate Custom Lot Wizard'

    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True
    )

    preview_lot_number = fields.Char(
        string='Preview Lot Number',
        compute='_compute_preview_lot_number'
    )

    quantity = fields.Float(
        string='Quantity',
        default=1.0,
        required=True
    )

    @api.depends('product_id')
    def _compute_preview_lot_number(self):
        for wizard in self:
            if wizard.product_id and wizard.product_id.default_code:
                first_two = wizard.product_id.default_code[:2]
                last_two = wizard.product_id.default_code[-2:]
                current_year = datetime.now().year
                day_of_year = datetime.now().timetuple().tm_yday
                wizard.preview_lot_number = f"{first_two}{last_two}{current_year}{day_of_year:03d}"
            else:
                wizard.preview_lot_number = False

    def action_generate_lot(self):
        self.ensure_one()

        lot = self.env['stock.lot'].create({
            'name': self.preview_lot_number,
            'product_id': self.product_id.id,
            'company_id': self.env.company.id,
        })

        # Create stock.quant in draft
        quant = self.env['stock.quant'].create({
            'product_id': self.product_id.id,
            'location_id': self.env.ref('stock.stock_location_stock').id,
            'lot_id': lot.id,
            'inventory_quantity': self.quantity,
        })

        # Open the stock quant tree view
        # action = self.env.ref('stock.action_update_quantity_on_hand').read()[0]
        # action['domain'] = [('product_id', '=', self.product_id.id)]
        # action['context'] = {'search_default_productgroup': 1, 'search_default_internal_loc': 1}
        return self.product_id.action_update_quantity_on_hand()
