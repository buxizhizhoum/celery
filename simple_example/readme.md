#Basic usage

cd to directory where the script to run is in. Here we cd to the directory where tasks.py is in.

start celery:
     
     celery -A <script_name_to_run_no_suffix> worker --loglevel=info

start script to get result from celery backend:
     
     python get_result.py


#Work with supervisor

create supervisor config file add below lines to config file:

    [program:celery_tasks]
    ;directory is where the script is in
    directory=/home/buxizhizhoum/1-Work/2-Codes/celery/bin/simple_example
    ;how to start the process
    command=celery -A tasks worker


manage with supervisor:
    
    supervisord  # this command will start all of the processes
    supervisorctl status
    supervisorctl stop <process name>
    supervisorctl start <process name>
    supervisorctl tail <process name>  # get output of process
