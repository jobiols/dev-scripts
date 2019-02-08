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
# https://api.github.com/repos/jobiols/valente/issues?state=all
#import requests
import textwrap

GITHUB_USER = 'jobiols'
GITHUB_PASSWORD = ''
AUTH = (GITHUB_USER, GITHUB_PASSWORD)

class Issue():
    """ Representa un issue, tiene una prioridad que eststá en el titulo entre []
        devuelve lo que hay que imprimir en una lista de strings
    """

    def __init__(self, data):
        self._number = data['number']
        self._body = data['body']
        self.milestone = ''
        if data['milestone']:
            self.milestone = data['milestone']['title'] or False
        self._title = data['title']
        a = self._title
        if '[' in a and ']' in a:
            self.prio = a[a.find('[') + 1: a.find(']')]
        else:
            self.prio = '9999'
        # definir el orden de prioridades
        self.order = u'{0:a>10}{1:0>4}'.format(self.milestone, self.prio)

    def lines(self):
        """ Genera las lineas a imprimir para describir el issue
        """
        ret = []
        ret.append(u'{2} #{0:04} {1}'.format(
            self._number,
            self._title,
            self.milestone
        )
        )
        if self._body:
            wtext = textwrap.wrap(self._body, replace_whitespace=False)
            for wtext_line in wtext:
                for final_line in wtext_line.split('\n'):
                    ret.append(u'    {}'.format(final_line))
        ret.append('')
        return ret


class Issues():
    """
    Get Issues from a specified repository

    Uses basic authentication (Github username + password) to retrieve Issues
    from a repository that username has access to. Supports Github API v3.
    if password is left blank can retrieve issues from public repos.
    """

    def __init__(self, repo):
        self._repo = '{}/{}'.format(GITHUB_USER, repo)
        #        self._state = 'closed'
        self._state = 'open'

    #        self._state = 'all'

    def _get_requests(self, url):
        """ dada una url devuelve un request a github, si GITHUB_PASSWORD está en blanco
            lo saca de un repo publico sino lo podria sacar de uno privado, NO ESTA TESTEADO
        """
        if GITHUB_PASSWORD:
            req = requests.get(url, auth=AUTH)
        else:
            req = requests.get(url)
        # el status code deber ser 200 sino es un error
        if not req.status_code == 200:
            if 'message' in req.json():
                msg = req.json()['message']
            else:
                msg = ''
            raise Exception(req.status_code, msg)
        return req

    def _get_issues_from_req(self, req, ret):
        """ Extrae los issues del request
        """
        for issue in req.json():
            ret.append(Issue(issue))
        return ret

    def _get_pages(self, req, url):
        return dict(
            [(rel[6:-1], url[url.index('<') + 1:-1]) for url, rel in
             [link.split(';') for link in
              req.headers['link'].split(',')]])

    def get_issues(self):
        ret = []
        url = u'https://api.github.com/repos/{}/issues?state={}'.format(self._repo,
                                                                        self._state)
        req = self._get_requests(url)
        ret = self._get_issues_from_req(req, ret)
        if 'link' in req.headers:
            pages = self._get_pages(req, url)
            while 'last' in pages and 'next' in pages:
                req = self._get_requests(pages['next'])
                ret = self._get_issues_from_req(req, ret)
                pages = self._get_pages(req, url)

                if pages.get('next') == pages.get('last'):
                    break

        ret.sort(key=lambda x: x.order)
        return ret

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
