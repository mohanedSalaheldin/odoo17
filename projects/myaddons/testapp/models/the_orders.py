
from odoo import models, fields, api

class MyOrder(models.Model):
    _name = 'my.order'
    _description = 'My Order'

    order_des = fields.Char()
    name = fields.Char()
    item_ids = fields.One2many('my.order.item', 'order_id')
    state = fields.Selection([('new', 'New'), ('ready', 'Ready')], default='new')

    def event_ready(self):
        self.write({'state': 'ready'})

class MyItem(models.Model):
    _name = 'my.order.item'
    _description = 'My Order Line'


    name = fields.Char()
    item_name = fields.Char()
    item_price = fields.Char()
    qty = fields.Integer()

    order_id = fields.Many2one('my.order', domain="[('state','=','ready')]")

