#!/usr/bin/env bash

# eliminar los backups locales
sudo rm -r /odoo_ar/odoo-11.0e/sonoras/backup_dir/*

# traerse los backups
scp root@work:/odoo_ar/odoo-11.0e/sonoras/backup_dir/2019_03_07* /odoo_ar/odoo-11.0e/sonoras/backup_dir/

# restorear el backup mas nuevo
sudo docker run --rm -i \
    --link pg-sonoras:db \
    -v /odoo_ar/odoo-11.0e/sonoras/backup_dir/:/backup \
    -v /odoo_ar/odoo-11.0e/sonoras/data_dir/filestore:/filestore \
    --env NEW_DBNAME=sonoras_prod \
    --env DEACTIVATE=True \
    jobiols/dbtools

