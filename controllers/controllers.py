# -*- coding: utf-8 -*-
from odoo import http

# class BarcodePngGenerator(http.Controller):
#     @http.route('/barcode_png_generator/barcode_png_generator/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/barcode_png_generator/barcode_png_generator/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('barcode_png_generator.listing', {
#             'root': '/barcode_png_generator/barcode_png_generator',
#             'objects': http.request.env['barcode_png_generator.barcode_png_generator'].search([]),
#         })

#     @http.route('/barcode_png_generator/barcode_png_generator/objects/<model("barcode_png_generator.barcode_png_generator"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('barcode_png_generator.object', {
#             'object': obj
#         })