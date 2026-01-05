from odoo import models, fields, api


class DanhMucChungChi(models.Model):
    _name = 'danh_muc_chung_chi'
    _description = 'Danh mục chứng chỉ của nhân sự'
    
    name = fields.Char("Tên chứng chỉ", required=True)
    ma = fields.Char("Mã chứng chỉ", required=True)
    noi_cap = fields.Char("Nơi cấp", required=True)
    ngay_cap = fields.Date("Ngày cấp", required=True)
    hieu_luc = fields.Date("Hiệu lực", required=True)
    loai_chung_chi = fields.Selection([
        ('chuyen_mon', 'Chuyên môn'),
        ('ngoai_ngu', 'Ngoại ngữ'),
        ('tin_hoc', 'Tin học'),
        ('khac', 'Khác')
    ], string="Loại chứng chỉ", required=True)
    mo_ta = fields.Text("Mô tả")