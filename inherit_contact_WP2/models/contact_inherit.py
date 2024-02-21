from odoo import api, fields, models
from odoo.exceptions import UserError


class ContactInherit(models.Model):
    _inherit = 'res.partner'
    
    phone = fields.Char(string="Phone")
    
    _sql_constraints = [
        ('_unique_phone_number',
         'UNIQUE(phone)',
         ('The phone number must be unique!!'))
    ]
    
    # @api.constrains('phone')
    # def _check_phone_availability(self):
    #     for rec in self:

    # _sql_constraints = [
    #     ('phone_unique', 'UNIQUE(phone)', 'The phone number must be unique!')
    # ]