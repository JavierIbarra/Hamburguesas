From odoo:14.0

USER root

COPY ./addons-customize /mnt/extra-addons-customize
COPY ./config /etc/odoo

COPY ./docker/docker-entrypoint.sh entrypoint.sh
RUN chmod +x /entrypoint.sh

USER odoo

ENTRYPOINT [ "/entrypoint.sh" ]