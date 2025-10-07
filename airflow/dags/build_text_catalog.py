from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "data-infra",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}

def build_catalog(**ctx):
    # placeholder: call CLI to materialize manifest → gold tables
    print("Building text catalog via manifest...")

with DAG(
    dag_id="build_text_catalog",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    max_active_runs=1,
) as dag:
    PythonOperator(task_id="build_catalog", python_callable=build_catalog)
