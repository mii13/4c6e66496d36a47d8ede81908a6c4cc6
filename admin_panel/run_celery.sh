#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

# run Celery worker
celery worker -A admin_panel.celery --loglevel=info