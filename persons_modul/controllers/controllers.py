# -*- coding: utf-8 -*-
from odoo import http


class PersonsModul(http.Controller):
    @http.route('/persons', auth='public', website=True)
    def index(self, **kw):
        Persons = http.request.env['persons_modul.person']
        return http.request.render('persons_modul.listing', {
            'persons': Persons.search([], limit=5),
        })

    @http.route('/persons/add', type='http', auth='public', website=True)
    def persons_add_form(self, **kwargs):
        return http.request.render('persons_modul.persons_add_template')

    @http.route('/persons/create', type='http', auth='public', methods=['POST'], website=True, csrf=True)
    def persons_create(self, **post):
        http.request.env['persons_modul.person'].sudo().create({
            'first_name': post.get('first_name'),
            'last_name': post.get('last_name'),
            'birthday': post.get('birthday'),
            'sex': post.get('sex'),
            'company_id': int(post.get('company_id')),
        })
        return http.request.redirect('/persons')
