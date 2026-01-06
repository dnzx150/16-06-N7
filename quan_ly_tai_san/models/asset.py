from odoo import models, fields, api

class CustomAsset(models.Model):
    _name = 'custom.asset'
    _description = 'Tài sản công ty'

    name = fields.Char(string='Tên tài sản', required=True)
    code = fields.Char(string='Mã tài sản', required=True)
    category_id = fields.Many2one('asset.category', string='Danh mục tài sản')
    maintenance_ids = fields.One2many('asset.maintenance', 'asset_id', string='Lịch sử bảo trì')
    assignment_ids = fields.One2many('asset.assignment', 'asset_id', string='Lịch sử bàn giao')
    status = fields.Selection([
        ('available', 'Sẵn sàng'),
        ('using', 'Đang sử dụng'),
        ('broken', 'Hỏng/Bảo trì')
    ], string='Trạng thái', default='available')