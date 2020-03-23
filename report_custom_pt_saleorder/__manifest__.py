# -*- coding: utf-8 -*-
{
    'name': 'Personalizzazione Report Preventivi',
    'version': '10.0.1.0.0',
    'category': 'Localization',
    'license': 'AGPL-3',
    'summary': 'Report personalizzato per Preventivi / Ordini',
    'description': """
        Report personalizzato per Preventivi / Ordini
    """,
    'author': 'LP',
    'website': 'https://pretecno.it',
    'depends': ['sale','report_custom_pt_base'],
    'data': [
        'views/templates.xml',
    ],
    'installable': True,
}