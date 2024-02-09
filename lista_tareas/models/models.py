# -*- coding: utf-8 -*-

from odoo import models, fields, api
#Definimos el modelo de datos
class lista_tareas(models.Model):
    _name = 'lista_tareas.lista_tareas'
    _description = 'lista_tareas.lista_tareas'

    tarea = fields.Char()
    prioridad = fields.Integer()
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()

    # Agregamos dos variables para la vista calendar, que definirán la fecha de inicio y de fin de las tareas
    date_assign = fields.Date("Fecha de inicio")
    date_end = fields.Date("Fecha de fin")

    # Agregamos una variable Image para la imagen que se mostrará en el diseño Kanban
    imagen = fields.Image("Imagen")

    @api.depends('prioridad')

    def _value_urgente(self):
        for record in self:
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False