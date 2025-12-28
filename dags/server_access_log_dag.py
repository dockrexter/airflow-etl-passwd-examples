# Import the libraries
from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow.models import DAG
# Operators; you need this to write tasks!
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# This makes scheduling easy
from airflow.utils.dates import days_ago
import os

BASH_SCRIPT_PATH = os.path.join(os.path.dirname(__file__), 'server_access_log.sh')
extracted_log = '/usr/local/airflow/dags/extracted-log.txt'
transformed_file = '/usr/local/airflow/dags/transformed.txt'
output_file = '/usr/local/airflow/dags/data_for_analytics.csv'

def transform():
    global extracted_log, transformed_file
    print("Inside Transform")
    with open(extracted_log, 'r') as infile, \
            open(transformed_file, 'w') as outfile:
        for line in infile:
            processed_line = line.replace('#', ',')
            outfile.write(processed_line + '\n')

def load():
    global transformed_file, output_file
    print("Inside Load")
    with open(transformed_file, 'r') as infile, \
            open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(line)

def check():
    global output_file
    print("Inside Check")
    with open(output_file, 'r') as infile:
        for line in infile:
            print(line)

# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'Shaheer Rahi',
    'start_date': days_ago(0),
    'email': ['mshaheer.rahi@gmail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}           
# Define the DAG
with DAG(
    'server_access_log_dag',
    default_args=default_args,
    description='A simple ETL DAG for server access logs',
    schedule_interval=timedelta(days=1),
) as dag:

    # Define the tasks
    extract_task = BashOperator(
        task_id='extract',
        bash_command=f'bash /usr/local/airflow/dags/server_access_log.sh '
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load,
    )

    check_task = PythonOperator(
        task_id='check',
        python_callable=check,
    )

    # Set the task dependencies
    extract_task >> transform_task >> load_task >> check_task
