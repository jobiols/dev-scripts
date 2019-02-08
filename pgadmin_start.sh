#!/bin/bash
#	conectarse con un server odoo
#	Nombre: pg-iomaq (nombre de la imagen)
# 	puerto 5432
#	base de datos de mantenimiento: postgres
#	nombre de usuario: odoo
# 	el nombre del host es el nombre de la imagen


sd pull dpage/pgadmin4
sd run -p 80:80 \
	-e "PGADMIN_DEFAULT_EMAIL=odoo" \
	-e "PGADMIN_DEFAULT_PASSWORD=odoo" \
	--link pg-vhing:db \
	--name pgadmin4 \
	-d dpage/pgadmin4
