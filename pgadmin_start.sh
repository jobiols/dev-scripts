#!/bin/bash
# Como conectarse con un server odoo
# Arrancar esto y conectarse a localhost:80
# Entrar con credenciales odoo / odoo
#  General
#     name nombrecliente
#  Connection 
#	Host nombredelaimagenposgress
#	Port 5432
#	Maintenance database: postgres
#	Username odoo
#	Password odoo


sd pull dpage/pgadmin4
sd run -p 80:80 \
	-e "PGADMIN_DEFAULT_EMAIL=odoo" \
	-e "PGADMIN_DEFAULT_PASSWORD=odoo" \
	--link pg-narove:db \
	--name pgadmin4 \
	-d dpage/pgadmin4
