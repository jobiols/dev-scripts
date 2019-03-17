#!/usr/bin/env bash

# eliminar los backups locales
sudo rm -r /odoo_ar/odoo-11.0e/polimera/backup_dir/*

# traerse los backups
scp ubuntu@polimera:/odoo_ar/odoo-11.0e/polimera/backup_dir/2019_03_1* /odoo_ar/odoo-11.0e/polimera/backup_dir/

# restorear el backup mas nuevo
sudo docker run --rm -i \
    --link pg-polimera:db \
    -v /odoo_ar/odoo-11.0e/polimera/backup_dir/:/backup \
    -v /odoo_ar/odoo-11.0e/polimera/data_dir/filestore:/filestore \
    --env NEW_DBNAME=polimera_prod \
    --env DEACTIVATE=True \
    jobiols/dbtools
