# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

try:
    a = float('1eer0')
except ValueError:
    print 'aa'
    raise