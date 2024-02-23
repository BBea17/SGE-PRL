from odoo import models, fields, api

class Profesor(models.Model):
    _name = 'estudios.profesor'
    _description = 'Estudios Profesor'

    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre")
    apellido = fields.Char(string="Apellido")
    dni = fields.Integer(string="DNI")
    modulos = fields.One2many('estudios.modulo', 'profesor', string="Módulos")