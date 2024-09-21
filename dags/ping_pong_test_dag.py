from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import requests

default_args = {
    'start_date': datetime(2023, 9, 20),
    'retries': 1,
}

def trigger_coworker_script1():
    url = 'http://127.0.0.1:4041/trigger'
    data = {
        'project': 'pingpong-test',
        'branch': 'main',
        'script': 'ping_pong.py',
        'parameters': ['ping']  # Übergabeparameter hier
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Erfolg: ", response.text)
    else:
        print("Fehler: ", response.text)

def trigger_coworker_script1():
    url = 'http://127.0.0.1:4041/trigger'
    data = {
        'project': 'pingpong-test',
        'branch': 'main',
        'script': 'ding_dong.py',
        'parameters': ['ding']  # Übergabeparameter hier
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Erfolg: ", response.text)
    else:
        print("Fehler: ", response.text)

with DAG('coworker_pingpong', default_args=default_args, schedule_interval='@once') as dag:
    send_request = PythonOperator(
        task_id='trigger_coworker',
        python_callable=trigger_coworker_script1()
    )
