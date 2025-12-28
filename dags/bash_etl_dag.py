from datetime import timedelta
from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# Update this path to where etl_passwd.sh is located
BASH_SCRIPT_PATH = '/path/to/your/etl_passwd.sh'

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
    'bash_etl_passwd_dag',
    default_args=default_args,
    description='ETL pipeline for /etc/passwd using BashOperator',
    schedule_interval=timedelta(days=1),
)

# Run the Bash script
run_etl_script = BashOperator(
    task_id='run_etl_script',
    bash_command=f'bash {BASH_SCRIPT_PATH}',
    dag=dag,
)
