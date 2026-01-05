from odoo import models, fields, api

class RoomMeeting(models.Model):
    _name = 'room.meeting'
    _description = 'Thông tin phòng họp'

    name = fields.Char(string='Tên phòng', required=True)
    capacity = fields.Integer(string='Sức chứa')
    location = fields.Char(string='Vị trí (Tầng)')
    # PHỐI HỢP: Kết nối với Module A (Many2many)
    asset_ids = fields.Many2many('custom.asset', string='Trang thiết bị trong phòng')