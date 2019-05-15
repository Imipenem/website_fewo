#!/bin/bash
# Reference:
# https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04

apt-get update

apt-get install python3-pip python3-dev nginx

pip3 install virtualenv

cd ~

git clone https://github.com/Imipenem/website_fewo

cd website_fewo

virtualenv dpenv

source dpenv/bin/activate

pip3 install gunicorn

python setup.py clean --all install

cp /home/laurin001/website_fewo/production_setup/website_fewo.service \
/etc/systemd/system/website_fewo.service

systemctl start website_fewo

systemctl enable website_fewo

cp /home/laurin001/website_fewo/production_setup/website_fewo \
/etc/nginx/sites-available/webiste_fewo

ln -s /etc/nginx/sites-available/website_fewo /etc/nginx/sites-enabled

nginx -t

systemctl restart nginx

ufw delete allow 5000

ufw allow 'Nginx Full'

add-apt-repository ppa:certbot/certbot -y

apt install python-certbot-nginx -y

certbot --nginx -d ferienwohnung-ehmele.de -d www.ferienwohnung-ehmele.de --non-interactive --agree-tos -m philipp_ehm@protonmail.com
