# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import odoorpc

# esta es la base para crear una bd de prueba, habria que instalarle un modulo
# todavia no se como hacerlo

odoo = odoorpc.ODOO('localhost', port=8069)

odoo.db.create('admin', 'product_autoload_test', demo=True)
