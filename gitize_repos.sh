#!/bin/bash
cd /odoo_ar/odoo-9.0
sudo chmod -R +w dist-packages/ extra-addons/
echo .idea/\n*.pyc >> dist-packages/openerp/.gitignore
echo .idea/\n*.pyc >> extra-addons/.gitignore
git -C dist-packages/openerp/ init
git -C dist-packages/openerp/ add .
git -C dist-packages/openerp/ commit -m "inicial"
git -C extra-addons/ init
git -C extra-addons/ add .
git -C extra-addons/ commit -m "inicial"

