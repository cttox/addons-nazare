# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    rdgs = fields.Char(
        string='R.D.G.S'
    )
