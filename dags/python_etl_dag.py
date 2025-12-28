from datetime import timedelta
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

# Define the path for the input and output files
input_file = '/etc/passwd'
extracted_file = 'extracted-data.txt'
transformed_file = 'transformed.txt'
output_file = 'data_for_analytics.csv'


def extract():
    print("Inside Extract")
    with open(input_file, 'r') as infile, \
         open(extracted_file, 'w') as outfile:
        for line in infile:
            fields = line.split(':')
            if len(fields) >= 6:
                field_1 = fields[0]      # username
                field_3 = fields[2]      # UID
                field_6 = fields[5]      # home directory
                outfile.write(f"{field_1}:{field_3}:{field_6}\n")


def transform():
    print("Inside Transform")
    with open(extracted_file, 'r') as infile, \
         open(transformed_file, 'w') as outfile:
        for line in infile:
            processed_line = line.replace(':', ',')
            outfile.write(processed_line + '\n')


def load():
    print("Inside Load")
    with open(transformed_file, 'r') as infile, \
         open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(line + '\n')


def check():
    print("Inside Check")
    with open(output_file, 'r') as infile:
        for line in infile:
            print(line.strip())


# Default arguments
default_args = {
    'owner': 'Shaheer Rahi',
    'start_date': days_ago(0),
    'email': ['youremail'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'python_etl_passwd_dag',
    default_args=default_args,
    description='ETL pipeline for /etc/passwd using PythonOperator',
    schedule_interval=timedelta(days=1),
)

# Define tasks
execute_extract = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag,
)

execute_transform = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag,
)

execute_load = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag,
)

execute_check = PythonOperator(
    task_id='check',
    python_callable=check,
    dag=dag,
)

# Task pipeline
execute_extract >> execute_transform >> execute_load >> execute_check
