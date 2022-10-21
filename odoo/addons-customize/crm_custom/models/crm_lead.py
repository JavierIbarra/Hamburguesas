from odoo import fields, models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    burger = fields.Integer(string="Numero de hamburguesas")
    ingredients = fields.Many2many(
        comodel_name='product.product',
        string="Ingredientes",
    )