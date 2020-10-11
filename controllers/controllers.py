# -*- coding: utf-8 -*-
# from odoo import http


# class AccountFifoExtension(http.Controller):
#     @http.route('/account_fifo_extension/account_fifo_extension/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/account_fifo_extension/account_fifo_extension/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('account_fifo_extension.listing', {
#             'root': '/account_fifo_extension/account_fifo_extension',
#             'objects': http.request.env['account_fifo_extension.account_fifo_extension'].search([]),
#         })

#     @http.route('/account_fifo_extension/account_fifo_extension/objects/<model("account_fifo_extension.account_fifo_extension"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('account_fifo_extension.object', {
#             'object': obj
#         })
