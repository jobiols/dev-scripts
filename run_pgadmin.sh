#!/bin/bash
# USO ./pgadmin_start.sh docker_db_name

# Como conectarse con un server odoo
# Arrancar esto y conectarse a localhost:80
# Entrar con credenciales odoo@odoo.com / odoo
#  General
#     name nombrecliente
#  Connection
#	Host nombredelaimagenposgress
#	Port 5432
#	Maintenance database: postgres
#	Username odoo
#	Password odoo

#	--link $1 \

sd pull dpage/pgadmin4
sd run -p 80:80 \
	-e "PGADMIN_DEFAULT_EMAIL=odoo@odoo.com" \
	-e "PGADMIN_DEFAULT_PASSWORD=odoo" \
	--link $1 \
	--name pgadmin4 \
	-d dpage/pgadmin4 



