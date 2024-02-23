# -*- coding: utf-8 -*-
# from odoo import http


# class Estudios(http.Controller):
#     @http.route('/estudios/estudios', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estudios/estudios/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('estudios.listing', {
#             'root': '/estudios/estudios',
#             'objects': http.request.env['estudios.estudios'].search([]),
#         })

#     @http.route('/estudios/estudios/objects/<model("estudios.estudios"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estudios.object', {
#             'object': obj
#         })

