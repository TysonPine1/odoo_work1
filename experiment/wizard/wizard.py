from odoo import fields, models, api
import io, base64, xlsxwriter
from datetime import date, datetime, time, timedelta
 

class CreateAttendee(models.TransientModel):
    _name = "wizard.exmp"
    _description = "Wizard Experiment"
    
    session_id = fields.Many2one("experiment.exmp", string="Session" )
    attendees = fields.Many2many("res.partner", string="Attendees")
    date = fields.Date(string='Date')
    excel_file = fields.Binary('Excel File')
    
    def action_pdf(self):
    
        data = {
            'model': 'wizard.exmp',
            'session_id': self.session_id.id,
            'attendees': self.attendees.ids,
            'date': self.date,
            'form': self.read()[0]
        }

        selected_session_id = data['form']['session_id'][0]
        selected_attendees_ids = data['form']['attendees']
        print("SELECTED____>", selected_attendees_ids)
        sessions = self.env['experiment.exmp'].search([('id', '=' , selected_session_id)]).filtered(lambda o: o.attendees)
        

        session_list = []
        for s in sessions:
            attendees_list = []
            for p in s.attendees:
                # vals = {
                #     'attendees':p.name
                # }
                attendees_list.append(p.name)
            vals = {
                'session_name':s.session_id,
                'attendees':attendees_list,
                'start_date':s.date,
            }
        
            session_list.append(vals)
        data['sessions']=session_list
                
        return self.env.ref('experiment.exmp_pdf').with_context(landscape=True).report_action(self, data=data)
     
    def get_style(slef, workbook):
        header_style = workbook.add_format({'font_name': 'Sans Serif', 'font_size': 12, 'align': 'vcenter', 'bold': True, 'text_wrap': True})
        header_style1 = workbook.add_format({'font_name': 'Sans Serif', 'font_size': 12, 'align': 'center', 'bold': True, 'text_wrap': True})
        header_style1.set_align('vcenter')
        table_header = workbook.add_format({'font_name': 'Sans Serif', 'font_size': 12, 'align': 'center', 'bold': True, 'text_wrap': True, 'border': 1, 'bg_color': '#A9D08E'})
        table_header.set_align('vcenter')
        default_style = workbook.add_format({'font_name': 'Sans Serif', 'font_size': 11, 'align': 'vcenter', 'border': 1})
        number_style1 = workbook.add_format({'font_name': 'Sans Serif', 'font_size': 11, 'num_format': '0', 'align': 'center', 'bold': True, 'border': 1})
        number_style1.set_align('vcenter')
        number_style2 = workbook.add_format({'font_name': 'Sans Serif', 'font_size': 11, 'num_format': '0', 'align': 'center', 'border': 1})
        number_style2.set_align('vcenter')
        float_style1 = workbook.add_format({'font_name': 'Sans Serif', 'font_size': 11, 'num_format': '#,##0.00', 'align': 'vcenter', 'border': 1})
        float_style2 = workbook.add_format({'font_name': 'Sans Serif', 'font_size': 11, 'num_format': '#,##0.00', 'align': 'vcenter', 'bold': True, 'border': 1})
        return header_style, header_style1, table_header, default_style, number_style1, number_style2, float_style1, float_style2   
     
    def _write_excel_data(self, workbook, sheet):
        header_style, header_style1, table_header, default_style, number_style1, number_style2, float_style1, float_style2 = self.get_style(workbook)
        
        sheet.set_column('A:A', 6)
        sheet.set_column('B:B', 15)
        sheet.set_column('C:C', 25)
        sheet.set_column('D:D', 20) 
        sheet.set_column('E:I', 15)  
        sheet.set_column('J:J', 15) 
        sheet.set_column('K:K', 35)
        
        y_offset = 0     
        sheet.merge_range(y_offset, 0, y_offset, 1, "Date", header_style)
        selected_dates = self.date.strftime('%d-%m-%Y')
        sheet.merge_range(y_offset, 2, y_offset, 4, selected_dates, header_style)

        y_offset += 1
        sheet.merge_range(y_offset, 0, y_offset, 1, "Session", header_style)
        sheet.merge_range(y_offset, 2, y_offset, 4, self.session_id.session_id or '-', header_style)

        y_offset += 1
        sheet.merge_range(y_offset, 0, y_offset, 1, "Attendees", header_style)
        branches = ', '.join(self.attendees('name')) if self.attendees else '-'
        sheet.merge_range(y_offset, 2, y_offset, 4, branches, header_style)

        y_offset += 1
        sheet.merge_range(y_offset, 0, y_offset, 5, "Sheet 1", header_style1)
        
        y_offset += 1
        sheet.write(y_offset, 0, 'No', table_header)
        sheet.write(y_offset, 1, 'Date', table_header)
        sheet.write(y_offset, 2, 'Session', table_header)
        sheet.write(y_offset, 3, 'Attendees', table_header)
      
    def action_excel(self):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        report_name = 'Excel Experiment Report(' + self.date.strftime('%d-%m-%Y') + ').xlsx'
        sheet = workbook.add_worksheet('Excel Experiment Report')
        self._write_excel_data(workbook, sheet)
        
        workbook.close()
        output.seek(0)
        generated_file = output.read()
        output.close()
        excel_file = base64.encodestring(generated_file)
        self.write({'excel_file': excel_file})
        
        if self.excel_file:
            active_id = self.ids[0]
            return {
                'type': 'ir.actions.act_url',
                'url': 'web/content/?model=wizard.exmp&download=true&field=excel_file&id=%s&filename=%s' % (active_id, report_name),
                'target': 'new',
            }
        
    