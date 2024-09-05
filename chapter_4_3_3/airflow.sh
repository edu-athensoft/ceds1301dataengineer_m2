#!/bin/bash

case $1 in
"start"){
    echo "-----start airflow-------"
    airflow webserver -p 8080 -D;airflow scheduler &
};;
"stop"){
    echo "-----stop  airflow-------"
    ps -ef|egrep 'scheduler|airflow-webserver'|grep -v grep|awk '{print $2}'|xargs kill -15
};;
esac