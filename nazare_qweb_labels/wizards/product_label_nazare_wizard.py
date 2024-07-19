# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models, api

class ProductLabelWizard(models.TransientModel):
    _name = 'product.label.wizard'
    _description = 'Product Label Wizard'

    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True
    )

    lot_id = fields.Many2one(
        'stock.lot',
        string='Lot',
        domain="[('product_id', '=', product_id),('quantity', '>', 0)]",
        required=True
    )

    use_date = fields.Datetime(
        string='Use date',
        related='lote_id.use_date',
        readonly=True
    )

    quantity = fields.Float(
        string='Quantity',
        required=True)

    uom_id = fields.Many2one(
        'uom.uom',
        string='Contenido',
        required=True
    )

    ingredients = fields.Html(
        string='Ingredients',
        related='product_id.ingredients',
        readonly=False
    )

    rdgs = fields.Char(
        string='R.D.G.S',
        related='company_id.rdgs',
        readonly=True
    )

    description_pickingout = fields.Char(
        string='Description Picking Out',
        related='product_id.description_pickingout',
        readonly=False
    )

    title = fields.Char(
        string='Title',
        required=True
    )

    label_type = fields.Selection([
        ('master_box', 'Master Box'),
        ('in_bulk', 'In Bulk')
    ], string='Label type', required=True)

    @api.multi
    def print(self):
        self.ensure_one()
        if self.tipo_de_etiqueta == 'master_box':
            return self.env.ref(
                'product_label_wizard.report_label_master').report_action(self)
        else:
            return self.env.ref(
                'product_label_wizard.report_label_granel').report_action(self)
