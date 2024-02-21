{
    'name': 'Inherit WorkPlace',
    'version': '13.0',
    'summary': 'Work Inherit',
    'sequence': 1,
    'depends': ['mail', 'base', 'board', 'web', 'report_xlsx', 'purchase', 'stock', 'purchase_stock', 'stock_account'],
    'category': 'Work Related',
    'license': 'AGPL-3',
    'author': 'Heinrich von Helmholtz',
    'data': [
        'views/po_wpinherit_view.xml',
        'views/smove_wpinherit_view.xml',
        'wizard/wizard_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False
}