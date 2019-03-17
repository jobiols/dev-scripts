#!/usr/bin/env bash

# eliminar los backups locales
sudo rm -r /odoo_ar/odoo-11.0/geminis/backup_dir/*

# traerse los backups
scp root@work:/odoo_ar/odoo-11.0/geminis/backup_dir/2019_02_20* /odoo_ar/odoo-11.0/geminis/backup_dir/

# restorear el backup mas nuevo
sudo docker run --rm -i \
    --link pg-geminis:db \
    -v /odoo_ar/odoo-11.0/geminis/backup_dir/:/backup \
    -v /odoo_ar/odoo-11.0/geminis/data_dir/filestore:/filestore \
    --env NEW_DBNAME=geminis_prod \
    --env DEACTIVATE=True \
    jobiols/dbtools

