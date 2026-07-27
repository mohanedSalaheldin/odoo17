# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Patients(models.Model):
    _inherit = "res.partner"

    is_patient = fields.Boolean(string="Is Patient")
    birthdate = fields.Date(string="Birthdate")


class ResUser(models.Model):
    _inherit = "res.users"

    is_doctor = fields.Boolean(string="Is Doctor")


class TheAppointments(models.Model):
    _name = "the.appointments"
    _description = "Appointment module"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Apppintment ID",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: _("New"),
    )

    patient_id = fields.Many2one(
        "res.partner",
        string="Patient",
        required=True,
        domain="[('is_patient', '=', True)]",
    )

    patient_age = fields.Integer(string="Age")
    notes = fields.Text(string="Notes")
    app_date = fields.Datetime(string="Date Time", required=True)

    @api.model
    def create(self, vals):
        if vals.get("name", _("New")) == _("New"):
            vals["name"] = self.env["ir.sequence"].next_by_code(
                "the.appointments.sequence"
            ) or _("New")
        result = super().create(vals)
        return result
