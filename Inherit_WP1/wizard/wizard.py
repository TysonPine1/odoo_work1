from odoo import api, fields, models

class POWizardInherit(models.TransientModel):
    _name = "po.inherit.wizard"
    
    order_type = fields.Selection(string="Order Type", selection=[('delivery', 'Delivery'), ('pickup', 'Pickup')], readonly=True, tracking=True)
    driver_name = fields.Char(string="Driver Name", readonly=True, tracking=True)
    vehicles = fields.Char(string="Vehicles", readonly=True, tracking=True)

    selected_option = fields.Char(string="Selected Options", readonly=True, tracking=True)
    purchase_order_ids = fields.Many2many('purchase.order', string='Purchase Order')
     
    # def process_order(self):
    #     order = self.purchase_order
    #     if self.order_type == 'pickup':
            
    #     elif self.ord == 'delivery':
            
    #     return {'type': 'ir.actions.act_window_close'}
        
    #!! different line
        # def create_wizard(self):
        #     wizrad_id = self.env({})
        #     return {
        #         'name' : 'PO Wizard',
        #         'view_mode' : 'form',
        #         'view_type' : 'form',
        #         'res_model' : 'po.inherit.wizard',
        #         'res_id' : wizrad_id.id,
        #         'type' : 'ir.actions.act_window',
        #         'target' : 'new',
        #         'context' : 'self.env.context'
        #     }
    
    # def _get_purchase_orders(self, selection):
    #     purchase_orders = self.env['purchase.order'].search([('field_name', '=', selection)])
    #     return purchase_orders
    
    # def default_get(self, fields):
    #     res = super('POWizardInherit', self).default_get(fields)
    #     if 'purchase_order_list' in fields:
    #         selection = self.env.context.get('selection', False)
    #         if selection:
    #             purchase_orders = self.env['purchase.order'].search([])
    #             res['purchase.order_list'] = [(6, 0, purchase_orders.ids)]
    #     return list
    
    # @api.model
    # def default_get(self,fields):
    #     res = super(POWizardInherit, self).default_get(fields)
    #     order_type = self._context.get('default_order_type')
    #     if order_type:
    #         order = self.env['purchase.order'].search([('order_type', '=', order_type)])
    #         selected_option = ','.koin(order.mapped('name'))
    #         res.update({'selected_option': selected_option})
    #     return res
        
            
    # @api.depends('filter_type')
    # def _compute_filter_order(self):
    #     for wizard in self:
    #         if wizard.filter_type:
    #             if wizard.filter_type == 'delivery':
    #                 orders = self.env['purchase.order'].search([('order_type', '=', 'delivery')])
    #             elif wizard.filter_type == 'pickup':
    #                 orders = self.env['purchase.order'].search([('order_type', '=', 'pickup')])
    #             else:
    #                 orders = self.env['purchase.order'].search([])
    #             wizard.filter_order = orders.ids
    
        # filter_type = self.env['purchase.order'].sudo().search([]).mapped('order_type')
        # self.filter_type = [(option, option) for option in filter_type if option != 'delivery']
    
    # def open_filter_po(self):
    #     return {
    #         'name' : 'Filter Type',
    #         'type' : 'ir.actions.act_window',
    #         'view_mode' : 'form',
    #         'res_model' : 'po.inherit.wizard',
    #         'target' : 'new',
    #     }
    # def action_show_filpo(self):
    #     show = self.env['purchase.order'].search([('order_type', 'in', ['delivery', 'pickup'])])
    #     return {
    #         'name' : 'PO Filter',
    #         'type' :  'ir.actions.act_window',
    #         'view_mode' : 'tree',
    #         'res_model' : 'purchase.order',
    #         'domain' : [('id', 'in', show.ids)],    
    #     }