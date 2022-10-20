from odoo import fields, models

class ProductProduct(models.Model):
    _inherit = 'product.product'

    crm_ids = fields.Many2many(
        comodel_name='crm.lead',
        string="crm",
    )