
from odoo import models, fields, api



class ContactsNew(models.Model):
    _inherit = 'res.partner'

    my_notes = fields.Char()
    my_contacts_salas_no = fields.Char()
