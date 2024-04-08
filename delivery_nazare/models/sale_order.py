# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _prepare_delivery_line_vals(self, carrier, price_unit):

        res = super()._prepare_delivery_line_vals(carrier, price_unit)

        # Nazare new methos will only works on "Baed on rule" delivery types
        if carrier.delivery_type != 'base_on_rule':
            return res
        vals = self.carrier_id.base_on_rule_rate_shipment_nazare(self)
        name = (res['name'], vals['name_carrier'])
        res['name'] = ' - '.join(name)
        return res
