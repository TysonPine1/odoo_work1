{
    'name': 'Experiment',
    'version': '13.0',
    'summary': 'Experiment',
    'sequence': 1,
    'depends': ['mail', 'base', 'board', 'web', 'report_xlsx'],
    'category': 'Expeimentation',
    'license': 'AGPL-3',
    'author': 'Heinrich von Helmholtz',
    'data': [
        'views/exmp.xml',
        'wizard/wizard.xml',
        'reports/report.xml',
        'reports/report_pdf_view.xml',
        'security/ir.model.access.csv',
        ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False
}