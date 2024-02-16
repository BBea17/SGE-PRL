# -*- coding: utf-8 -*-
# se importan siempre #
from odoo import models, fields, api

class medico(models.Model):
    _name = 'hospital.medico'
    _description = 'hospital.medico'
     
    nombre = fields.Char("Nombre del médico")
    apellido = fields.Char("Apellido del médico")
    num_colegiado = fields.Integer("Número de colegiado:")
    diagnosticoMedico = fields.One2many('hospital.diagnostico','relMedico')


class paciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'hospital.paciente'
     
    nombre = fields.Char("Nombre del paciente:")
    apellido = fields.Char("Apellido del paciente:")
    sintoma = fields.Char("Síntomas del paciente:")

    diagnosticoPaciente = fields.One2many('hospital.diagnostico','relPaciente')


class diagnostico(models.Model):
    _name = 'hospital.diagnostico'
    _description = 'hospital.diagnostico'

    sintoma = fields.Char()
    descripcion = fields.Char()

    relPaciente = fields.Many2one('hospital.paciente')
    relMedico = fields.Many2one('hospital.medico')


