#!/usr/bin/env bash

# eliminar los backups locales
sudo rm -r /odoo_ar/odoo-8.0/makeover/backup_dir/*

# traerse los backups
scp ubuntu@makeover:/odoo_ar/odoo-8.0/makeover/backup_dir/makeover_prod_automatic_20190313* /odoo_ar/odoo-8.0/makeover/backup_dir/

# restorear el backup mas nuevo
sudo docker run --rm -i \
    --link pg-makeover:db \
    -v /odoo_ar/odoo-8.0/makeover/backup_dir/:/backup \
    -v /odoo_ar/odoo-8.0/makeover/data_dir/filestore:/filestore \
    --env NEW_DBNAME=makeover_prod \
    --env DEACTIVATE=True \
    jobiols/dbtools

