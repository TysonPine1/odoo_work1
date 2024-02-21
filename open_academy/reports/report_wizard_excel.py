
#!---V1 initial trial-- from odoo import models

# class ReportExcelWiz(models.AbstractModel):
#     _name = 'report.open_academy.report_excel_wiz'
#     _inherit = 'report.report_xlsx.abstract'
    
#     def generate_excel_report(self, workbook, data, lines):
#         format1 = workbook.add_format({'font_size': 14, 'align': 'vcenter', 'bold': True})
#         format2 = workbook.add_format({'font_size': 10, 'align': 'vcenter'})
#         sheet = workbook.add_worksheet('Report Excel Wiz')
#         sheet.set_column(3, 3, 50)
#         sheet.set_column(2, 2, 30)
#         sheet.write(2, 2, 'Name', format1)
#         sheet.write(2, 3, lines.session_id, format2)
#         sheet.write(3, 2, 'Date', format1)
#         sheet.write(3, 3, lines.start_date, format2)