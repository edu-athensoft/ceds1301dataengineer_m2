from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
        dag_id='ods_dwd_dws_car_electric_driving',
        schedule_interval='0/3 * * * *',
        start_date=datetime(2024, 1, 1),
        catchup=False,
        default_args={'depends_on_past': True},
        tags=['data_warehouse_example']
) as dag:
    ods_car_data_logs_collect_task = BashOperator(
        task_id='ods_car_data_logs_collect_task',
        bash_command='/Users/kevin/workspace/tools/airflow/dags/chapter_5/dist/ods_car_data_logs_collect',
    )
    dwd_car_electric_driving_fact_generate_task = BashOperator(
        task_id='dwd_car_electric_driving_fact_generate_task',
        bash_command='/Users/kevin/workspace/tools/airflow/dags/chapter_5/dist/dwd_car_electric_driving_fact_generate',
    )
    dws_car_electric_driving_stats_d_generate_task = BashOperator(
        task_id='dws_car_electric_driving_stats_d_generate_task',
        bash_command='/Users/kevin/workspace/tools/airflow/dags/chapter_5/dist/dws_car_electric_driving_stats_d_generate',
    )

    ods_car_data_logs_collect_task >> dwd_car_electric_driving_fact_generate_task >> dws_car_electric_driving_stats_d_generate_task


