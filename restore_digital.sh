#!/usr/bin/env bash

# eliminar los backups locales
sudo rm -r /odoo_ar/odoo-11.0e/digital/backup_dir/*

# traerse los backups
scp argentina@digital:/odoo_ar/odoo-11.0e/digital/backup_dir/2019_03_1* /odoo_ar/odoo-11.0e/digital/backup_dir/

# restorear el backup mas nuevo
sudo docker run --rm -i \
    --link pg-digital:db \
    -v /odoo_ar/odoo-11.0e/digital/backup_dir/:/backup \
    -v /odoo_ar/odoo-11.0e/digital/data_dir/filestore:/filestore \
    --env NEW_DBNAME=digital_prod \
    --env DEACTIVATE=True \
    jobiols/dbtools
