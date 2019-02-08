# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2016  jeo Software  (http://www.jeo-soft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------

"""
Help dict
    'name':'clientname','port':'portnumber','odoover':'odoo-version'
    'repos': [
    # install repository of standard modules (1)
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
    # install multiple single repos in a installdir (2)
         {'usr': 'jobiols', 'instdir':'ml', 'repo': 'meli_oerp', 'branch': '8.0'},
         {'usr': 'jobiols', 'instdir':'ml', 'repo': 'payment_mercadopago', 'branch': '8.0'},
    # install repo with inner path (3)
         {'usr': 'jobiols', 'innerdir':'addons', 'repo': 'odoo_fpoc', 'branch': 'master'},
    ]
    'images':[
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
    ]

NOTES:
    1- standard directory structure as in all oca repos, there is a repo name with
       many modules inside.
    2- single repo structure, the repo name is the module name then you must provide an
       install dir to get things in standard form.
    3- inner repo structure, the module is located in an inner path as in
       https://github.com/ctmil/odoo_fpoc.git, you must declare the innerdir to reach the
       module and put the things in standard form.
"""

_clients = [

    #######################################################################
    #
    # ODOO V7
    #
    #######################################################################
    {'name': 'atly', 'port': '8069', 'odoover': '7.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'atly-work', 'branch': '7.0'},
         {'usr': 'jobiols', 'repo': 'atly-orig', 'branch': '7.0'},
     ],
     'images': [
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-adhoc', 'ver': '7.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    #
    # ODOO V8
    #
    #######################################################################

    {'name': 'aramis', 'port': '8069', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'cl-aramis', 'branch': '8.0',
          'host': 'bitbucket'},

         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'stock-logistics-workflow',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'journal-constraint', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-odoo-support', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoomrp-wip', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'account-financial-reporting',
          'branch': '8.0'},

     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
     ]
     },

    {'name': 'agro', 'port': '8000', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'farm', 'branch': '8.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'marco', 'port': '8003', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'multi-store', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'commission', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoomrp-wip', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'social', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'stock-logistics-warehouse', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'stock-logistics-workflow', 'branch': '8.0'},
         {'usr': 'ingadhoc', 'repo': 'website', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'serviciosbaeza-odoo-addons',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'crm', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'oca', 'repo': 'account-financial-tools', 'branch': '8.0'},
         {'usr': 'ingadhoc', 'repo': 'product', 'branch': '8.0'},
         {'usr': 'marionumza', 'repo': 'pos', 'branch': '8.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'artattack', 'port': '8002', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'customer', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'multi-store', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'pos', 'branch': '8.0'},
         {'usr': 'adhoc-dev', 'repo': 'odoo-addons', 'branch': '8.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'esmeralda', 'port': '8069', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'customer', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'power', 'port': '8069', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'customer', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'reves', 'port': '8069', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'reves', 'branch': '8.0'},

         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'stock-logistics-workflow', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'journal-constraint', 'branch': '8.0'},
         {'usr': 'ingadhoc', 'repo': 'odoo-support', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoomrp-wip', 'branch': '8.0'},

         # repos para la impresora fiscal
         {'usr': 'jobiols', 'repo': 'fiscal-printer', 'branch': '8.0'},

         #         {'usr': 'jobiols-reves', 'instdir': 'fiscal', 'repo': 'ra_fpoc', 'branch': 'master'},
         #         {'usr': 'jobiols-reves', 'instdir': 'fiscal', 'repo': 'l10n_ar_fpoc', 'branch': 'master'},
         #         {'usr': 'jobiols-reves', 'innerdir': 'addons', 'repo': 'odoo_fpoc', 'branch': 'master'},

     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },

    #######################################################################
    {'name': 'suelos', 'port': '8070', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'suelos', 'branch': '8.0'},

         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'stock-logistics-workflow', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'journal-constraint', 'branch': '8.0'},
         {'usr': 'ingadhoc', 'repo': 'odoo-support', 'branch': '8.0'},

     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################1
    {'name': 'test', 'port': '8001', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-product', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         #         {'usr': 'jobiols', 'repo': 'cursos', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'knowledge', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'bank-statement-import', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoomrp-wip', 'branch': '8.0'},
         # lo sacaron de la oca lo necesito por el recalculate_prices
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'social', 'branch': '8.0'},
         # lo pide por un modulo lote lock o algo parecido al instalar base vacia
         {'usr': 'oca', 'repo': 'stock-logistics-warehouse', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'stock-logistics-workflow', 'branch': '8.0'},
         {'usr': 'ingadhoc', 'repo': 'website', 'branch': '8.0'},

         #         {'usr': 'oca', 'repo': 'product-variant', 'branch': '8.0'},
         # connector
         {'usr': 'jobiols', 'repo': 'connector', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'connector-ecommerce', 'branch': '8.0'},
         # requerido por connector - ecommerce para automatizar el sale workflow
         {'usr': 'jobiols', 'repo': 'sale-workflow', 'branch': '8.0'},
         # cosas como m2mcategory
         {'usr': 'oca', 'repo': 'product-attribute', 'branch': '8.0'},

     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo',
          'ver': '8.0.tienda_nube'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },

    #######################################################################1
    {'name': 'maketest', 'port': '8000', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-product', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'cursos', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'knowledge', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'bank-statement-import', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoomrp-wip', 'branch': '8.0'},
         # lo sacaron de la oca lo necesito por el recalculate_prices
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'social', 'branch': '8.0'},
         # lo pide por un modulo lote lock o algo parecido al instalar base vacia
         {'usr': 'oca', 'repo': 'stock-logistics-warehouse', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'stock-logistics-workflow', 'branch': '8.0'},
         {'usr': 'ingadhoc', 'repo': 'website', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'pos', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'SerpentCS_Contributions',
          'branch': '8.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################1
    {'name': 'makeover', 'port': '8068', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-product', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'cursos', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'knowledge', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'bank-statement-import', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoomrp-wip', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '8.0'},
         # lo sacaron de la oca lo necesito por el recalculate_prices
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'social', 'branch': '8.0'},
         # lo pide por un modulo lote lock o algo parecido al instalar base vacia
         {'usr': 'oca', 'repo': 'stock-logistics-warehouse', 'branch': '8.0'},
         {'usr': 'oca', 'repo': 'stock-logistics-workflow', 'branch': '8.0'},
         {'usr': 'ingadhoc', 'repo': 'website', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'pos', 'branch': '8.0'},

     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'sams', 'port': '8069', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-crm', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-product', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-partner', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'crm', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'customer', 'branch': '8.0'},

     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'nixel', 'port': '8090', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'tablero_nixel', 'instdir': 'nixel',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'valente', 'port': '8091', 'odoover': '8.0',
     'repos': [
         #         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoomrp-wip', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'valente', 'branch': '8.0'},

     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},

     ],
     },
    #######################################################################
    {'name': 'tds', 'port': '8071', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-stock', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'jeo', 'branch': '8.0'},
         #         {'usr': 'jobiols', 'repo': 'odoomrp-wip', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'web', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'contract', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'stock-logistics-warehouse',
          'branch': '8.0'},

     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },

    #######################################################################
    #
    # ODOO V9
    #
    #######################################################################
    {'name': 'mario', 'port': '8069', 'odoover': '9.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'mario', 'branch': '9.0'},
         {'usr': 'ingadhoc', 'repo': 'odoo-support', 'branch': '9.0'},

         # requeridos por la localizacion argentina -- 19/12/17
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-miscellaneous', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-argentina-reporting',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'partner-contact', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '9.0'},
         {'usr': 'oca', 'repo': 'reporting-engine', 'branch': '9.0'},
         {'usr': 'ingadhoc', 'repo': 'argentina-sale', 'branch': '9.0'},
         {'usr': 'ingadhoc', 'repo': 'stock', 'branch': '9.0'},

         {'usr': 'jobiols', 'repo': 'web', 'branch': '9.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '9.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
     ]
     },

    {'name': 'glinsar', 'port': '8069', 'odoover': '9.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'cl-glinsar', 'branch': '9.0',
          'host': 'bitbucket'},
         {'usr': 'ingadhoc', 'repo': 'odoo-support', 'branch': '9.0'},

         # requeridos por la localizacion argentina -- 19/12/17
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-miscellaneous', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-argentina-reporting',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'partner-contact', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '9.0'},
         {'usr': 'oca', 'repo': 'reporting-engine', 'branch': '9.0'},
         {'usr': 'ingadhoc', 'repo': 'argentina-sale', 'branch': '9.0'},
         {'usr': 'ingadhoc', 'repo': 'stock', 'branch': '9.0'},

         {'usr': 'jobiols', 'repo': 'web', 'branch': '9.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '9.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
     ]
     },

    {'name': 'sams9', 'port': '8069', 'odoover': '9.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'cl-sams', 'branch': '9.0',
          'host': 'bitbucket'},
         {'usr': 'ingadhoc', 'repo': 'odoo-support', 'branch': '9.0'},

         # requeridos por la localizacion argentina -- 19/12/17
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-miscellaneous', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-argentina-reporting',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'partner-contact', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '9.0'},
         {'usr': 'oca', 'repo': 'reporting-engine', 'branch': '9.0'},
         {'usr': 'ingadhoc', 'repo': 'argentina-sale', 'branch': '9.0'},
         {'usr': 'ingadhoc', 'repo': 'stock', 'branch': '9.0'},

         {'usr': 'jobiols', 'repo': 'web', 'branch': '9.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '9.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         #         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },

    #######################################################################
    {'name': 'jeo9', 'port': '8010', 'odoover': '9.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'customer', 'branch': '9.0'},
         {'usr': 'ingadhoc', 'repo': 'odoo-support', 'branch': '9.0'},

         # requeridos por la localizacion argentina -- 19/12/17
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-miscellaneous', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-argentina-reporting',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-invoicing',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'partner-contact', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '9.0'},
         {'usr': 'oca', 'repo': 'reporting-engine', 'branch': '9.0'},
         {'usr': 'ingadhoc', 'repo': 'argentina-sale', 'branch': '9.0'},
         {'usr': 'ingadhoc', 'repo': 'stock', 'branch': '9.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '9.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     },
    #######################################################################
    {'name': 'ou', 'port': '8069', 'odoover': '9.0',
     'repos': [
         # requeridos por la localizacion argentina -- 19/12/17
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-financial-tools',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-miscellaneous', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-account-payment', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-aeroo_reports', 'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-argentina-reporting',
          'branch': '9.0'},
         {'usr': 'jobiols', 'repo': 'adhoc-reporting-engine', 'branch': '9.0'},
         # customizacion
         {'usr': 'jobiols', 'repo': 'customer', 'branch': '9.0'},
         # oca tools
         {'usr': 'oca', 'repo': 'server-tools', 'branch': '9.0'},
         {'usr': 'oca', 'repo': 'partner-contact', 'branch': '9.0'},
         {'usr': 'oca', 'repo': 'reporting-engine', 'branch': '9.0'},

         #         {'usr': 'jobiols', 'repo': 'temp_modules', 'branch': '9.0'},
         #         {'usr': 'jobiols', 'repo': 'cursos', 'branch': '9.0'},
         #         {'usr': 'oca', 'repo': 'knowledge', 'branch': '9.0'},
     ],

     'images': [
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'docker-openupgrade',
          'ver': '9.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
     ]
     },
    #######################################################################
    #
    # ODOO V10
    #
    #######################################################################
    {'name': 'varazdin', 'port': '8069', 'odoover': '10.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'varazdin', 'branch': '10.0'},
         {'usr': 'jobiols', 'repo': 'SerpentCS_Contributions',
          'branch': '10.0'},
     ],
     'images': [
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '10.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
     ]
     },
    #######################################################################

    {'name': 'testarg', 'port': '8069', 'odoover': '10.0',
     'repos': [
         {'usr': 'odoo-arg', 'repo': 'odoo_l10n_ar', 'branch': 'master'},
     ],
     'images': [
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo',
          'ver': '10.0.arg'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
     ]
     },

    #######################################################################
    #
    # ODOO V10 Enterprise
    #
    #######################################################################
    {'name': 'agt', 'port': '8069', 'odoover': '10.0+e',
     'repos': [
         {'usr': 'jobiols', 'repo': 'SerpentCS_Contributions', 'branch': '10.0'},
         {'usr': 'vauxoo', 'repo': 'agt', 'branch': '10.0', 'host': 'git.vauxoo.com'},
         {'usr': 'Vauxoo', 'repo': 'enterprise', 'branch': '10.0'},
         #{'usr': 'Vauxoo', 'repo': 'mexico', 'branch': '10.0'},
         {'usr': 'Vauxoo', 'repo': 'server-tools', 'branch': '10.0'},
         {'usr': 'Vauxoo', 'repo': 'addons-vauxoo', 'branch': '10.0'}
     ],
     'images': [
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-e', 'ver': '10.0e-20170616'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.6'},
     ]
     },
]

# {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-jeo', 'ver': '10.0.v'},
