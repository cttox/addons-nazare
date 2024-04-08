# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _prepare_delivery_line_vals(self, carrier, price_unit):

        res = super()._prepare_delivery_line_vals(carrier, price_unit)
        vals = self.carrier_id.rate_shipment(self.id)
        import ipdb; ipdb.set_trace()
        return res
