#!/usr/bin/env bash

# eliminar los backups locales
sudo rm -r /odoo_ar/odoo-11.0e/digital/backup_dir/*

# traerse los backups
scp odoo11@sams:/odoo_ar/odoo-11.0/sams/backup_dir/2019_04_03* /odoo_ar/odoo-11.0/sams/backup_dir/

# restorear el backup mas nuevo
sudo docker run --rm -i \
    --link pg-sams:db \
    -v /odoo_ar/odoo-11.0/sams/backup_dir/:/backup \
    -v /odoo_ar/odoo-11.0/sams/data_dir/filestore:/filestore \
    --env NEW_DBNAME=sams_prod \
    --env DEACTIVATE=True \
    jobiols/dbtools
