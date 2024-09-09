from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
        dag_id='airflow_data_warehouse_stream_collect',
        #schedule_interval='0/6 * * * *',
        start_date=datetime(2024, 1, 1),
        catchup=False,
        default_args={'depends_on_past': True},
        tags=['data_warehouse_example']
) as dag:
    start = BashOperator(
        task_id="print_start_date",
        bash_command="date",)

    stream_logs_collect_util_task = BashOperator(
        task_id='stream_logs_collect_util_task',
        bash_command='/Users/kevin/workspace/tools/airflow/dags/chapter_2_3_6_stream/dist/realtime_logs_collect_util',
    )

    end = BashOperator(
        task_id="print_end_date",
        bash_command="date",)

    start >> stream_logs_collect_util_task >> end