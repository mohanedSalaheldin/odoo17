# -*- coding: utf-8 -*-
# from odoo import http


# class QwebApp(http.Controller):
#     @http.route('/qweb_app/qweb_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qweb_app/qweb_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('qweb_app.listing', {
#             'root': '/qweb_app/qweb_app',
#             'objects': http.request.env['qweb_app.qweb_app'].search([]),
#         })

#     @http.route('/qweb_app/qweb_app/objects/<model("qweb_app.qweb_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qweb_app.object', {
#             'object': obj
#         })

