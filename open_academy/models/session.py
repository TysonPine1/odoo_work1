from odoo import fields, models, api, exceptions

class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'OpenAcademy Sessions'
    
    session_name = fields.Char(string="Session Name", required=True)
    start_date = fields.Datetime(string="Start Date", default=fields.Date.today, required=True)
    active = fields.Boolean(string='Active', default=True)
    seat = fields.Integer(string="Seat", required=True)
    booked_seat = fields.Integer(string="Booked Seat")
    percentage_of_taken_seat = fields.Float(string="Percentage of taken seats", compute="_compute_percentage_of_taken_seat", store=True)
    description_S = fields.Html(string="Description")
    attendees = fields.Many2many('res.partner', string="Attendees")
    instructor = fields.Many2one('res.partner', string="Instructor", domain="[('instructor', '=', True) | ('teacher_categories','!=',False)]")
    participants = fields.Integer(string="Participants")
    responsible = fields.Many2one('res.users')
    course = fields.Many2one('openacademy.course', string='Course')
    attendees_count = fields.Integer(string="Number of attendees", compute="_compute_attendees_count")
    # duration = fields.Integer(string="Duration")    
    
    _sql_constraints = [('check_descripton_title_difference', 'CHECK(description <> title)', 'Course description and title must be different!')]
    
    @api.depends('booked_seat', 'seat')
    def _compute_percentage_of_taken_seat(self):
        for session in self:
            if session.seat > 0:
                session.percentage_of_taken_seat = (session.booked_seat / session.seat) * 100
            else:
                session.percentage_of_taken_seat = 0
                
    @api.onchange('booked_seat', 'participants')
    def _onchange_validate_seat(self):
        if self.participants and self.seat and self.participants > self.seat:
            raise exceptions.UserError("Participants cannot exceed total seats!")
        if self.booked_seat and self.booked_seat < 0:
            raise exceptions.UserError("Booked seats cannot be negative!")
        
    @api.constrains('instructor', 'attendees')
    def _check_instructor_not_in_attendees(self):
        for session in self:
            if session.instructor in session.attendees:
                raise exceptions.UserError("Instructor cannot be in attendees!")
        
    @api.depends('attendees')
    def _compute_attendees_count(self):
        for record in self:
            record.attendees_count = len(record.attendees)