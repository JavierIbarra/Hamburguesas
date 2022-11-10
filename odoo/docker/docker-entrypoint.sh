#!/bin/bash

/usr/bin/odoo \
    --init crm,sale,stock,l10n_cl \
    --without-demo all \
    --database $DB_ODOO \
    --db_host $HOST \
    --db_user $USER \
    --db_port $PORT  \
    --db_password $PASSWORD \