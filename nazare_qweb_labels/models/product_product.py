# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    ingredients = fields.Html(
        string='Ingredients'
    )
    label_title = fields.Html(
        string='Title',
    )
    label_quantity = fields.Float(
        string='Quantity',
    )
    label_uom_id = fields.Many2one(
        'uom.uom',
        string='Contenido',
    )

    def action_open_label_layout_nazare(self):
        action = self.env['ir.actions.act_window']._for_xml_id(
            'nazare_qweb_labels.action_open_label_layout_nazare')
        action['context'] = {'default_product_id': self.id}
        return action
