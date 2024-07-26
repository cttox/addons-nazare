# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_open_label_layout_nazare(self):
        action = self.product_variant_ids[0].action_open_label_layout_nazare()
        return action
