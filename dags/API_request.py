# https://api.openweathermap.org/data/3.0/onecall?lat=-34.8806944444&lon=-57.9958055556&appid=a0e5483662a5faed42697e1d9119b3a1

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