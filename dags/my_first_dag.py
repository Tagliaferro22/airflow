from airflow import DAG
from airflow.operators.bash import BashOperator  
from airflow.operators.python import PythonOperator 
from datetime import datetime, timedelta
from random import randint

TAGS =  ["Mi primer dag"] # Un tag para posteriormente poder filtrar el DAG
DAG_ID = "MI_PRIMER_DAG"
DAG_DESCRIPTION = """El primer DAG que programo en mi vida, hola mundo"""
DAG_SCHEDULE = "0 9 * * *" # Se ejecuta todos los días a las 9AM

retries = 4 # La cantidad de reintentos
retry_delay = timedelta(minutes=5) # Va a tomarse una pausa de 5 minutos entre cada reintento

def execute_task():
    return f"¡Hola, mundo! {randint(1,10)}"

dag = DAG(
    dag_id = DAG_ID,
    description = DAG_DESCRIPTION,
    catchup = False,
    schedule_interval = DAG_SCHEDULE,
    max_active_runs = 1,
    dagrun_timeout = timedelta(minutes=3, seconds=20),
    default_args = {"start_date" : datetime(2025, 1, 29)},
    tags=TAGS
)

with dag as using_dag:
    start_task = BashOperator(
        task_id = "inicia_el_proceso",
        bash_command='echo "Esta tarea no hace nada"'
    )

    end_task = BashOperator(
        task_id = "finaliza_el_proceso",
        bash_command='echo "Esta tarea no hace nada"'
    )

    first_task = PythonOperator(
        task_id = "primera_tarea",
        python_callable = execute_task,
        retries = retries,
        retry_delay = retry_delay
    )

start_task >> first_task >> end_task # Establecemos las dependencias de las tareas, first_task depende de que se ejecute start_task, mientras que end_task depende de que se ejecuten tanto start_task cómo luego first_task
