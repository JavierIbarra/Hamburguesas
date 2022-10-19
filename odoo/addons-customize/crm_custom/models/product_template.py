from odoo import fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    crm_ids = fields.Many2many(
        comodel_name='crm.lead',
        column1='crm_id',
        column2='product_id',
        string="crm",
    )