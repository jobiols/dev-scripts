#!/usr/bin/env bash

# eliminar los backups locales
sudo rm -r /odoo_ar/odoo-11.0/vhing/backup_dir/*

# traerse los backups
scp ubuntu@vhing:/odoo_ar/odoo-11.0/vhing/backup_dir/2019_02_19_15* /odoo_ar/odoo-11.0/vhing/backup_dir/

# restorear el backup mas nuevo
sudo docker run --rm -i \
    --link pg-vhing:db \
    -v /odoo_ar/odoo-11.0/vhing/backup_dir/:/backup \
    -v /odoo_ar/odoo-11.0/vhing/data_dir/filestore:/filestore \
    --env NEW_DBNAME=vhing_prod \
    --env DEACTIVATE=True \
    jobiols/dbtools
