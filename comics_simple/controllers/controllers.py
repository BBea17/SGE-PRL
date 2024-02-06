# -*- coding: utf-8 -*-
# from odoo import http


# class ComicsSimple(http.Controller):
#     @http.route('/comics_simple/comics_simple', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/comics_simple/comics_simple/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('comics_simple.listing', {
#             'root': '/comics_simple/comics_simple',
#             'objects': http.request.env['comics_simple.comics_simple'].search([]),
#         })

#     @http.route('/comics_simple/comics_simple/objects/<model("comics_simple.comics_simple"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('comics_simple.object', {
#             'object': obj
#         })

