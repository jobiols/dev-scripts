# -*- coding: utf-8 -*-
# For copyright and license notices, see __manifest__.py file in module root

# conectar con odoo
print 'conectando con odoo'
odoo = odoorpc.ODOO(odoo_key['server'], port=odoo_key['port'])
odoo.login(odoo_key['database'], odoo_key['username'], odoo_key['password'])
print 'conectado.'
