from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
        dag_id='airflow_data_warehouse_log_collect',
        schedule_interval='0/3 * * * *',
        start_date=datetime(2024, 1, 1),
        catchup=False,
        default_args={'depends_on_past': True},
        tags=['data_warehouse_example']
) as dag:
    backend_logs_generate_util_task = BashOperator(
        task_id='backend_logs_generate_util_task',
        bash_command='/Users/kevin/workspace/tools/airflow/dags/chapter_2_3_3_log/dist/backend_logs_generate_util',
    )
    backend_logs_collect_util_task = BashOperator(
        task_id='backend_logs_collect_util_task',
        bash_command='/Users/kevin/workspace/tools/airflow/dags/chapter_2_3_3_log/dist/backend_logs_collect_util',
    )
    backend_logs_generate_util_task >> backend_logs_collect_util_task


