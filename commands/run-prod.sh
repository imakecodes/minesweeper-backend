#!/bin/bash
uwsgi --module app.wsgi --http 0.0.0.0:8000 --enable-threads --thunder-lock
