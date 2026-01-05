from odoo import models, fields, api


class DanhMucChucVu(models.Model):
    _name = 'danh_muc_chuc_vu'
    _description = 'Danh mục chức vụ'
    name = fields.Char("Tên chức vụ", required=True)
    ma = fields.Char("Mã chức vụ", required=True)
    phu_cap = fields.Float("Phụ cấp chức vụ")
    ghi_chu = fields.Text("Ghi chú")