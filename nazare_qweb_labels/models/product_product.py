# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    ingredients = fields.Html(
        string='Ingredients'
    )
