from __future__ import annotations

import json
import os
from datetime import datetime

from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.python import PythonOperator
from google.cloud import storage

DAG_ID = "primer_intento_api_request"

api_dag = DAG(
    DAG_ID,
    default_args = {"retries" : 1},
    start_date = datetime(2025,1,31),
    catchup = False
)

# Esta es la tarea necesaria para obtener la información del HTTP, es decir, de nuestra API
get_data_from_api = SimpleHttpOperator(
    task_id="get_http_data",
    http_conn_id="http_conn_id_demo",
    method="GET",
    endpoint=f"https://api.openweathermap.org/data/3.0/onecall?lat=-34.8806944444&lon=-57.9958055556&appid={}",
    response_filter = lambda response : json.loads(response.text),
    dag=dag
)