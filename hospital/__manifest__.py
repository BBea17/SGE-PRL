# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': "Práctica 3 SGE: PRL, hospital.",

    'description': """
Long description of module's purpose
    """,

    'author': "Pablo Romero Lorenzo",
    'website': "https://www.empresaPRL.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # importar las vistas que queremos
    'data': [
        'security/ir.model.access.csv',
        'views/paciente.xml',
        'views/medico.xml',
        'views/diagnostico.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

