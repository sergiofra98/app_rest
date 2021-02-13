#!/bin/bash
exec gunicorn --config gunicorn_config.py app_rest:app