from __future__ import annotations

import pendulum

from airflow.datasets import Dataset
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

# [START dataset_def]
dag1_dataset = Dataset("s3://dag1/output_1.txt", extra={"hi": "bye"})
# [END dataset_def]
dag2_dataset = Dataset("s3://dag2/output_1.txt", extra={"hi": "bye"})

with DAG(
    dag_id="ops_silver_trigger_30min_SLA",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule="@daily",
    tags=["produces", "dataset-scheduled"],
) as dag1:
    BashOperator(outlets=[dag1_dataset], task_id="inbound_grns", bash_command="sleep 5")

