# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Sale order line lot number',
    'version': '1.0.0.0',
    'category': 'Sales/Sales',
    'summary': '',
    'description': "Retrieve the lot number and expiry date from lot into the sale order line",
    'author': "Cesar Barron",
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'assets': {
    },
    'application': True,
    'license': 'LGPL-3'
}
