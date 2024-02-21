from odoo import models, fields, api

class Exmp(models.Model):
    _name = 'experiment.exmp'
    _description = 'experiment.exmp'
    
    session_id = fields.Char(string="Course", required=True)
    attendees = fields.Many2many('res.partner', string="Attendees")
    date = fields.Date(string="Date", required=True)
    description = fields.Html(string="Description")