# -*- coding: utf-8 -*-
# test for sd.py
#######################
import unittest

from sd import process_input


class SudoDockerTestCase(unittest.TestCase):
    def test_empty(self):
        """ Si no tiene parametros devuelve lista vacia
        """
        self.assertListEqual(
                process_input([]),
                [],
                'falla sin parametros'
        )

    def test_ps(self):
        """ Con un solo parámetro agrega sudo docker
        """
        self.assertListEqual(
                process_input(['./sd', 'ps']),
                ['sudo', 'docker', 'ps'],
                'falla con un solo parámetro'
        )

    def test_inside(self):
        """ pseudo sintaxis inside, agrega parametros para docker
        """
        self.assertListEqual(
                process_input(['./sd', 'inside', 'jobiols/backup']),
                ['sudo', 'docker', 'run', '-it', '--rm', '--entrypoint=/bin/bash', 'jobiols/backup'],
                'falla con inside'
        )

    def test_inside_bad(self):
        """  Generar un error al no poner la imagen en inside
        """
        self.assertListEqual(
                process_input(['./sd', 'inside']),
                [],
                'falle cuando no esta la imagen'
        )

if __name__ == '__main__':
    unittest.main()
