from odoo import fields, models, _

class StockInheritMoveWP(models.Model):
    _inherit = 'stock.move'

    order_type = fields.Selection(string="Order Type", selection=[('delivery', 'Delivery'), ('pickup', 'Pickup')], required=True, tracking=True)
    # order_type = fields.Selection(string="Pickup and Delivery", selection=[('sale', 'Sale'), ('purchase', 'Purchase')], required=True, tracking=True)
    driver_name = fields.Char(string="Driver Name", required=False, tracking=True)
    vehicles = fields.Char(string="Vehicles", required=False, tracking=True)
    location_id = fields.Char(string="Location", required=False, tracking=True)

    