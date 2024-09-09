from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
        dag_id='airflow_data_warehouse_file_collect',
        schedule_interval='0/5 * * * *',
        start_date=datetime(2024, 1, 1),
        catchup=False,
        default_args={'depends_on_past': True},
        tags=['data_warehouse_example']
) as dag:
    start = BashOperator(
        task_id="print_start_date",
        bash_command="date",)

    file_collect_util_task = BashOperator(
        task_id='file_collect_util_task',
        bash_command='/Users/kevin/workspace/tools/airflow/dags/chapter_2_3_5_file/dist/order_json_collect',
    )

    end = BashOperator(
        task_id="print_end_date",
        bash_command="date",)

    start >> file_collect_util_task >> end