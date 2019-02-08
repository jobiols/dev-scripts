# -*- coding: utf-8 -*-
# For copyright and license notices, see __manifest__.py file in module root
import sys
from datetime import datetime
import subprocess
import json

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
YELLOW_LIGHT = "\033[33m"
CLEAR = "\033[0;m"
REPOS_DIR = '/home/jobiols/git-repos/FROZEN/'
NOW = datetime.now()


def sc__(params):
    if args.verbose:
        print '>', params
    p = subprocess.Popen(params.split(), stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    return p.communicate()


def sc_(params):
#    if args.verbose:
#        print '>', params
    return subprocess.call(params, shell=True)


def green(string):
    return GREEN + string + CLEAR


def yellow(string):
    return YELLOW + string + CLEAR


def red(string):
    return RED + string + CLEAR


def yellow_light(string):
    return YELLOW_LIGHT + string + CLEAR


def msgrun(msg):
    print yellow(msg)


def msgdone(msg):
    print green(msg)


def msgerr(msg):
    print red(msg)
    sys.exit()


def msginf(msg):
    print yellow_light(msg)


def get_repos_data():
    """ levantar datos de archivo de configuracion, tiene
        que estar en el mismo directorio que este archivo
    """
    with open('update-forks-data.json') as f:
        json_data = json.load(f)
    return json_data['repos']
