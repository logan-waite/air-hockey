After running *install.sh*, you should have everything you need installed to run the air hockey server. To start the server, the following commands will need to be run.

First, log out then log back in. This will automatically put you into the virtual environment that the server is in to run. Alternatively, you can run the following commands to get into the environment:

    source /usr/local/bin/virtualenvwrapper.sh
    workon air-hockey

Once in the virtualenv, make sure you are in */var/www/airhockey* and start the redis server in a screen so it can run in the background without bothering anybody.

    screen -mdS redis redis-server

If you ever want or need to look at this screen, you can use the command `screen -r redis-server` to switch to the screen, and then `ctrl-a d` to detach and leave the process running in the background.

Then, to run the web server, we're using the gunicorn service with the gevent worker so the "chat" system will work. Run that using:

    screen -mdS server gunicorn --no-sendfile --bind 0.0.0.0:8000 --worker-class=gevent -t 99999 air-hockey:app

It's in a screen so you can still do stuff on the server without having to turn off the server.
