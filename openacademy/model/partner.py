# -*- coding: utf-8 -*-
from openerp import fields,models


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(defautl=False)
    
    session_ids = fields.Many2many('openacademy.session',
                                   string="Session as attendee",readonly=True)
