#    -v /odoo_ar/odoo-13.0e/tatakua/backup_dir:/var/odoo/backups/ \
#    -v /odoo_ar/odoo-13.0e/tatakua/log:/var/log/odoo \
#    -e ODOO_CONF=/dev/null \
#    --stop-after-init --logfile=false -d tatakua_test -u all --test-enable

#!/bin/sh
#cp -r /odoo_ar/odoo-13.0e/tatakua/sources/odoo-paraguay/l10n_py_invoice_document/ /odoo_ar/odoo-13.0e/tatakua/sources_test/odoo-paraguay/
#cp -r /odoo_ar/odoo-13.0e/tatakua/sources/odoo-paraguay/partner_ruc_unique/ /odoo_ar/odoo-13.0e/tatakua/sources_test/odoo-paraguay/
#cp -r /odoo_ar/odoo-13.0e/tatakua/sources/odoo-paraguay/l10n_py_reports/ /odoo_ar/odoo-13.0e/tatakua/sources_test/odoo-paraguay/
oe --restore -d tatakua_test -c tatakua

sudo docker run --rm -it \
    --link wdb \
    -v /odoo_ar/odoo-13.0e/tatakua/config:/opt/odoo/etc/ \
    -v /odoo_ar/odoo-13.0e/tatakua/data_dir:/opt/odoo/data \
    -v /odoo_ar/odoo-13.0e/tatakua/sources:/opt/odoo/custom-addons \
    -v /odoo_ar/odoo-13.0e/extra-addons:/opt/odoo/extra-addons \
    -v /odoo_ar/odoo-13.0e/dist-packages:/usr/lib/python3/dist-packages \
    -v /odoo_ar/odoo-13.0e/dist-local-packages:/usr/local/lib/python3.7/dist-local-packages \
    -e WDB_SOCKET_SERVER=wdb \
    --link pg-tatakua:db \
    jobiols/odoo-ent:13.0e.debug -- \
        -i  l10n_py \
   --stop-after-init -d tatakua_test \
        --test-enable




#        -i  l10n_py,l10n_py_invoice_document,partner_ruc_unique,l10n_py_reports,l10n_py_vat_book \
