#! /bin/bash
gunicorn --bind :8000 TestTask.wsgi:application
