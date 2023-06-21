{
    'name': 'Billboard Advertisement',
    'summary': '',
    'version': '16.0.1',
    'author': "aleemcaan",
    'category': 'Sales/Sales',
    'license': 'LGPL-3',
    'images': [],
    'website': "",
    'description': """ """,
    'depends': [
        'product', 'stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/report_templates.xml',
        'reports/billboard_catalog_report.xml',
        'reports/billboard_catalog_report_templates.xml',
    ],
    'auto_install': True,
    'installable': True,
}
