from odoo import models, fields, api

class Modulo(models.Model):
    _name = 'estudios.modulo'
    _description = 'Estudios Módulo'

    _rec_name='nombre'

    nombre = fields.Char(string="Nombre")
    ciclo = fields.Many2one('estudios.cicloformativo', string="Ciclo Formativo")
    profesor = fields.Many2one('estudios.profesor', string="Profesor")
    alumnos = fields.Many2many('estudios.alumno', string="Alumnos")