#!/bin/sh
PROJ_DIR=/srv/django/adamthorson_prod
UWSGI_INI=${PROJ_DIR}/uwsgi.ini
UWSGI_NGINX_BASE=/var/run/nginx
UWSGI_NGINX_SOCK=${UWSGI_NGINX_BASE}/uwsgi.sock
# Setup uWSGI to nginx socket
sudo mkdir $UWSGI_NGINX_BASE
sudo touch $UWSGI_NGINX_SOCK
sudo chmod -R 770 $UWSGI_NGINX_BASE
sudo chown -R www-data:www-data $UWSGI_NGINX_BASE
# Start uWSGI
workon adamthorson_prod
cd $PROJ_DIR
uwsgi --ini $UWSGI_INI