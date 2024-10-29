# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.fields import Many2one
from datetime import date


class Person(models.Model):
    _name = 'persons_modul.person'
    _description = 'Person'
    _rec_name = 'full_name'

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    full_name = fields.Char(string='Fell Name', compute='_compute_full_name', store=True)
    birthday = fields.Date(string='Birthday')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    sex = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('non_binary', 'Non_Binary')
    ])
    company_id = Many2one('res.company', string='Company', default=lambda self: self.env.company)

    @api.depends('first_name', 'last_name')
    def _compute_full_name(self):
        for record in self:
            record.full_name = f'{record.first_name} {record.last_name}'

    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                to_day = date.today()
                age = to_day.year - record.birthday.year
                if (to_day.month, to_day.day) < (record.birthday.month, record.birthday.day):
                    age -= 1
                record.age = age
            else:
                record.age = 0
