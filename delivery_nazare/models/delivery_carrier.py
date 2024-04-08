# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import _, fields, models
from odoo.tools.safe_eval import safe_eval
from odoo.exceptions import UserError


class DeliveryPriceRule(models.Model):
    _inherit = 'delivery.price.rule'

    carrier_rule_name = fields.Char(
        string='Carrier',
    )


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    def base_on_rule_rate_shipment_nazare(self, order):
        carrier = self._match_address(order.partner_shipping_id)
        if not carrier:
            return {'success': False,
                    'price': 0.0,
                    'name_carrier': '',
                    'error_message': _('Error: this delivery method is not available for this address.'),
                    'warning_message': False}
        try:
            name_carrier, price_unit = self._get_price_available_nazare(order)
        except UserError as e:
            return {'success': False,
                    'price': 0.0,
                    'name_carrier': name_carrier,
                    'error_message': e.args[0],
                    'warning_message': False}

        price_unit = self._compute_currency(order, price_unit, 'company_to_pricelist')

        return {'success': True,
                'price': price_unit,
                'name_carrier': name_carrier,
                'error_message': False,
                'warning_message': False}

    def _get_price_available_nazare(self, order):
        self.ensure_one()
        self = self.sudo()
        order = order.sudo()
        total = weight = volume = quantity = 0
        total_delivery = 0.0
        for line in order.order_line:
            if line.state == 'cancel':
                continue
            if line.is_delivery:
                total_delivery += line.price_total
            if not line.product_id or line.is_delivery:
                continue
            if line.product_id.type == "service":
                continue
            qty = line.product_uom._compute_quantity(line.product_uom_qty, line.product_id.uom_id)
            weight += (line.product_id.weight or 0.0) * qty
            volume += (line.product_id.volume or 0.0) * qty
            quantity += qty
        total = (order.amount_total or 0.0) - total_delivery

        total = self._compute_currency(order, total, 'pricelist_to_company')

        return self._get_price_from_picking_nazare(total, weight, volume, quantity)

    def _get_price_from_picking_nazare(self, total, weight, volume, quantity):
        price = 0.0
        carrier_name = ''
        criteria_found = False
        price_dict = self._get_price_dict(total, weight, volume, quantity)
        if self.free_over and total >= self.amount:
            return 0
        for line in self.price_rule_ids:
            test = safe_eval(line.variable + line.operator + str(line.max_value), price_dict)
            if test:
                price = line.list_base_price + line.list_price * price_dict[line.variable_factor]
                carrier_name = line.carrier_rule_name
                criteria_found = True
                break
        if not criteria_found:
            raise UserError(_("No price rule matching this order; delivery cost cannot be computed."))

        return carrier_name, price
