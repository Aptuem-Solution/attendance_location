# -*- coding: utf-8 -*-
{
    'name': "Attendance Location",

    'summary': "Calculate attendance based on office location and allowed distance",

    'description': """
        This module calculates attendance based on the office location and allowed distance. 
        It checks whether the employee's check-in location is within the allowed range of the office location.
    """,

    'author': "Gamal Ashraf",
    'website': "https://www.aptuem.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources/Attendance',
    'version': '0.1',
    'module_type': 'official',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_attendance'],

    # always loaded
    'data': [
        # 'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
