from odoo import models, fields, api


class LichSuCongTac(models.Model):
    _name = 'lich_su_cong_tac'
    _description = 'Lich sử công tác của nhân sự'

    chuc_vu_id = fields.Many2one('danh_muc_chuc_vu', string="Chức vụ")
    chuc_vu = fields.Char(related='chuc_vu_id.name', string="Tên chức vụ", store=True)
    nhan_vien_id = fields.Many2one('nhan_vien', string="Nhân viên") 
    ten_nhan_vien = fields.Char(related='nhan_vien_id.name', string="Tên nhân viên", store=True)
    don_vi_id = fields.Many2one('danh_muc_don_vi', string="Đơn vị")
    ten_don_vi = fields.Char(related='don_vi_id.name', string="Tên đơn vị", store=True)


    ngay_bat_dau = fields.Date("Ngày bắt đầu")
    ngay_ket_thuc = fields.Date("Ngày kết thúc")