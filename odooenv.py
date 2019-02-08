#!/usr/bin/env python2.7
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
# Directory structure
#
#   ├──odoo
#      ├─ nginx
#      ├─ postgresql
#      ├──odoov-8.0
#      │  ├──[clientname]
#      │  │   ├──config
#      │  │   │  └──openerp-server.conf
#      │  │   ├──data_dir
#      │  │   │  └──[filestore]
#      │  │   └──log
#      │  │      └──odoo.log
#      │  └──sources
#      └──odoov-9.0
#         ├──[clientname]
#         │   ├──config
#         │   │  └──openerp-server.conf
#         │   ├──data_dir
#         │   │  └──[filestore]
#         │   └──log
#         │      └──odoo.log
#         └──sources
#
##############################################################################

import argparse
import logging
import logging.handlers
import os
import pwd
import subprocess
import time
from datetime import datetime

from classes import Environment
from classes.client_data import _clients
from classes.git_issues import Issues

# el archivo a ejecutar después de hacer backup
POST_BACKUP_ACTION = 'upload-backup'


def sc_(params, shell=False):
    """ Run command or command list with arguments.  Wait for commands to complete
        If args.verbose is true, prints command
        If any errors stop list execution and returns error
        if shell=True go shell mode (only for --cron-jobs)

    :param params: command or command list
    :return: error return
    """
    # if not a list convert to a one element list
    if not isinstance(params, list):
        params = [params]

    # traverse list executing commands
    for _cmd in params:
        # si shell = True no hacemos el split
        cmd = _cmd if shell else _cmd.split()
        if args.verbose:
            Environment().msgrun(' ')
            if shell:
                Environment().msgrun(cmd)
            else:
                Environment().msgrun(' '.join(cmd))
            Environment().msgrun(' ')
        ret = subprocess.call(cmd, shell=shell)
        if ret:
            return ret

    return 0


def update_db(e):
    mods = e.get_modules_from_params()
    db = e.get_database_from_params()
    cli = e.get_client(e.get_clients_from_params('one'))

    msg = 'Performing update'
    if mods[0] == 'all':
        msg += ' of all modules'
    else:
        msg += ' of module(s) ' + ', '.join(mods)

    msg += ' on database "{}"'.format(db)

    if e.debug_mode():
        msg += ' forcing debug mode'
    e.msgrun(msg)

    params = 'sudo docker run --rm -it '
    params += '-v {}{}/config:/etc/odoo '.format(cli.get_home_dir(), cli.get_name())
    params += '-v {}{}/data_dir:/var/lib/odoo '.format(cli.get_home_dir(), cli.get_name())
    params += '-v {}sources:/mnt/extra-addons '.format(cli.get_home_dir())
    if e.debug_mode():
        params += '-v {}sources/openerp:/usr/lib/python2.7/dist-packages/openerp '.format(
                cli.get_home_dir())
    params += '--link postgres:db '
    params += '{} -- '.format(cli.get_image('odoo').get_image())
    params += '--stop-after-init '
    params += '--logfile=false '
    params += '-d {} '.format(db)
    params += '-u {} '.format(', '.join(mods))

    # TODO revisar porque si le pongo log-level=warn a la v9 no funciona
    if cli.get_ver() == '8.0':
        params += '--log-level=warn '

    if e.debug_mode():
        params += '--debug '
    sc_(params)


def update_images_from_list(e, images):
    # avoid image duplicates
    tst_list = []
    unique_images = []
    for img in images:
        if img.get_formatted_image() not in tst_list:
            tst_list.append(img.get_formatted_image())
            unique_images.append(img)

    for img in unique_images:
        params = img.get_pull_image()
        e.msginf('pulling image ' + img.get_formatted_image())
        if sc_(params):
            e.msgerr('Fail pulling image ' + img.get_name() + ' - Aborting.')


def update_repos_from_list(e, repos):
    # do nothing if no_repos option is true
    if not e.no_repos():
        # check if /odoo exists
        if not os.path.isdir(e.get_base_dir()):
            sc_('sudo mkdir {}'.format(e.get_base_dir()))
            username = pwd.getpwuid(os.getuid()).pw_name
            # change ownership to current user
            sc_('sudo chown ' + username + ':' + username + ' ' + e.get_base_dir())

        for repo in repos:
            # if get_tag, delete the repo to force clone.
            if e.get_tag():
                params = 'sudo rm -r {}'.format(repo.get_inst_dir())
                if sc_(params):
                    e.msgerr('Fail deleting repo '+repo.get_name())

            # Check if repo exists
            if os.path.isdir(repo.get_inst_dir()):
                e.msginf('pull  ' + repo.get_formatted_repo())
                params = repo.do_pull_repo()
            else:
                e.msginf('clone ' + repo.get_formatted_repo())
                params = repo.do_clone_repo(e)

            if sc_(params):
                e.msgerr('Fail installing environment, uninstall and try again.')

#            # if get_tag is true checkout this repo to a known tag
#            if e.get_tag():
#                if sc_(repo.do_checkout_tag(e.get_tag())):
#                    e.msginf('Checkout, the repo does not have this tag')


def install_client(e):
    # get clients to install from params
    clients = e.get_clients_from_params()
    if len(clients) > 1:
        plural = 's'
    else:
        plural = ''
    e.msgrun('Install client' + plural + ' ' + ', '.join(clients))

    for client_name in clients:

        cli = e.get_client(client_name)

        # Creating directory's for installation if does not exist
        if not os.path.isdir(cli.get_base_dir()):
            sc_('sudo mkdir {}'.format(cli.get_base_dir()))
            username = pwd.getpwuid(os.getuid()).pw_name
            # change ownership to current user
            sc_('sudo chown {}:{} {}'.format(username, username, cli.get_base_dir()))

        # Creating client's directories
        if not os.path.isdir('{}{}/config'.format(cli.get_home_dir(),cli.get_name())):
            sc_('sudo mkdir -p {}{}/config'.format(cli.get_home_dir(), cli.get_name()))
            sc_('sudo chmod o+w {}{}/config'.format(cli.get_home_dir(), cli.get_name()))
            sc_('sudo mkdir -p {}{}/data_dir'.format(cli.get_home_dir(), cli.get_name()))
            sc_('sudo chmod o+w {}{}/data_dir'.format(cli.get_home_dir(), cli.get_name()))
            sc_('sudo mkdir -p {}{}/log'.format(cli.get_home_dir(), cli.get_name()))
            sc_('sudo chmod o+w {}{}/log'.format(cli.get_home_dir(), cli.get_name()))

        # Creating sources directory
        if not os.path.isdir('{}sources'.format(cli.get_home_dir())):
            sc_('sudo mkdir -p {}sources'.format(cli.get_home_dir()))
            sc_('sudo chmod o+w {}sources'.format(cli.get_home_dir()))

        # Creating postgresql directory
        if not os.path.isdir(e.get_psql_dir()):
            sc_('mkdir {}'.format(e.get_psql_dir()))

        # Creating log directory
        if not os.path.isfile(LOG_FILENAME):
            sc_('sudo mkdir -p {}'.format(os.path.dirname(LOG_FILENAME)))
            sc_('sudo touch {}'.format(LOG_FILENAME))
            sc_('sudo chmod 666 {}'.format(LOG_FILENAME))

        # clone or update repos as needed
        update_repos_from_list(e, cli.get_repos())

        # creating config file for client
        param = 'sudo docker run --rm '
        param += '-v {}{}/config:/etc/odoo '.format(cli.get_home_dir(), cli.get_name())
        param += '-v {}sources:/mnt/extra-addons '.format(cli.get_home_dir())
        param += '-v {}{}/data_dir:/var/lib/odoo '.format(cli.get_home_dir(), cli.get_name())
        param += '-v {}{}/log:/var/log/odoo '.format(cli.get_home_dir(), cli.get_name())
        param += '--name {}_tmp '.format(cli.get_name())
        param += '{} '.format(cli.get_image('odoo').get_image())
        param += '-- --stop-after-init -s '
        if not e.no_dbfilter():
            param += '--db-filter={}_.* '.format(cli.get_name())

        # patch for openupgrade image
        ou = '/opt/openerp/addons,' if client_name == 'ou' else ''

        if cli.get_addons_path():
            param += '--addons-path={}{} '.format(ou, cli.get_addons_path())
        param += '--logfile=/var/log/odoo/odoo.log '
        param += '--logrotate '

        e.msginf('creating config file')
        if sc_(param):
            e.msgerr('failing to write config file. Aborting')


        # TODO no puedo escribir en este archivo. Revisarlo
        # adding server_mode to config file
        if e.server_mode():
            config_name = 'openerp-server.conf' if cli.get_numeric_ver() < 10 else 'odoo.conf'
            config_file = '{}{}/config/{}'.format(cli.get_home_dir(), cli.get_name(), config_name)

            param = "echo '{}' >{}".format('server_mode = {}'.format(e.server_mode()), config_file)
            print '>>>>>', param
            if sc_(param):
                e.msgerr('failing to append server mode')

    e.msgdone('Installing done')


def run_environment(e):
    e.msgrun('Running environment images')
    client_name = e.get_clients_from_params(cant='one')

    cli = e.get_client(client_name)

    err = 0
    image = cli.get_image('postgres')
    params = 'sudo docker run -d '
    if e.debug_mode():
        params += '-p 5432:5432 '
    params += '-e POSTGRES_USER=odoo '
    params += '-e POSTGRES_PASSWORD=odoo '
    params += '-v {}:/var/lib/postgresql/data '.format(e.get_psql_dir())
    params += '--restart=always '
    params += '--name {} '.format(image.get_name())
    params += image.get_image()
    err += sc_(params)

    if cli.get_numeric_ver() < 10:
        image = cli.get_image('aeroo')
        params = 'sudo docker run -d '
        params += '-p 127.0.0.1:8989:8989 '
        params += '--name={} '.format(image.get_name())
        params += '--restart=always '
        params += image.get_image()
        err += sc_(params)

    if err:
        e.msgerr('Fail running some images.')

    e.msgdone('images running')
    return True


def server_help(e):
    client = e.get_clients_from_params('one')
    cli = e.get_client(client)

    params = 'sudo docker run --rm -it '
    params += cli.get_image('odoo').get_image() + ' '
    params += '-- '
    params += '--help '

    if sc_(params):
        e.msgerr("Can't run help")


def quality_test(e):
    """
    Corre un test especifico, los parametros necesarios son:
    -Q repositorio test_file.py -d database -c cliente -m modulo
    """
    cli = e.get_client(e.get_clients_from_params('one'))
    repo_name, test_file = e.get_qt_args_from_params()
    module_name = e.get_modules_from_params()[0]
    db = e.get_database_from_params()

    # chequear si el repo está dentro de los repos del cliente
    repos_lst = []
    for repo in cli.get_repos():
        repos_lst.append(repo.get_name())
    if repo_name not in repos_lst:
        e.msgerr('Client "{}" does not own "{}" repo'.format(cli.get_name(), repo_name))

    msg = 'Performing test {} on repo {} for client {} and database {}'.format(
            test_file, repo_name, cli.get_name(), db)
    e.msgrun(msg)

    params = 'sudo docker run --rm -it '
    params += '-v {}{}/config:/etc/odoo '.format(cli.get_home_dir(), cli.get_name())
    params += '-v {}{}/data_dir:/var/lib/odoo '.format(cli.get_home_dir(), cli.get_name())
    params += '-v {}sources:/mnt/extra-addons '.format(cli.get_home_dir())
    if e.debug_mode():
        # a partir de la version 10 cambia a odoo el nombre de los fuentes
        sources_image = 'odoo' if cli.get_ver().split('.')[0] >= '10' else 'openerp'
        sources_host = sources_image

        # si es openupgrade el sources_image es upgrade
        if cli == 'ou':
            sources_image = 'upgrade'

        params += '-v {}sources/dist-packages:/usr/lib/python2.7/dist-packages '.format(
                cli.get_home_dir(), sources_image, sources_host)
    params += '--link postgres:db '
    params += '{} -- '.format(cli.get_image('odoo').get_image())
    params += '--stop-after-init '
    params += '--logfile=false '
    params += '-d {} '.format(db)
    params += '--log-level=test '
    params += '--test-file=/mnt/extra-addons/{}/{}/tests/{} '.format(
            repo_name, module_name, test_file)
    sc_(params)


def run_client(e):
    clients = e.get_clients_from_params()
    for clientName in clients:
        cli = e.get_client(clientName)

        txt = 'Running image for client {}'.format(clientName)
        if e.debug_mode():
            txt += ' with debug mode on port {}'.format(cli.get_port())

        e.msgrun(txt)
        if e.debug_mode():
            params = 'sudo docker run --rm -it '
        else:
            params = 'sudo docker run -d '

        # a partir de la 10 no se usa aeroo
        if cli.get_numeric_ver() < 10:
            params += '--link aeroo:aeroo '

        # open port for wdb
        if e.debug_mode():
            params += '-p 1984:1984 '
        params += '-p {}:8069 '.format(cli.get_port())
        params += '-v {}{}/config:/etc/odoo '.format(cli.get_home_dir(), cli.get_name())
        params += '-v {}{}/data_dir:/var/lib/odoo '.format(cli.get_home_dir(),
                                                           cli.get_name())
        params += '-v {}sources:/mnt/extra-addons '.format(cli.get_home_dir())
        if e.debug_mode():
            # a partir de la version 10 cambia a odoo el nombre de los fuentes
            sources_image = 'odoo' if cli.get_numeric_ver > 9 else 'openerp'
            sources_host = sources_image

            # si es openupgrade el sources_image es upgrade
            if clientName == 'ou':
                sources_image = 'upgrade'

            params += '-v {}sources/dist-packages:/usr/lib/python2.7/dist-packages '.format(
                    cli.get_home_dir(), sources_image, sources_host)

        params += '-v {}{}/log:/var/log/odoo '.format(cli.get_home_dir(), cli.get_name())
        params += '--link postgres:db '

        if not e.debug_mode():
            params += '--restart=always '

        params += '--name {} '.format(cli.get_name())

        # si estamos en modo debug agregarlo al nombre de la imagen
        if e.debug_mode():
            params += '{}.debug '.format(cli.get_image('odoo').get_image())
        else:
            params += '{} '.format(cli.get_image('odoo').get_image())

        if not e.no_dbfilter():
            params += '-- --db-filter={}_.* '.format(cli.get_name())

        if not e.debug_mode():
            params += '--logfile=/var/log/odoo/odoo.log '
        else:
            params += '--logfile=False '

        if e.get_args().translate:
            params += '--language=es --i18n-export=/etc/odoo/es.po --update ' \
                      '--i18n-overwrite --modules={} --stop-after-init ' \
                      '-d {}'.format(e.get_modules_from_params()[0],
                                     e.get_database_from_params())

        if sc_(params):
            e.msgerr("Can't run client {}, Tip: run sudo docker rm -f {}".format(
                    cli.get_name(), cli.get_name()))

        else:
            e.msgdone(
                    'Client ' + clientName + ' up and running on port ' + cli.get_port())

    return True


def stop_client(e):
    clients = e.get_clients_from_params()
    e.msgrun('stopping clients ' + ', '.join(clients))

    for clientName in clients:
        e.msginf('stopping image for client ' + clientName)
        if sc_('sudo docker stop ' + clientName):
            e.msgerr('cannot stop client ' + clientName)

        if sc_('sudo docker rm ' + clientName):
            e.msgerr('cannot remove client ' + clientName)

    e.msgdone('all clients stopped')

    return True


def stop_environment(e):
    images_to_stop = ['postgres', 'aeroo']
    e.msgrun('Stopping images ' + ', '.join(images_to_stop))
    for name in images_to_stop:
        e.msgrun('Stopping image ' + name)
        sc_('sudo docker stop ' + name)
        sc_('sudo docker rm ' + name)

    e.msgdone('Images stopped')
    return True


def pull_all(e):
    e.msgrun('--- Pulling all images')

    images = []
    for cli in e.get_clients_form_dict():
        if cli.get_name() in e.get_clients_from_params():
            images.extend(cli.get_images())
    update_images_from_list(e, images)

    e.msgdone('All images ok ')
    e.msgrun('--- Pulling all repos')

    repos = []
    for cli in e.get_clients_form_dict():
        if cli.get_name() in e.get_clients_from_params():
            repos.extend(cli.get_repos())
    update_repos_from_list(e, repos)

    e.msgdone('All repos ok ')


def list_data(e):
    # if --issues option get issues from github
    if args.repo:
        iss = Issues(args.repo[0])
        try:
            for issue in iss.get_issues():
                for line in issue.lines():
                    e.msginf(line)
        except Exception as EX:
            e.msgerr(str(EX))

        exit(0)

    # if no -c option get all clients else get -c clients
    if args.client is None:
        clients = e.get_clients_form_dict()
    else:
        clients = []
        for clientName in e.get_clients_from_params():
            clients.append(e.get_client(clientName))

    for cli in clients:
        e.msginf('client -- ' + cli.get_name(0) + ' -- on port ' + cli.get_port())

        e.msgrun(3 * '-' +
                 ' Images ' +
                 72 * '-')
        for image in cli.get_images():
            e.msgrun('   ' +
                     image.get_formatted_image())
        e.msgrun(' ')
        e.msgrun(3 * '-' + 'branch' +
                 4 * '-' + 'repository' +
                 25 * '-' + 'instalation dir' +
                 20 * '-')
        for repo in cli.get_repos():
            e.msgrun('   ' +
                     repo.get_formatted_repo() +
                     ' ' + repo.get_inst_dir())
        e.msgrun(' ')


def no_ip_install(e):
    e.msgrun('Installing no-ip client')
    # download and unpack noip client for linux
    cmdr = [
        'sudo apt-get update',
        'sudo apt-get install gcc wget make -y -qq',
        'sudo wget -O /usr/local/src/noip.tar.gz \
             http://www.noip.com/client/linux/noip-duc-linux.tar.gz',
        'sudo tar xf /usr/local/src/noip.tar.gz -C /usr/local/src/'
    ]
    sc_(cmdr)
    e.msginf("Please answer some questions")
    # compile, configure an install as a deamon
    # TODO parece que falla con el &&
    cmdr = [
        'cd /usr/local/src/noip-2.1.9-1 && sudo make install',
        'sudo rm /usr/local/src/noip.tar.gz',
        'sudo cp /usr/local/src/noip-2.1.9-1/debian.noip2.sh  /etc/init.d/',
        'sudo chmod +x /etc/init.d/debian.noip2.sh',
        'sudo update-rc.d debian.noip2.sh defaults',
        'sudo /etc/init.d/debian.noip2.sh restart'
    ]
    sc_(cmdr)
    e.msgdone('no-ip service running')

    e.msginf('To config defaults issue noip2 with capital C as follows:')
    e.msginf('sudo /usr/local/bin/noip2 -C')


def post_backup(e):
    client_name = e.get_clients_from_params('one')
    client = e.get_client(client_name)
    backup_dir = client.get_backup_dir()

    # verify what to do before backup, default is backup housekeeping
    limit_seconds = time.time() - 10 * 60 * 60 * 24

    # walk the backup dir
    for root, dirs, files in os.walk(backup_dir):
        for filename in files:
            seconds = os.path.getctime(root + filename)
            if seconds < limit_seconds:
                # no eliminar el archivo de postbackup
                if filename[-13:] != POST_BACKUP_ACTION:
                    sc_('sudo rm ' + root + filename)
                    # os.remove(root+file)
                    logger.info('Removed backup file "%s"', filename)

    # watch for upload-backup cmdfile and execute
    for root, dirs, files in os.walk(backup_dir):
        for filename in files:
            if filename[-13:] == POST_BACKUP_ACTION:
                sc_(backup_dir + filename)


def backup(e):
    dbname = e.get_database_from_params()
    client_name = e.get_clients_from_params('one')
    e.msgrun('Backing up database ' + dbname + ' of client ' + client_name)

    client = e.get_client(client_name)
    img = client.get_image('backup')

    params = 'sudo docker run --rm -i '
    params += '--link postgres:db '
    params += '--volumes-from {} '.format(client_name)
    params += '-v {}:/backup '.format(client.get_backup_dir())
    params += '--env DBNAME={} '.format(dbname)
    params += '{}  backup'.format(img.get_image())
    try:
        if sc_(params):
            e.msgerr('failing backup. Aborting')
    except Exception as EX:
        logger.error('Failing backup %s', str(EX))
        e.msgerr('failing backup. Aborting {}'.format(str(EX)))

    e.msgdone('Backup done')
    logger.info('Backup database "%s"', dbname)

    post_backup(e)


def restore(e):
    dbname = e.get_database_from_params()
    client_name = e.get_clients_from_params('one')
    timestamp = e.get_timestamp_from_params()
    new_dbname = e.get_new_database_from_params()
    if dbname == new_dbname:
        e.msgerr('new dbname should be different from old dbname')

    e.msgrun(
            'Restoring database ' + dbname + ' of client ' + client_name + ' onto database ' + new_dbname)

    client = e.get_client(client_name)
    img = client.get_image('backup')

    params = 'sudo docker run --rm -i '
    params += '--link postgres:db '
    params += '--volumes-from ' + client_name + ' '
    params += '-v ' + client.get_backup_dir() + ':/backup '
    params += '--env NEW_DBNAME=' + new_dbname + ' '
    params += '--env DBNAME=' + dbname + ' '
    params += '--env DATE=' + timestamp + ' '
    params += img.get_image() + ' restore'

    if sc_(params):
        e.msgerr('failing restore. Aborting')

    e.msgdone('Restore done')
    logger.info('Restore database %s', dbname)
    return True


def decode_backup(root, filename):
    """
    from root and filename generates human readable filename
    i.e.: jeo_datos_201511022236

    :param root: directory where backups reside
    :param filename: backup filename without extension
    :return: formatted filename
    """

    # size of bkp
    path = os.path.join(root, filename + '.dump')
    try:
        size = os.stat(path).st_size
    except:
        size = 0

    # plus size of tar
    path = os.path.join(root, filename + '.tar')
    try:
        size += os.stat(path).st_size
    except:
        size += 0

    size /= 1000000

    # strip db name
    a = len(filename) - 13
    dbname = filename[0:a]

    # strip date
    date = filename[-12:]
    dt = datetime.strptime(date, '%Y%m%d%H%M')

    # format date
    fdt = datetime.strftime(dt, '%d/%m/%Y %H:%M GMT')
    n = 15 - len(dbname)

    return dbname + n * ' ' + fdt + '  [' + date + '] ' + str(size) + 'M'


def backup_list(e):
    # if no -c option get all clients else get -c clients
    if args.client is None:
        clients = []
        for cli in e.get_clients_form_dict():
            clients.append(cli.get_name())
    else:
        clients = e.get_clients_from_params()

    for clientName in clients:
        cli = e.get_client(clientName)
        backup_dir = cli.get_backup_dir()

        filenames = []
        root = ''
        # walk the backup dir
        for root, dirs, files in os.walk(backup_dir):
            for filedesc in files:
                # get the .dump files and decode it to human readable format
                filename, file_extension = os.path.splitext(filedesc)
                if file_extension == '.dump':
                    filenames.append(filename)

        if len(filenames):
            filenames.sort()
            e.msgrun('List of available backups for client ' + clientName)
            for filedesc in filenames:
                e.msginf(decode_backup(root, filedesc))


def cron_jobs(e):
    """
        Agrega un job en el crontab de admin para hacer backup dos veces por dia.
            crontab -l lista el crontab
            grep -v {} filtra dejando pasar todo menos lo que hay en {}
            echo {} agrega {}
            sudo crontab - mete todo lo anterior en crontab
    """
    dbname = e.get_database_from_params()
    client = e.get_clients_from_params('one')
    e.msginf('Adding cron jobs to this server')

    # el comando que cron tiene que lanzar. Suponiendo que nadie lo edita, al lanzar nuevamente
    # este proceso se elimina y se vuelve a crear permitiendo modificar el cronjob.
    croncmd = 'odooenv.py --backup -d {} -c {} > /var/log/odoo/bkp.log #Added by odooenv.py DO NOT EDIT MANUALLY'.format(
            dbname, client)

    # la linea que agregaremos a cron sería en que momento backupear + el croncmd
    cronjob = '0 0,12 * * * {}'.format(croncmd)

    command = '(sudo crontab -l | grep -v "{}" ; echo "{}") | sudo crontab - '.format(croncmd, cronjob)
    sc_(command, shell=True)


def cron_list(e):
    e.msginf('List of cron backup jobs on this server')
    if sc_('sudo crontab -l | grep "#Added by odooenv.py"', shell=True):
        e.msgerr('No crontab jobs found!')


def tag_repos(e):
    """
    Pone un tag a todos los repos que tiene este cliente con timestamp+client_name

    :param e: Environment
    """
    client_name = e.get_clients_from_params(cant='one')
    ts = datetime.now()
    # build tag
    tag = '{}-{}'.format(ts.strftime('%Y-%m-%d-%H-%m-%S'), client_name)

    e.msginf('All this repos will be tagged')
    cli = e.get_client(client_name)
    for repo in cli.get_repos():
        e.msginf('tagging {} to [{}]'.format(tag, repo.get_formatted_repo()))

    ans = raw_input('proceed with tagging? (y/n)')
    if ans != 'y':
        e.msgerr('command aborted')

    for repo in cli.get_repos():
        e.msginf('tagging {} to [{}]'.format(tag, repo.get_formatted_repo()))
        if sc_(repo.do_tag_repo(tag)):
            e.msgerr('tag failed')

    e.msgdone('all repos tagged')


def checkout_tag(e):
    client_name = e.get_clients_from_params(cant='one')
    tag = e.get_args().checkout_tag[0]
    e.msginf('Checking out tag {} for all repos belonging to client {}'.format(
            tag,
            client_name
    ))

    cli = e.get_client(client_name)
    for repo in cli.get_repos():
        e.msginf('checking out >> {}'.format(repo.get_formatted_repo()))
        if sc_(repo.do_checkout_tag(tag)):
            e.msgwarn('there is no such tag in this repo!!')

    e.msgdone('All repos with this tag were checked out')


def issues(e):
    pass


def undo_checkout_tag(e):
    client_name = e.get_clients_from_params(cant='one')
    cli = e.get_client(client_name)

    e.msginf('Checking out branch {} for all repos belonging to client {}'.format(
            cli.get_ver(),
            client_name
    ))

    for repo in cli.get_repos():
        e.msginf('checking out >> {}'.format(repo.get_formatted_repo()))
        if sc_(repo.do_checkout(cli.get_ver())):
            e.msginf('there is no such version in this repo')

    e.msgdone('All repos with this version were checked out')


if __name__ == '__main__':
    LOG_FILENAME = '/var/log/odooenv/odooenv.log'
    try:
        # Set up a specific logger with our desired output level
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # Add the log message handler to the logger
        handler = logging.handlers.RotatingFileHandler(
                LOG_FILENAME, maxBytes=2000000, backupCount=5)

        # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
        handler.setFormatter(formatter)

        logger.addHandler(handler)
    except Exception as ex:
        logger = logging.getLogger(__name__)
        print 'Warning!, problems with logfile', str(ex)

    parser = argparse.ArgumentParser(description="""
        ==========================================================================
        Odoo environment setup v5.1.0 by jeo Software <jorge.obiols@gmail.com>
        With wdb support (https://github.com/Kozea/wdb)
        ==========================================================================
    """)
    parser.add_argument('-p', '--pull-all',
                        action='store_true',
                        help="Pull all images and repos for a client, need a -c "
                             "option")

    parser.add_argument('-i', '--install-cli',
                        action='store_true',
                        help="Install client, requires -c option. Pull repos and "
                             "generate odoo config file")

    parser.add_argument('-R', '--run-env',
                        action='store_true',
                        help="Run database and aeroo images.")

    parser.add_argument('-S', '--stop-env',
                        action='store_true',
                        help="Stop database and aeroo images.")

    parser.add_argument('-r', '--run-cli',
                        action='store_true',
                        help="Run client odoo images, requires -c options. Optional")

    parser.add_argument('-s', '--stop-cli',
                        action='store_true',
                        help="Stop client images, requires -c options.")

    parser.add_argument('-l', '--list',
                        action='store_true',
                        help="List all data in this server. Clients and images. with "
                             "--issues REPO list the github issues from repo")

    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help="Go verbose mode. Prints every command")

    parser.add_argument('-n', '--no-ip-install',
                        action='store_true',
                        help="Install no-ip on this server. Experimental")

    parser.add_argument('-u', '--update-db',
                        action='store_true',
                        help="Update database requires -d -c and -m options.")

    parser.add_argument('-d',
                        action='store',
                        nargs=1,
                        dest='database',
                        help="Database name.")

    parser.add_argument('-w',
                        action='store',
                        nargs=1,
                        dest='new_database',
                        help="New database name. Only for restore command")

    parser.add_argument('-m',
                        action='append',
                        dest='module',
                        help="Module to update or all for updating all the reegistered "
                             "modules, you can specify multiple -m options.")

    parser.add_argument('--server-mode',
                        action='append',
                        dest='server_mode',
                        help="Appends option server_mode = 'mode' to config file when installing with -i option ")

    parser.add_argument('-c',
                        action='append',
                        dest='client',
                        help="Client name.")

    parser.add_argument('--debug',
                        action='store_true',
                        help='This option has three efects: '
                             '1.- when doing an update database, (option -u) it forces debug mode. '
                             '2.- When running environment (option -R) it opens port 5432 to access '
                             'postgres server databases. '
                             '3.- when doing a pull (option -p) it clones the full repo i.e. does '
                             'not issue --depth 1 to git ')

    parser.add_argument('--no-dbfilter',
                        action='store_true',
                        help='Eliminates dbfilter: The client can see any database. '
                             'Without this, the client can only see databases starting with clientname_')

    parser.add_argument('--no-repos',
                        action='store_true',
                        help='Does not clone or pull repos used with -i or -p')

    parser.add_argument('-H', '--server-help',
                        action='store_true',
                        help="List server help requires -c option (because needs to run a image)")

    parser.add_argument('--backup',
                        action='store_true',
                        help="Lauch backup. requires -d and -c options.")

    parser.add_argument('--backup-list',
                        action='store_true',
                        help="List available backups with timestamps to restore.")

    parser.add_argument('--restore',
                        action='store_true',
                        help="Launch restore requires -c, -d, -w and -t options.")

    parser.add_argument('-t',
                        action='store',
                        nargs=1,
                        dest='timestamp',
                        help="Timestamp to restore database, see --backup-list for "
                             "available timestamps.")

    parser.add_argument('-Q', '--quality-test',
                        action='store',
                        metavar=('repo', 'test_file'),
                        nargs=2,
                        dest='quality_test',
                        help="Perform a test, arguments are Repo where test lives, "
                             "and yml/py test file to run (please include extension). "
                             "Need -d, -m and -c options "
                             "Note: for the test to run there must be an admin user "
                             "with password admin")

    parser.add_argument('-j', '--cron-jobs',
                        action='store_true',
                        help='Cron Backup. it adds cron jobs for doing backup to a '
                             'client database. backups twice a day at 12 AM and 12 PM. '
                             'Needs a -c option to tell which client to backup.')

    parser.add_argument('--cron-list',
                        action='store_true',
                        help="List available cron jobs")

    parser.add_argument('--translate',
                        action='store_true',
                        help="Generate a po file for a module to translate, need a -r "
                             "and -m option")

    parser.add_argument('--issues',
                        dest='repo',
                        nargs=1,
                        action='store',
                        help="list formatted and priorized issues from github, "
                             "used with -l this option supports github API v3 "
                             "priority is the number between brackets in issue title"
                             "THIS COMMAND IS DEPRECATED IN FAVOR OF GITHUB PROJECTS"
                        )

    parser.add_argument('-T' '--tag-repos',
                        dest='tag_repos',
                        action='store_true',
                        help="Tag all repos used by a client with a tag consisting of "
                             "client name and a timestamp. Need -c option"
                        )

    parser.add_argument('--checkout-tag',
                        action='store',
                        nargs=1,
                        help='checkouts a tag from all the repos belonging to a client '
                             'needs -c option. If some repo does not have the tag, reports the '
                             'error and continues with next repo.'
                             'The tag was previously setted with -T option. '
                             'To undo this situation issue a --undo-checkout-tag'
                        )

    parser.add_argument('--undo-checkout-tag',
                        action='store_true',
                        help='checkouts the normal branch (i.e. odoo version) for all the repos belonging '
                             'to the client. Needs -c option. '
                             'This revers the the repos modifyed for a --checkout-tag to its normal state. '
                             'Warning: if there is any local change in a repo, the checkout will fail.'
                        )

    args = parser.parse_args()
    environment = Environment(args, _clients)

    if args.install_cli:
        install_client(environment)
    if args.stop_env:
        stop_environment(environment)
    if args.run_env:
        run_environment(environment)
    if args.stop_cli:
        stop_client(environment)
    if args.run_cli:
        run_client(environment)
    if args.pull_all:
        pull_all(environment)
    if args.list:
        list_data(environment)
    if args.no_ip_install:
        no_ip_install(environment)
    if args.update_db:
        update_db(environment)
    if args.backup:
        backup(environment)
    if args.restore:
        restore(environment)
    if args.backup_list:
        backup_list(environment)
    if args.server_help:
        server_help(environment)
    if args.cron_jobs:
        cron_jobs(environment)
    if args.cron_list:
        cron_list(environment)
    if args.quality_test:
        quality_test(environment)
    if args.tag_repos:
        tag_repos(environment)
    if args.checkout_tag:
        checkout_tag(environment)
    if args.undo_checkout_tag:
        undo_checkout_tag(environment)
