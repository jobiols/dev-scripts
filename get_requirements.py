#!/usr/bin/env python

from __future__ import print_function
import sys
import os
import argparse

import subprocess
from repos_lib import sc_, msgrun, msginf, msgerr, msgdone, NOW, get_repos_data, \
    REPOS_DIR


def version():
    version = args.version[0]

    msgrun('Getting requirements for ' + version)

    # obtener todos los directorios bajo REPOS_DIR
    repo_list = next(os.walk(REPOS_DIR))[1]

    # hacer checkout de todos los repos en la version correcta
    # los que no tienen el branch fallan y listo
    for repodir in repo_list:
        sc_('git -C {}{} checkout {}'.format(REPOS_DIR, repodir, version))

    list_of_files = []
    for (dirpath, dirnames, filenames) in os.walk(REPOS_DIR):
        for filename in filenames:
            if filename.find('quirem') > 0:
                list_of_files.append(dirpath +'/'+ filename)

    for file in list_of_files:
        print(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
    get_requirements v 0.0.1---------------------------------------------------
    Busca los requirements.txt en todos los repositorios definidos para usar
    y los lista para poder ponerlos en la imagen.
    """)
    parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        help="Show commands")

    parser.add_argument('-V',
                        '--version',
                        action='append',
                        dest='version',
                        help="Odoo Version")

    args = parser.parse_args()

    if args.version:
        version()

