#!/usr/bin/env bash
exec gunicorn --config gunicorn.conf.py app:app