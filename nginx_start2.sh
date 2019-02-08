#!/usr/bin/env bash

#!/usr/bin/env bash
sd run -d \
    --name=nginx \
    --restart=always \
    --link maketest:odoo \
    -v /odoo/nginx:/etc/nginx/conf.d:ro \
    -p 80:80 \
    -p 443:443 \
    nginx