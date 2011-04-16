#!/bin/bash

APP_DIR="/var/www/nightreading"
SOCK_FILE=$APP_DIR+"/django.sock"
PIDFILE=$APP_DIR+"/django.pid"


git pull
git archive  master | tar -C $APP_DIR -xf -

if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
    sleep 1
fi

set -x
python manage.py \
    runfcgi method=threaded \
    debug=true --pythonpath=$APP_DIR \
    pidfile=$PIDFILE \
    host=127.0.0.1 port=8205
    #maxspare=3 minspare=1 maxchildren=5 maxrequests=500 \
    #socket=$SOCK_FILE \
set +x
 
