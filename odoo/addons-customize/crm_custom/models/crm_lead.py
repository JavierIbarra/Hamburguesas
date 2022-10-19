from odoo import fields, models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    burger = fields.Integer()
    ingredients = fields.One2many(
        comodel_name='product.product',
        inverse_name='crm_ids',
        column1='crm_id',
        column2='product_id',
        string="Ingredientes",
    )