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
from unittest import TestCase
from env import Client
from env import Environment

__author__ = 'jorge'

clients__ = [
    #######################################################################
    {'name': 'makeover', 'port': '8068', 'odoover': '8.0',
     'repos': [
         {'usr': 'jobiols', 'repo': 'odoo-argentina', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'odoo-addons', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'aeroo_reports', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'str', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'knowledge', 'branch': '8.0'},
         {'usr': 'jobiols', 'repo': 'server-tools', 'branch': '8.0'},
     ],
     'images': [
         {'name': 'aeroo', 'usr': 'jobiols', 'img': 'aeroo-docs'},
         {'name': 'odoo', 'usr': 'jobiols', 'img': 'odoo-adhoc', 'ver': '8.0'},
         {'name': 'postgres', 'usr': 'postgres', 'ver': '9.4'},
         {'name': 'backup', 'usr': 'jobiols', 'img': 'backup'},
     ]
     }
]


class TestClient(TestCase):
    def get_cli(self):
        args = None
        env = Environment(args, clients__)
        cli = env.get_client('makeover')
        return cli

    def test_get_ver(self):
        cli = self.get_cli()
        self.assertEqual(cli.get_ver(), '8.0')

    def test_get_backup_dir(self):
        cli = self.get_cli()
        self.assertEqual(cli.get_backup_dir(), '/home/jorge/odoo-8.0/makeover/backup/')

    def test_get_repos(self):
        cli = self.get_cli()
        self.assertEqual(cli.get_repos(), '')

    def test_get_images(self):
        self.fail()

    def test_get_image(self):
        self.fail()

    def test_get_name(self):
        self.fail()

    def test_get_port(self):
        self.fail()

    def test_get_home_dir(self):
        self.fail()

    def test_get_addons_path(self):
        self.fail()
