#!/usr/bin/env bash
# tecnopropy-tatakua-sh-master-1077424_daily.zip

# Desempaquetar la base de sh en un tmp
sudo rm -r tmp/
unzip "$1" -d tmp
gunzip tmp/tecnopropy-tatakua-sh-master-1077424_daily.sql.gz
mv tmp/tecnopropy-tatakua-sh-master-1077424_daily.sql dump.sql

# Crear copia de la base vacia
cp tatakua_prod_2020-05-18_18-18-22.zip bd_vacia.zip

# eliminar el dump de la base vacia
zip -d bd_vacia.zip dump.sql

# agregar el dump de la base de sh
zip -u bd_vacia.zip dump.sql

# traer el filestore
sudo rm -r filestore
mkdir filestore
cp -r tmp/tecnopropy-tatakua-sh-master-1077424_daily/home/odoo/data/filestore/tecnopropy-tatakua-sh-master-1077424/* filestore

# eliminar el filestore de la base vacia
zip -d bd_vacia.zip filestore

# agregar el filestore nuevo a la base vacia
zip -ur bd_vacia.zip filestore

mv bd_vacia.zip /odoo_ar/odoo-13.0e/tatakua/backup_dir/

oe --restore