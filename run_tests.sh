#    -v /odoo_ar/odoo-13.0e/extra-addons:/opt/odoo/extra-addons \
#    -v /odoo_ar/odoo-13.0e/dist-packages:/usr/lib/python3/dist-packages \
#    -v /odoo_ar/odoo-13.0e/dist-local-packages:/usr/local/lib/python3.7/dist-local-packages \


#!/bin/sh
sudo docker run --rm -it \
    -v /odoo_ar/odoo-13.0e/tatakua/config_test:/opt/odoo/etc/ \
    -v /odoo_ar/odoo-13.0e/tatakua/data_dir:/opt/odoo/data \
    -v /odoo_ar/odoo-13.0e/tatakua/log:/var/log/odoo \
    -v /odoo_ar/odoo-13.0e/tatakua/sources_test:/opt/odoo/custom-addons \
    -v /odoo_ar/odoo-13.0e/tatakua/backup_dir:/var/odoo/backups/ \
    --link pg-tatakua:db \
    -e ODOO_CONF=/dev/null \
    jobiols/odoo-ent:13.0e -- \
    --stop-after-init --logfile=false -d tatakua_test -u all --test-enable
