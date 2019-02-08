#!/usr/bin/env bash

sudo docker run --rm -it -p 1984:1984 -p 8069:8069 \
	-v /odoo/odoo-10.0+e/agt/config:/etc/odoo \
	-v /odoo/odoo-10.0+e/agt/data_dir:/var/lib/odoo \
	-v /odoo/odoo-10.0+e/sources:/mnt/extra-addons \
	-v /odoo/odoo-10.0+e/sources/dist-packages:/usr/lib/python2.7/dist-packages \
	-v /odoo/odoo-10.0+e/agt/log:/var/log/odoo \
	--link postgres:db \
	--name agt jobiols/odoo-e:10.0e-20170616.debug -- --logfile=False

