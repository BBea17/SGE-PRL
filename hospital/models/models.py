# -*- coding: utf-8 -*-
# se importan siempre #
from odoo import models, fields, api

#modelo medico, con sus atributos y la relación One2Many hacia el registro diagnostico
class medico(models.Model):
    _name = 'hospital.medico'
    _description = 'hospital.medico'
     
    nombre = fields.Char("Nombre del médico")
    apellido = fields.Char("Apellido del médico")
    num_colegiado = fields.Integer("Número de colegiado:")
    diagnosticoMedico = fields.One2many('hospital.diagnostico','relMedico')

#modelo paciente, con sus atributos y la relación One2Many hacia el registro diagnostico
class paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'hospital.paciente'
     
    nombre = fields.Char("Nombre del paciente:")
    apellido = fields.Char("Apellido del paciente:")
    sintoma = fields.Char("Síntomas del paciente:")

    diagnosticoPaciente = fields.One2many('hospital.diagnostico','relPaciente')

#modelo diagnostico, con sus atributos y las relaciones Many2One hacia los registros paciente y medico respectivamente
class diagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'hospital.diagnostico'

    sintoma = fields.Char()
    descripcion = fields.Char()

    relPaciente = fields.Many2one('hospital.paciente')
    relMedico = fields.Many2one('hospital.medico')


