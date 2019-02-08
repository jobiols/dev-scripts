#!/usr/bin/env python
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
import subprocess
import sys, os

if __name__ == '__main__':
    repo = sys.argv[1]

    if repo[-1] == '/':
        print 'quitar la barra del directorio'
        exit()

    for root, dirs, files in os.walk(repo):
        if '.idea' in root or '.git' in root or 'dev-scripts' in root:
            continue
        for dir in dirs:
            if '.idea' in dir or '.git' in dir:
                continue
            print 'setting permission 755 {}/{}'.format(root, dir)
            params = 'sudo chmod 755 {}/{}'.format(root, dir)
            subprocess.call(params, shell=True)
        for file in files:
            if 'pyc' in file:
                continue
            print 'setting permission 644 {}/{}'.format(root, file)
            params = 'sudo chmod 644 {}/{}'.format(root, file)
            subprocess.call(params, shell=True)
