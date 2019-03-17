#!/usr/bin/env bash

# restorear el backup que viene en $1 con el nombre $2
sudo docker run --rm -i \
    --link pg-polimera:db \
    -v /odoo_ar/odoo-11.0e/polimera/backup_dir/:/backup \
    -v /odoo_ar/odoo-11.0e/polimera/data_dir/filestore:/filestore \
    --env NEW_DBNAME=$2 \
    --env ZIPFILE=$1 \
    --env DEACTIVATE=True \
    jobiols/dbtools
