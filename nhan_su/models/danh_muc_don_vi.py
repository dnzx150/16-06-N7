from odoo import models, fields, api


class DanhMucDonVi(models.Model):
    _name = 'danh_muc_don_vi'
    _description = 'Danh mục đơn vị'
    name = fields.Char("Tên đơn vị", required=True)
    ma = fields.Char("Mã đơn vị", required=True)