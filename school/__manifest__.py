# -*- coding: utf-8 -*-
{
    'name': "Administración de escuela",

    'summary': "Crea estudiantes para tu escuela",

    'description': """
Long description of module's purpose
    """,

    'author': "Javier",
    'website': "https://www.javier.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Education',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'imagens': ['static/description/icon.png'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/students_tag.xml',
        'views/carreers.xml',
        'views/subjects.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

