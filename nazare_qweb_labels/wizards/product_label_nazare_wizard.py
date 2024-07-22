# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models

class ProductLabelWizard(models.TransientModel):
    _name = 'product.label.layout.nazare'
    _description = 'Product Label Nazare'

    company_id = fields.Many2one(
        comodel_name='res.company',
        string='Company',
        default=lambda self: self.env.user.company_id,
        readonly=True
    )

    product_id = fields.Many2one(
        'product.product',
        string='Product',
        required=True
    )

    lot_id = fields.Many2one(
        'stock.lot',
        string='Lot',
        domain="[('product_id', '=', product_id),('product_qty', '>', 0)]",
        required=True
    )

    use_date = fields.Datetime(
        string='Use date',
        related='lot_id.use_date',
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

    description_pickingout = fields.Text(
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
    ], string='Label type', required=True, default='master_box')

    def print(self):
        self.ensure_one()
        if self.label_type == 'master_box':
            return self.env.ref(
                'nazare_qweb_labels.report_label_master').report_action(self)
        else:
            return self.env.ref(
                'nazare_qweb_labels.report_label_granel').report_action(self)