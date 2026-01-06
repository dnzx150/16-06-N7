from odoo import models, fields, api

class RoomMeeting(models.Model):
    _name = 'room.meeting'
    _description = 'Thông tin phòng họp'

    name = fields.Char(string='Tên phòng', required=True)
    capacity = fields.Integer(string='Sức chứa')
    location = fields.Char(string='Vị trí (Tầng)')
    # PHỐI HỢP: Kết nối với Module A (Many2many)
    asset_ids = fields.Many2many('custom.asset', string='Trang thiết bị trong phòng')
    room_type_id = fields.Many2one('room.type', string='Loại phòng')
    assignment_ids = fields.One2many('asset.assignment', 'room_id', string='Tài sản hiện có')