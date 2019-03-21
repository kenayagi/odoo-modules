# -*- coding: utf-8 -*-
# Copyright 2019 Sergio Corato
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
{
    'name': 'DDT report',
    'version': '10.0.1.0.0',
    'category': 'other',
    'author': 'Sergio Corato',
    'website': 'https://efatto.it',
    'license': 'AGPL-3',
    'description': '''This module add better DDT report.''',
    'depends': ['l10n_it_ddt', 'report_qweb_element_page_visibility'],
    'data': ['views/report_ddt.xml',
             'views/report_view.xml',],
    'installable': True,
}