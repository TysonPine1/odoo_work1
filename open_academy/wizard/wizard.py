from odoo import api, fields, models

class CreateAttendee(models.TransientModel):
    _name = "create.wizard"
    _description = "Create Attendee"
    
    session_id = fields.Many2one("openacademy.session", string="Session" )
    partner_id = fields.Many2many("res.partner", string="Attendees")
    course_id = fields.Many2one("openacademy.course",'Course')
    date = fields.Date(string='Date')
    
   
            