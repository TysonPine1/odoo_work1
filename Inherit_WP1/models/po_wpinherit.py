from odoo import api, fields, models, _
from odoo.exceptions import UserError
from addons.purchase_stock.models.purchase import PurchaseOrder as Purchase
from odoo.tools.float_utils import float_compare, float_round

class PurchaseOrderWP(models.Model):
    _inherit = 'purchase.order'

    order_type = fields.Selection(string="Order Type", selection=[('delivery', 'Delivery'), ('pickup', 'Pickup')], required=True, tracking=True)
    # order_type = fields.Selection(string="Pickup and Delivery", selection=[('sale', 'Sale'), ('purchase', 'Purchase')], required=True, tracking=True)
    driver_name = fields.Char(string="Driver Name", required=False, tracking=True)
    vehicles = fields.Char(string="Vehicles", required=False, tracking=True)
    location_id = fields.Char(string="Location", required=False, tracking=True)

    @api.model   
    def _prepare_picking(self):
        res = super(PurchaseOrderWP, self)._prepare_picking()
        res['order_type'] = self.order_type
        res['driver_name'] = self.driver_name
        res['vehicles'] = self.vehicles
        return res
    
    # ** This code below fucking WORKS, DONT DELETE it!! **
    def action_wp_filter(self):
        selected_order_type = self.order_type
        filtered_purchase_orders = self.env['purchase.order'].search([('order_type', '=', selected_order_type)])
        # purchase_order = self.env['purchase.order'].search([])
        wizard = self.env['po.inherit.wizard'].create({})
        wizard.purchase_order_ids = [(6, 0, filtered_purchase_orders.ids)]
        return  {   
            'name' : 'Filter PO',
            'type' : 'ir.actions.act_window',
            'res_model' : 'po.inherit.wizard',
            'res_id' : wizard.id,
            'view_mode' : 'form',
            'target' : 'new',
        }
    
    @api.constrains('vehicles', 'driver_name', 'location_id')
    def _check_available_vehicles(self):
        for rec in self:
            if rec.vehicles and rec.driver_name and rec.location_id:
                tangled_order = self.env['purchase.order'].search([
                    ('vehicles', '=', rec.vehicles), 
                    ('driver_name', '=', rec.driver_name),
                    ('location_id', '!=', rec.location_id), 
                    ('id', '!=', rec.id)
                ])
                if tangled_order:
                    raise UserError(('You can\'t be on another location when you are already at %s!!') % (rec.location_id))
    # def action_wp_filter(self):
    #     wizard = self.env['po.inherit.wizard'].create({
    #         'purchase_order':self.id,
    #     })
    #     return {
    #         'name' : 'Filter PO',
    #         'type' : 'ir.actions.act_window',
    #         'res_model' : 'po.inherit.wizard',
    #         'view_mode' : 'form',
    #         'target' : 'new',
    #         'res_id' : wizard.id,   
    #     }
    # def action_wp_filter(self):
    #     action = self.env.ref('Inherit_WP1.action_powizard_form').read()[0]
    #     action['context'] = {
    #         'default_order_type': self.order_type,
    #         'default_driver_name': self.driver_name,
    #         'default_vehicles': self.vehicles,
    #         'active_id': self.id
    #     }
    #     return action   
    
    #? Don't even think about deleting this block
    #    # def action_wp_filter(self):
    #     return {
    #         'name' : 'PO Wizard',
    #         'type' : 'ir.actions.act_window',
    #         'res_model' : 'po.inherit.wizard',
    #         'view_mode' : 'form',
    #         'target' : 'new',
    #         'context' : {'default_order_type': self.order_type}
    #     }
    #? got it!!!??
    # def action_wp_filter(self):
    #         selection = self.order_type
    #         return {
    #         'name' : 'PO Wizard',
    #         'type' : 'ir.actions.act_window',
    #         'res_model' : 'po.inherit.wizard',
    #         'view_mode' : 'form ',
    #         'veiw_id' : self.env.ref('Inherit_WP1.view_powizard_form').id,
    #         # 'domain' : [('order_type', '=', self.order_type)],
    #         'context' : {'selection': selection},
    #         'target' : 'new',
    #     }
        
    # def select_option(self):
    #     return  {
    #         'name': 'Select Option',
    #         'type' : 'ir.actions.act_window',
    #         'res_model' : 'po.inherit.wizard',
    #         'view_mode' : 'form',
    #         'target' : 'new',
    #         'context' : {'default_order_type': self.order_type}
    #     }
        # return {
        #     'name' : 'PO Wizard',
        #     'type' : 'ir.actions.act_window',
        #     'res_model' : 'po.inherit.wizard',
        #     'view_mode' : 'tree',
        #     'veiw_id' : self.env.ref('Inherit_WP1.view_powizard_form').id,
        #     'domain' : [('order_type', 'in', show.ids)],
        #     'target' : 'new',
        # }
        
class StockMovingWP(models.Model):
    _inherit = 'purchase.order.line'
    
    order_type = fields.Selection(string="Order Type", selection=[('delivery', 'Delivery'), ('pickup', 'Pickup')], readonly=True, tracking=True)
    # order_type = fields.Selection(string="Pickup and Delivery", selection=[('sale', 'Sale'), ('purchase', 'Purchase')], readonly=True, tracking=True)
    driver_name = fields.Char(string="Driver Name", readonly=True, tracking=True)
    vehicles = fields.Char(string="Vehicles", readonly=True, tracking=True)
    
    @api.model
    def _prepare_stock_moves(self, picking):
        res = super(StockMovingWP, self)._prepare_stock_moves(picking)
        purchase_oder = self.env['purchase.order'].search([('id', '=', self.order_id.id)])
        for move in res:
            move['order_type'] = purchase_oder.order_type
            move['driver_name'] = purchase_oder.driver_name
            move['vehicles'] = purchase_oder.vehicles
        return res