# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'School Management',
    'version': '1.1',
    'summary': 'School Management for  iti students',
    'depends': ['sale', 'sale_management','mail'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/create_track_view.xml',
        'views/iti_student_view.xml',
        'views/iti_track_view.xml',
        'views/skills_view.xml',
        'views/sale_order_view.xml',
        'report/report.xml',
        'report/student_template.xml'
    ],
    'installable': True,
    'application': True,
    'author': 'ITI',
    'license': 'LGPL-3',
    'sequence': 1,
}
