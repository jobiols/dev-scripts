#!/usr/bin/env bash
#######################################################################
# Restore newest backup from production to local deactivating database.
# parameters: client version
# por ejemplo ./restore_database.sh polimera 11.0

client=$1
version=$2
username=$3
server=$username"@"$client

echo $server

dir="/odoo_ar/odoo-"$version/$client
bkp=$dir"/backup_dir"

# si hay algun parametro en 3 NO traigo la bd de produccion
if [ -z "$3" ]
then
   # eliminar los backups locales
   echo "Remove local backups in "$bkp
   sudo rm -r $bkp/*

   # traerse el backup mas nuevo
   echo "Getting newest backup from "$server
   scp $server:$bkp/$(ssh $server "ls -t $bkp/ | head -1") $bkp/
fi

# restorear el backup mas nuevo que encuentre
sudo docker run --rm -i \
    --link "pg-"$client":db" \
    -v $bkp/:/backup \
    -v $dir/data_dir/filestore:/filestore \
    --env NEW_DBNAME=$client"_prod" \
    --env DEACTIVATE=True \
    jobiols/dbtools:1.1.0
