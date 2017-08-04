# Let's move to the directory where the project is
cd /var/www/airhockey

source /usr/local/bin/virtualenvwrapper.sh
workon air-hockey

screen -mdS redis redis-server
screen -mdS server gunicorn --no-sendfile --bind 0.0.0.0:8000 --worker-class=gevent -t 99999 air-hockey:app
