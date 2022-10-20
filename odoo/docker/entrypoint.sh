echo -e "db_host=$POSTGRES_HOST \n
db_user=$POSTGRES_USER \n
database=$POSTGRES_DB \n
db_port=$POSTGRES_PORT \n
db_password=$POSTGRES_PASSWORD \n
data-dir=/opt/odoo_data_dir \n
addons-path=/mnt/extra-addons,/mnt/extra-addons-customize \n
init=base,crm \n
without-demo=all \n
log-request \n
log-handler=odoo.http.rpc.request:DEBUG \n
log-handler=odoo.http.rpc.response:DEBUG" > odoo/odoo.conf