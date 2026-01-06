from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AssetAssignment(models.Model):
    _name = 'asset.assignment'
    _description = 'Bàn giao tài sản'

    asset_id = fields.Many2one('custom.asset', string='Tài sản', required=True, ondelete='cascade')
    employee_id = fields.Many2one('nhan_vien', string='Người nhận (nhân viên)')
    room_id = fields.Many2one('room.meeting', string='Phòng nhận')
    assign_date = fields.Date('Ngày bàn giao', default=fields.Date.context_today)
    return_date = fields.Date('Ngày thu hồi')
    state = fields.Selection([('using', 'Đang sử dụng'), ('returned', 'Đã trả')], default='using')

    # Chú ý: Hàm này phải thẳng hàng với các trường fields ở trên
    @api.constrains('employee_id', 'room_id')
    def _check_assignment_target(self):
        for record in self:
            # Kiểm tra nếu chọn cả hai
            if record.employee_id and record.room_id:
                raise ValidationError("Một tài sản chỉ có thể bàn giao cho Nhân viên HOẶC Phòng họp, không thể chọn cả hai!")
            # Kiểm tra nếu không chọn cái nào
            if not record.employee_id and not record.room_id:
                raise ValidationError("Vui lòng chọn đối tượng nhận bàn giao (Nhân viên hoặc Phòng họp).")