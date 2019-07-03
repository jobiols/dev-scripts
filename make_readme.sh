#!/usr/bin/env bash
# uso make_readme module client version repo
# 
# make_readme.sh sale_order_validity_fix iomaq 9.0 cl-iomaq

oca-gen-addon-readme \
    --org-name=jeosoft \
    --repo-name=$1 \
    --branch=11.0 \
    --addon-dir=/odoo_ar/odoo-$3/$2/sources/$4/$1 \
    --gen-html

