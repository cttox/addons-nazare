# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def action_open_label_layout_nazare(self):
        action = self.product_id.action_open_label_layout_nazare()
        action['context']['default_lot_id'] = self.lot_producing_id.id
        return action
