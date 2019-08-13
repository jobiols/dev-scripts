#!/usr/bin/env bash
# uso make_readme version client 
# 
# make_readme.sh 11.0 digital

oca-gen-addon-readme \
	--org-name jobiols \
	--repo-name odoo-addons \
	--branch 11.0 \
	--addons-dir /odoo_ar/odoo-11.0/test11/sources/odoo-addons \
	--gen-html

