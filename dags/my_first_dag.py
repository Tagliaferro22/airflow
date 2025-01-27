from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime
from random import randint

def _training_model():
    return randint(1,10)

with DAG("my_first_dag_ever", start_date=datetime(2021,1,1), schedule_interval="@daily",catchup=False) as dag:
    training_model_A = PythonOperator(
        task_id = "training_model_A"
        python_callable = _training_model
    )