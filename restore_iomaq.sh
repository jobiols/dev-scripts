#!/usr/bin/env bash

# eliminar los backups locales
sudo rm -r /odoo_ar/odoo-9.0/iomaq/backup_dir/*

# traerse los backups
#scp ubuntu@iomaq:/odoo_ar/odoo-9.0/iomaq/backup_dir/iomaq_prod_automatic_20190309_* /odoo_ar/odoo-9.0/iomaq/backup_dir/
scp ubuntu@iomaq:/odoo_ar/odoo-9.0/iomaq/backup_dir/iomaq_6* /odoo_ar/odoo-9.0/iomaq/backup_dir/

sudo docker run --rm -i \
    --link pg-iomaq:db \
    -v /odoo_ar/odoo-9.0/iomaq/backup_dir/:/backup \
    -v /odoo_ar/odoo-9.0/iomaq/data_dir/filestore:/filestore \
    --env NEW_DBNAME=iomaq_prod \
    --env DEACTIVATE=True \
    jobiols/dbtools
