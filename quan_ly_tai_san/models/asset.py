from odoo import models, fields, api

class CustomAsset(models.Model):
    _name = 'custom.asset'
    _description = 'Tài sản công ty'

    name = fields.Char(string='Tên tài sản', required=True)
    code = fields.Char(string='Mã tài sản', required=True)
    category = fields.Selection([
        ('electronic', 'Thiết bị điện tử'),
        ('furniture', 'Nội thất'),
        ('other', 'Khác')
    ], string='Loại tài sản', default='electronic')
    status = fields.Selection([
        ('available', 'Sẵn sàng'),
        ('using', 'Đang sử dụng'),
        ('broken', 'Hỏng/Bảo trì')
    ], string='Trạng thái', default='available')