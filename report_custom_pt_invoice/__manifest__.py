# -*- coding: utf-8 -*-
{
    'name': 'Personalizzazione Report Fatture',
    'version': '10.0.1.0.0',
    'category': 'Localization',
    'license': 'AGPL-3',
    'summary': 'Report personalizzato per Fatture',
    'description': """
        Report personalizzato per Fatture
    """,
    'author': 'LP',
    'website': 'https://pretecno.it',
    'depends': ['account','report_custom_pt_base'],
    'data': [
        'views/templates.xml',
    ],
    'installable': True,
}
