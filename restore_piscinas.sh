#!/usr/bin/env bash

# eliminar los backups locales
sudo rm -r /odoo_ar/odoo-11.0/piscinas/backup_dir/*

# traerse los backups
scp root@work:/odoo_ar/odoo-11.0/piscinas/backup_dir/2019_03_06* /odoo_ar/odoo-11.0/piscinas/backup_dir/

# restorear el backup mas nuevo
sudo docker run --rm -i \
    --link pg-piscinas:db \
    -v /odoo_ar/odoo-11.0/piscinas/backup_dir/:/backup \
    -v /odoo_ar/odoo-11.0/piscinas/data_dir/filestore:/filestore \
    --env NEW_DBNAME=piscinas_prod \
    --env DEACTIVATE=True \
    jobiols/dbtools

