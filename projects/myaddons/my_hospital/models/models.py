# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Patients(models.Model):
    _inherit = "res.partner"

    is_patient = fields.Boolean(string="Is Patient")
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age")
    app_count = fields.Integer(string="Count", compute="get_app_count")

    def get_appointments(self):
        self.ensure_one()
        return {
            "name": _("Appointments"),
            "res_model": "the.appointments",
            "view_mode": "tree,form",
            "type": "ir.actions.act_window",
            "domain": [("patient_id", "=", self.id)],
            "context": {"default_patient_id": self.id},
        }

    def get_app_count(self):
        for rec in self:
            rec.app_count = self.env["the.appointments"].search_count(
                [("patient_id", "=", rec.id)]
            )


class ResUsers(models.Model):
    _inherit = "res.users"

    is_doctor = fields.Boolean(string="Is Doctor")
    is_supervisor = fields.Boolean(string="Is Supervisor")


class TheAppointments(models.Model):
    _name = "the.appointments"
    _description = "Appointment Module"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Appointment ID",
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
            ("draft", "Draft"),
            ("confirm", "Confirm"),
            ("done", "Done"),
            ("cancelled", "Cancelled"),
        ],
        string="Status",
        readonly=True,
        default="draft",
        tracking=True,
    )

    patient_age = fields.Integer(string="Age", related="patient_id.age")
    notes = fields.Text(string="Notes")
    doctor_notes = fields.Text(string="Doctor Notes")
    app_date = fields.Datetime(string="Date Time", required=True)
    prescription_ids = fields.One2many("the.prescription", "appointment_id")
    doctor_id = fields.Many2one(
        "res.users", string="Doctor", domain="[('is_doctor', '=', True)]"
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("name", _("New")) == _("New"):
                vals["name"] = self.env["ir.sequence"].next_by_code(
                    "the.appointments.sequence"
                ) or _("New")
        return super().create(vals_list)

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
    _description = "Prescription Module"

    name = fields.Char(string="Medicine Name")
    notes = fields.Text(string="Notes")
    appointment_id = fields.Many2one("the.appointments", string="Appointment")
    medicine_id = fields.Many2one("the.medicines", string="Medicine")


class Medicines(models.Model):
    _name = "the.medicines"
    _description = "Medicines Module"

    name = fields.Char(string="Medicine Name", required=True)
    effective_material = fields.Char(string="Effective Material")
    prescription_ids = fields.One2many("the.prescription", "medicine_id")