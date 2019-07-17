#!/usr/bin/env bash
# uso make_readme version client 
# 
# make_readme.sh 11.0 digital

oca-gen-addon-readme \
	--org-name jobiols \
	--repo-name odoo-addons \
	--branch 9.0 \
	--addons-dir /odoo_ar/odoo-9.0/iomaq/sources/odoo-addons \
	--gen-html

oca-gen-addon-readme \
        --org-name jobiols \
        --repo-name cl-iomaq \
        --branch 9.0 \
        --addons-dir /odoo_ar/odoo-9.0/iomaq/sources/cl-iomaq \
        --gen-html

