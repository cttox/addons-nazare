# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Custom Lot Generator',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Generate custom lot numbers for products',
    'depends': ['product', 'stock', 'mrp'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_product_views.xml',
        'views/generate_lot_wizard_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
