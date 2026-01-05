from odoo import models, fields, api


class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'
    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    name = fields.Char("Họ và tên", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    tuoi = fields.Integer("Tuổi", compute="_compute_tuoi", store = False)
    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    so_bhxh = fields.Char("Số bảo hiểm xã hội", required=True)
    ngay_tham_gia = fields.Date("Ngày tham gia")
    chuyen_mon = fields.Char("Chuyên môn")
    
    lich_su_cong_tac_ids = fields.One2many('lich_su_cong_tac', 'nhan_vien_id', string="Lịch sử công tác")
    
    @api.depends('ngay_sinh')
    def _compute_tuoi(self): # type: ignore
        for record in self:
            if record.ngay_sinh:
                record.tuoi = fields.Datetime.today().year - record.ngay_sinh.year
            else:
                record.tuoi=0