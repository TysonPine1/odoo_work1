from odoo import models, fields, api
from odoo.exceptions import UserError
from addons.purchase_stock.models.purchase import PurchaseOrder as Purchase
    
class PickingStock(models.Model):
    _inherit = 'stock.picking'
    
    order_type = fields.Selection(string="Order Type", selection=[('delivery', 'Delivery'), ('pickup', 'Pickup')], required=True, tracking=True)
    # order_type = fields.Selection(string="Pickup and Delivery", selection=[('sale', 'Sale'), ('purchase', 'Purchase')], required=True, tracking=True)
    driver_name = fields.Char(string="Driver Name", required=False, tracking=True)
    vehicles = fields.Char(string="Vehicles", required=False, tracking=True)