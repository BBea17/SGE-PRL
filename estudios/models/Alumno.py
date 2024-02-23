from odoo import models, fields, api

class Alumno(models.Model):
    _name = 'estudios.alumno'
    _description = 'Estudios Alumno'

    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre")
    apellido = fields.Char(string="Apellido")
    dni = fields.Integer(string="DNI")
    modulos = fields.Many2many('estudios.modulo', string="Módulos")

    profesor_modulo = fields.Many2one('estudios.profesor', related='modulos.profesor', string="Profesor del Módulo", readonly=True)
    
    
    profesor_modulossss = fields.One2many('estudios.modulo', related='profesor_modulo.modulos', string="Módulos del profesor", readonly=True)