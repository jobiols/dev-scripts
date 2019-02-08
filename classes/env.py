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
import logging
import sys

logger = logging.getLogger(__name__)
logger.info('this does not work :(')

RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
YELLOW_LIGHT = "\033[33m"
CLEAR = "\033[0;m"


class Environment:
    def __init__(self, args=None, clients=[]):
        self._clients = []
        for cli in clients:
            self._clients.append(Client(self, cli))

        self._home_dir = '/odoo/'
        self._home_template = self._home_dir + 'odoo-'
        self._psql = self._home_dir + 'postgresql_9.6/'
        self._args = args

    def get_base_dir(self):
        return self._home_dir

    def get_tag(self):
        if self._args.checkout_tag:
            return self._args.checkout_tag[0]
        else:
            return False

    def server_mode(self):
        if self._args.server_mode:
            return self._args.server_mode[0]
        else:
            return False

    def debug_mode(self):
        return self._args.debug

    def run_tests(self):
        return self._args.run_tests

    def no_dbfilter(self):
        return self._args.no_dbfilter

    def no_repos(self):
        return self._args.no_repos

    def get_modules_from_params(self):
        if self._args.module is None:
            self.msgerr('need -m option (module name or all for all modules)')
        return self._args.module

    def get_qt_args_from_params(self):
        if self._args.database is None:
            self.msgerr('need -d option')
        if len(self._args.database) > 1:
            self.msgerr('only one database expected')
        if self._args.client is None:
            self.msgerr('need -c option (client name)')
        if self._args.module is None:
            self.msgerr('need -m option (module name)')
        return self._args.quality_test

    def get_database_from_params(self):
        if self._args.database is None:
            self.msgerr('need -d option (database name)')
        if len(self._args.database) > 1:
            self.msgerr('only one database expected')
        return self._args.database[0]

    def get_new_database_from_params(self):
        if self._args.new_database is None:
            self.msgerr('need -w option (new database name)')
        if len(self._args.new_database) > 1:
            self.msgerr('only one new database name expected')
        return self._args.new_database[0]

    def get_timestamp_from_params(self):
        if self._args.timestamp is None:
            self.msgerr(
                    'need -t option (timestamp, see --backup-list for available timestamps)')
        if len(self._args.database) > 1:
            self.msgerr('only one timestamp expected')
        return self._args.timestamp[0]

    def get_clients_from_params(self, cant='multi'):
        if self._args.client is None:
            self.msgerr('need -c option (client name)')

        for cli in self._args.client:
            if self.get_client(cli) is None:
                self.msgerr('there is no ' + cli + ' client in this environment')

        if cant == 'multi':
            return self._args.client
        else:
            if len(self._args.client) > 1:
                self.msgerr('only one client expected')
            return self._args.client[0]

    def get_args(self):
        return self._args

    def get_client(self, clientName):
        cli = None
        for client in self._clients:
            if client.get_name() == clientName:
                cli = client
        return cli

    def get_clients_form_dict(self):
        return self._clients

    def get_template_dir(self):
        return self._home_template

    def get_psql_dir(self):
        return self._psql

    def green(self, string):
        return GREEN + string + CLEAR

    def yellow(self, string):
        return YELLOW + string + CLEAR

    def red(self, string):
        return RED + string + CLEAR

    def yellow_light(self, string):
        return YELLOW_LIGHT + string + CLEAR

    def msgrun(self, msg):
        print self.yellow(msg)

    def msgdone(self, msg):
        print self.green(msg)

    def msgerr(self, msg):
        print self.red(msg)
        sys.exit()

    def msginf(self, msg):
        print self.yellow_light(msg)

    def msgwarn(self, msg):
        print self.red(msg)


class Client:
    def __init__(self, env, dic):
        self._env = env

        self._name = dic['name']

        self._port = dic['port']

        self._ver = dic['odoover']

        self._repos = []
        unique_repos = []
        for rep in dic['repos']:
            if rep not in unique_repos:
                unique_repos.append(rep)
        for rep in unique_repos:
            self._repos.append(Repo(self, rep))

        self._images = []
        unique_images = []
        for img in dic['images']:
            if img not in unique_images:
                unique_images.append(img)
        for img in unique_images:
            self._images.append(Image(self, img))

    def get_base_dir(self):
        return self._env.get_base_dir()

    def get_ver(self):
        return self._ver

    def get_numeric_ver(self):
        return float(self._ver[0:2])

    def get_backup_dir(self):
        return self.get_home_dir() + self._name + '/backup/'

    def get_log_backup_file(self):
        return '/var/log/odoo/odoo.log'

    def get_repos(self):
        return self._repos

    def get_images(self):
        return self._images

    def get_image(self, image_name):
        ret = None
        for img in self._images:
            if img.get_name() == image_name:
                ret = img
        if ret is None:
            self._env.msgerr('There is no {} image found in this manifest'.format(image_name))
        return ret

    def get_name(self, pad=0):
        return self._name.ljust(pad)

    def get_port(self):
        return self._port

    def get_home_dir(self):
        return self._env.get_template_dir() + self._ver + '/'

    def get_addons_path(self):
        """ path to addons inside image, arma el addons para poner en el config de odoo """
        path = '/mnt/extra-addons/'
        paths = []
        for repo in self.get_repos():
            paths.append(path + repo.get_addons_dir())
        return ','.join(paths)


class Repo:
    def __init__(self, cli, dict):
        self._dict = dict
        self._cli = cli

    def get_name(self):
        return self._dict['repo']

    def _get_repo(self):
        return self._dict['usr'] + '/' + self._dict['repo']

    def get_formatted_repo(self):
        ret = 'b ' + self._dict['branch'].ljust(7) + ' ' + self._get_repo().ljust(30)
        return ret

    def get_path_dir(self):
        """
            Devuelve el directorio path al repo relativo al /sources/ es donde está el .git
        """
        if 'instdir' in self._dict:
            ret = self._dict['instdir'] + '/' + self._dict['repo']
            return ret

        if 'innerdir' in self._dict:
            ret = self._dict['repo']
            return ret

        ret = self._dict['repo']
        return ret

    def get_addons_dir(self):
        """
            Devuelve el directorio al relativo repositorio, es lo que va en config,
            generalmente es igual al get_path_dir salvo que el repo no sea standard
            :return:
        """
        if 'instdir' in self._dict:
            ret = self._dict['instdir']
            return ret

        if 'innerdir' in self._dict:
            ret = self._dict['repo'] +'/'+ self._dict['innerdir']
            return ret

        ret = self._dict['repo']
        return ret

    def get_inst_dir(self):
        """
            Devuelve el directorio de instalación del repo, (donde esta el .git)
        """
        ret = '{}sources/{}'.format(
                self._cli.get_home_dir(),
                self.get_path_dir())
        return ret

    def do_pull_repo(self):
        """
            Comando para hacer pull a un repo ya existente
        """
        return 'git -C {} pull'.format(self.get_inst_dir())

    def do_clone_repo(self, e):
        """
            Devuelve un comando que clona el repo localmente,
            soporta github y bitbucket

            :param e: Environment
        """

        # si estoy en debug o haciendo checkout tag, bajar el historial completo
        depth = '' if e.debug_mode() or e.get_tag else ' --depth 1 '

        if self._dict.get('host', 'github') == 'bitbucket':
            srv = '{}@bitbucket.org'.format(self._dict.get('usr'))
        else:
            srv = 'github.com'

        return 'git clone {} -b {} http://{}/{} {}'.format(
                depth,
                self._dict['branch'],
                srv,
                self._get_repo(),
                self.get_inst_dir())

    def do_checkout(self, branch):
        """
            Hace checkout de un branch

            :param branch:
            :return: devuelve el comando
        """
        return 'git -C {} checkout {}'.format(
                self.get_inst_dir(),
                branch
        )

    def do_checkout_tag(self, tag):
        """
            Hace checkout del tag

            :param tag:
            :return: devuelve el comando
        """
        return 'git -C {} checkout tags/{}'.format(
                self.get_inst_dir(),
                tag)

    def do_tag_repo(self, tag):
        """
            tags the origin repo with two commands
            tag the repo
            push the tag to origin

            :param tag:
        """
        return [
            'git -C {} tag {}'.format(
                    self.get_inst_dir(),
                    tag),
            'git -C {} push origin {}'.format(
                    self.get_inst_dir(),
                    tag),
        ]


class Image:
    def __init__(self, cli, dict):
        self._cli = cli
        self._dict = dict

    def get_ver(self):
        try:
            ver = self._dict['ver']
        except:
            ver = 'latest'
        return ver

    def get_formatted_image(self):
        ret = self._dict['usr']
        try:
            ret += '/' + self._dict['img']
        except:
            a = 1

        try:
            ret += ':' + self._dict['ver']
        except:
            a = 1

        return ret

    def get_image(self):
        try:
            usr = self._dict['usr']
        except:
            usr = ''

        try:
            image = self._dict['img']
        except:
            image = ''

        try:
            ver = self._dict['ver']
        except:
            ver = ''

        ret = usr
        if image != '':
            ret += '/' + image
        if ver != '':
            ret += ':' + ver

        return ret

    def get_name(self):
        return self._dict['name']

    def get_pull_image(self):
        return 'sudo docker pull {}'.format(self.get_image())
