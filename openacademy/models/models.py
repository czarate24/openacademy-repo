# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Clase o modulo para definir cursos'
     
    name = fields.Char(string="Title", required=True)
    description = fields.Text()