# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class DeliveryPriceRule(models.Model):
    _inherit = 'delivery.price.rule'

    carrier_rule_name = fields.Char(
        string='Carrier',
    )
