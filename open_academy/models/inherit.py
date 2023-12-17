from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    instructor = fields.Boolean(string="Instructor", default=False)
    session_name = fields.Many2many('openacademy.session', string="Session Name")
    
# class PartnerCategory(models.Model):
#     _inherit = 'res.partner.category'

#     name = fields.Char(string='Category Name', required=True)

# class CategoryAdd(models.Model):
#     _name = 'category.setup'
#     _description = 'Category setup'

#     @api.model
#     def create_partner_categories(self):
#         partner_category_data = [
#             {'name': 'Teacher / Level 1'},
#             {'name': 'Teacher / Level 2'},
#         ]

#         for data in partner_category_data:
#             self.env['res.partner.category'].create(data)

#         return True