from odoo import models, fields, api

class AssetCategory(models.Model):
    _name = 'asset.category'
    _description = 'Danh mục tài sản'
    name = fields.Char('Tên danh mục', required=True)
    code = fields.Char('Mã danh mục')
    description = fields.Text('Mô tả')