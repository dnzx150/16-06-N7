{
    'name': 'Quản lý Tài sản (Module A)',
    'version': '1.0',
    'summary': 'Quản lý danh mục thiết bị công ty',
    'depends': ['base'], # Module này độc lập
    'data': [
        'security/ir.model.access.csv',
        'views/asset_view.xml',
    ],
    'installable': True,
    'application': True,
}