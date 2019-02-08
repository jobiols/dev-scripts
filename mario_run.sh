#!/usr/bin/env bash
#    -p 139:139 -p 445:445 \

#sudo docker volume create --name fiscal_spooler

sudo docker run -it -d -p 139:139 -p 445:445 --name samba \
    -v /fiscal_spooler:/mnt/media \
    dperson/samba \
    -u "analia;dacid214" \
    -s "fiscal;/mnt/media;yes;no;yes;all"

sudo docker run --rm -it \
    --link aeroo:aeroo \
    -p 1984:1984 \
    -p 8069:8069 \
    -p 8072:8072 \
    -v /fiscal_spooler:/opt/odoo/fiscal_spooler \
    -v /odoo_ar/odoo-9.0/mario/config:/opt/odoo/etc/ \
    -v /odoo_ar/odoo-9.0/mario/data_dir:/opt/odoo/data \
    -v /odoo_ar/odoo-9.0/mario/log:/var/log/odoo \
    -v /odoo_ar/odoo-9.0/mario/sources:/opt/odoo/custom-addons \
    -v /odoo_ar/odoo-9.0/mario/backup_dir:/var/odoo/backups/ \
    -v /odoo_ar/odoo-9.0/extra-addons:/opt/odoo/extra-addons \
    -v /odoo_ar/odoo-9.0/dist-packages:/usr/lib/python2.7/dist-packages \
    --link pg-mario:db \
    --name mario \
    -e ODOO_CONF=/dev/null \
    -e SERVER_MODE=test \
    jobiols/odoo-jeo:9.0.f.debug --logfile=/dev/stdout
