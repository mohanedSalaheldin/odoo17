# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AddAppointmentWizard(models.TransientModel):
    _name = "add.appointment"
    _description = "Add Appointment Wizard"

    patient_id = fields.Many2one(
        "res.partner",
        string="Patient",
        required=True,
        domain="[('is_patient', '=', True)]",
    )
    doctor_id = fields.Many2one(
        "res.users", string="Doctor", domain="[('is_doctor', '=', True)]"
    )
    note = fields.Text(string='Notes')
    app_date = fields.Datetime(string='Date')

    def action_confirm_appointment(self):
        print("--------------- ok ---------------")
