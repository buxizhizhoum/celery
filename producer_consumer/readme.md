#Basic usage

cd to directory where the script to run is in. Here we cd to the directory where task_consumer.py is in.

start celery:
     
     celery -A <script_name_to_run_no_suffix> worker --loglevel=info

start script to get result from celery backend:
     
     python task_producer.py
