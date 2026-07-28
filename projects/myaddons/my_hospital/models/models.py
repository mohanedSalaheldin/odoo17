# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Patients(models.Model):
    _inherit = "res.partner"

    is_patient = fields.Boolean(string="Is Patient")
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age")
    app_count = fields.Integer(string="Count", compute="get_app_count")

    def get_appointments(self):
        action = {
            "name": "appointments",
            "res_model": "the.appointments",
            "view_id": False,
            "view_mode": "tree,form",
            "type": "ir.actions.act_window",
            "domain": [("patient_id", "=", self.id)],
        }
        return action

    def get_app_count(self):
        count = self.env["the.appointments"].search_count(
            [("patient_id", "=", self.id)]
        )
        self.app_count = count


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

    state = fields.Selection(
        [
            ("draft", "draft"),
            ("confirm", "confirm"),
            ("done", "done"),
            ("cancelled", "cancelled"),
        ],
        string="Status",
        readonly=True,
        default="draft",
    )

    patient_age = fields.Integer(string="Age", related="patient_id.age")
    notes = fields.Text(string="Notes")
    doctor_notes = fields.Text(string="Doctor Notes")
    app_date = fields.Datetime(string="Date Time", required=True)
    prescription_ids = fields.One2many('the.prescription', 'appointment_id')
    doctor_id = fields.Many2one('res.users', string="Doctor", domain="[('is_doctor', '=', True)]")


    @api.model
    def create(self, vals):
        if vals.get("name", _("New")) == _("New"):
            vals["name"] = self.env["ir.sequence"].next_by_code(
                "the.appointments.sequence"
            ) or _("New")
        result = super().create(vals)
        return result

    def action_confirm(self):
        for item in self:
            item.state = "confirm"

    def action_done(self):
        for item in self:
            item.state = "done"
            
    def action_cancel(self):
        for item in self:
            item.state = "cancelled"


class Prescription(models.Model):
    _name = "the.prescription"

    name = fields.Char(string="Medicine Name")
    notes = fields.Text(string="Notes")
    appointment_id = fields.Many2one('the.appointments', string="Appointment")
    medicine_id = fields.Many2one('the.medicines', string="Medicine")



class Medicines(models.Model):
    _name = 'the.medicines'

    name = fields.Char(string='Medicine Name', required=True)
    effective_material = fields.Char(string="Effective Material")
    prescription_ids = fields.One2many('the.prescription', 'medicine_id')