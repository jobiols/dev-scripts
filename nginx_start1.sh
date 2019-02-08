#!/usr/bin/env bash

sd run -d \
    --link aeroo:aeroo \
    -v /odoo/odoo-8.0/maketest/config:/etc/odoo \
    -v /odoo/odoo-8.0/maketest/data_dir:/var/lib/odoo \
    -v /odoo/odoo-8.0/sources:/mnt/extra-addons \
    -v /odoo/odoo-8.0/maketest/log:/var/log/odoo \
    --link postgres:db \
    --restart=always \
    --name maketest \
    jobiols/odoo-jeo:8.0 -- --db-filter=maketest_.* --logfile=/var/log/odoo/odoo.log


