from odoo import models, fields, api
class AssetMaintenance(models.Model):
    _name = 'asset.maintenance'
    _description = 'Bảo trì tài sản'
    asset_id = fields.Many2one('custom.asset', string='Tài sản', required=True, ondelete='cascade')
    maintenance_date = fields.Date('Ngày bảo trì')
    cost = fields.Float('Chi phí bảo trì')
    reason = fields.Text('Lý do/Nội dung')