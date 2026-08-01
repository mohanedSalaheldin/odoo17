# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OwlDev(models.Model):
    _name = 'owl_dev.todo.list'
    _description = 'owl_dev todo list'

    name = fields.Char(string="Task Name")
    color = fields.Char(string="Color")
    completed = fields.Boolean(string="Completed")