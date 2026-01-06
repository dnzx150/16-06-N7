{
    'name': 'Quản lý Phòng họp (Module B)',
    'version': '1.0',
    'summary': 'Đặt phòng họp và tích hợp tài sản',
    'depends': ['base','nhan_su', 'quan_ly_tai_san'], # PHỐI HỢP TẠI ĐÂY
    'data': [
        'security/ir.model.access.csv',
        'views/room_view.xml',
        'views/booking_view.xml',
        'views/qlvp.xml',
    ],
    'installable': True,
    'application': True,
}