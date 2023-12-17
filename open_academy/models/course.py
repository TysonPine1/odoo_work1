from odoo import fields, models, api

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'OpenAcademy Courses'

    courses = fields.Char(string="Course Name", required=True)
    course_duration = fields.Char(string="Course Duration", required=True)
    organizer = fields.Many2one('res.users', string="Organizer", required=True)
    is_instructor = fields.Boolean(string="Instructor", default=False)
    instructor = fields.Many2one('res.partner', string="Instructor", required=True)
    session_id = fields.Many2one('openacademy.session', string="Session Name")
    description = fields.Html(string="Description")
    teacher_categories = fields.Many2many('res.partner.category', string='Teacher Categories')
    responsible = fields.Many2one('res.users')
    
    def action_wizard(self):
        # Open the wizard view
        return {
            'name': 'My Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'create.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('open_academy.view_wizard_form').id,
            'target': 'new',
            'context': {
                'default_session_id': self.session_id.id,
                'default_date': self.session_id.start_date,
                'default_partner_id': [(6,0, [self.instructor.id])],
            }
        }
        
    