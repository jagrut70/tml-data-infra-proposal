from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {"owner": "data-infra", "retries": 1, "retry_delay": timedelta(minutes=5)}

with DAG(
    dag_id="stream_crawl_to_bronze",
    default_args=default_args,
    start_date=datetime(2025,1,1),
    schedule_interval=None,  # trigger manually or via sensor
    catchup=False,
) as dag:
    run_stream = BashOperator(
        task_id="run_stream",
        bash_command="python /opt/repo/spark_jobs/stream_to_delta.py --config /opt/repo/configs/local.example.json"
    )
