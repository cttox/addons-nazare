# Copyright 2024, Cesar Barron
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "Nazare custom Qweb labels",
    "description": """Adds custom label formats""",
    "summary": """This module adds some custom label formats
    for products
    """,
    "category": "Reporting",
    "version": "16.0.1.0.0",
    'author': 'Cesar Barron',
    'company': 'e-Fector TI',
    'maintainer': 'Cesar Barron',
    "depends": ['stock', 'sale'],
    "data": [
        'security/ir.model.access.csv',
        'data/report_paperformat.xml',
        'data/report_layout.xml',
        'views/product_product_views.xml',
        'views/res_company_views.xml',
        'wizards/product_label_nazare_wizard_views.xml',
        'reports/report_templates.xml',
        'reports/reports.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
