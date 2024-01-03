from odoo import fields, models, api

class CreateAttendee(models.TransientModel):
    _name = "create.wizard"
    _description = "Create Attendee"
    
    session_id = fields.Many2one("openacademy.session", string="Session" )
    partner_id = fields.Many2many("res.partner", string="Attendees")
    course_id = fields.Many2one("openacademy.course",'Course')
    date = fields.Date(string='Date')
    
    def action_wizport(self):
    
        data = {
            'model': 'create.wizard',
            'session_id': self.session_id.id,
            'partner_id': self.partner_id.ids,
            'date': self.date,
            'form': self.read()[0]
        }

        selected_session_id = data['form']['session_id'][0]
        selected_partner_ids = data['form']['partner_id']
        print("SELECTED____>", selected_partner_ids)
        sessions = self.env['openacademy.session'].search([('id', '=' , selected_session_id)]).filtered(lambda o: o.attendees)
        

        session_list = []
        for s in sessions:
            attendees_list = []
            for p in s.attendees:
                # vals = {
                #     'attendees':p.name
                # }
                attendees_list.append(p.name)
            vals = {
                'session_name':s.session_name,
                'attendees':attendees_list,
                'start_date':s.start_date,
            }
        
            session_list.append(vals)
        data['sessions']=session_list
                
        return self.env.ref('open_academy.action_report_wiz').with_context(landscape=True).report_action(self, data=data)
    