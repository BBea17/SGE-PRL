from odoo import models, fields, api

class CicloFormativo(models.Model):
    _name = 'estudios.cicloformativo'
    _description = 'Estudios Ciclo Formativo'

    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre")