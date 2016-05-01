# -*- coding: utf-8 -*-
from openerp import http

# class Moviebase(http.Controller):
#     @http.route('/moviebase/moviebase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/moviebase/moviebase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('moviebase.listing', {
#             'root': '/moviebase/moviebase',
#             'objects': http.request.env['moviebase.moviebase'].search([]),
#         })

#     @http.route('/moviebase/moviebase/objects/<model("moviebase.moviebase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('moviebase.object', {
#             'object': obj
#         })