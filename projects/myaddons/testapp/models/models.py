# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.fields import Datetime


class TestApp(models.Model):
    _name = 'testapp.testapp'
    _description = 'testapp.testapp'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='UserName', required=True, tracking=True)
    value = fields.Integer()
    value2 = fields.Float()
    description = fields.Text()
    is_gentleman = fields.Boolean(string="Is Male")
    binary = fields.Binary()
    selection = fields.Selection([('key1','val1'),('key2','val2')])
    date = fields.Datetime(default=Datetime.today())
    computed = fields.Float(readonly=True, compute='_value_pc')
    state = fields.Selection([('new','New'),('accepted','Accepted'),('rejected','Rejected')], default='new')

    _sql_constraints = [
        ('uniq_name', 'unique(name)', 'Name Should be Unique')
    ]


    cal1 = fields.Float(string='num1')
    cal2 = fields.Float(string='num2')
    result = fields.Float(string='num1+num2', readonly=True)

    @api.constrains('value')
    def _depends_on(self):
        if self.value >= 36 or self.value <= 26:
            raise ValidationError(_('Value Should be between 25 and 35'))


    @api.onchange('cal2')
    def on_change_value(self):
        self.result = self.cal1 + self.cal2

    @api.depends('result')
    def _value_pc(self):
        for record in self:
            record.computed = float(record.value) / 100

    def event_new(self):
        self.write({'state': 'new'})

    def event_accepted(self):
        self.write({'state': 'accepted'})

    def event_rejected(self):
        self.write({'state': 'rejected'})