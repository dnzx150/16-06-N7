# -*- coding: utf-8 -*-
from odoo import models, fields, api

class RoomBooking(models.Model):
    _name = 'room.booking'
    _description = 'Lịch đặt phòng họp'

    name = fields.Char(string='Mục đích họp', required=True)
    
    # KẾT NỐI VỚI HR ODOO: 'hr.employee'
    employee_id = fields.Many2one('nhan_vien', string='Nhân viên đặt phòng', required=True)
    
    room_id = fields.Many2one('room.meeting', string='Phòng họp', required=True)
    start_time = fields.Datetime(string='Bắt đầu', required=True)
    end_time = fields.Datetime(string='Kết thúc', required=True)
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('confirm', 'Đã xác nhận'),
        ('cancel', 'Đã hủy')
    ], string='Trạng thái', default='draft')