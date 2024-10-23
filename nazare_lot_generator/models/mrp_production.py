# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models
from datetime import datetime

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def action_generate_serial(self):
            self.ensure_one()
            if self.product_id.tracking == 'lot':
                if self.product_id.default_code:
                    first_two = self.product_id.default_code[:1]
                    last_two = self.product_id.default_code[-2:]
                    current_year = str(datetime.now().year)[-2:]
                    day_of_year = datetime.now().timetuple().tm_yday
                    lot_number = f"{first_two}{last_two}{current_year}{day_of_year:03d}"

                    lot = self.env['stock.lot'].create({
                        'name': lot_number,
                        'product_id': self.product_id.id,
                        'company_id': self.company_id.id,
                    })
                    self.lot_producing_id = lot.id
                else:
                    return super(MrpProduction, self).action_generate_serial()
            else:
                return super(MrpProduction, self).action_generate_serial()
