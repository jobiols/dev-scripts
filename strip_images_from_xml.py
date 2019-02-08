# -*- coding: utf-8 -*-
# For copyright and license notices, see __manifest__.py file in module root

from xml.etree.ElementTree import ElementTree

# leer el xml
tree = ElementTree()
tree.parse("/odoo_ar/odoo-11.0/vhing/sources/cl-vhing/project_eng/data/sales_order_data_demo_master.xml")

root = tree.getroot()
for x in range(3):
    # obtener todos los nodos record
    for record in root.findall(".//record"):
        for field in record:
            # eliminar campos indeseables
            if field.get('name') in ['tax_id','website_description','write_uid','create_date']:
                record.remove(field)

tree.write('/odoo_ar/odoo-11.0/vhing/sources/cl-vhing/project_eng/data/sales_order_data_demo.xml')
