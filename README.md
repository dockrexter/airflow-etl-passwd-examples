# Airflow ETL: Extract /etc/passwd to CSV (Python vs Bash)

This repository contains two Airflow DAGs that perform the same ETL task:

1. A **Python-based DAG** using `PythonOperator`.  
2. A **Bash-based DAG** using `BashOperator`.

Both pipelines:
- Extract username, UID, and home directory from `/etc/passwd`.  
- Transform the data into CSV format.  
- Load it into `data_for_analytics.csv`.  
- Include a check step to print the final output.

---




## 🛠️ Prerequisites

- Apache Airflow installed and running.  
- Access to a Unix-like system (Linux/macOS) with `/etc/passwd`.  
- The Airflow worker must have:
  - Read access to `/etc/passwd`.  
  - Write access to the directory where the DAGs and script are located.

---

## 🚀 How to use

### 1. Clone the repo
git clone https://github.com/dockrexter/airflow-etl-passwd-comparison.git 
cd airflow-etl-passwd-comparison



### 3. Update the Bash DAG with the correct path

In `dags/bash_etl_dag.py`, update `BASH_SCRIPT_PATH` to the full path of `etl_passwd.sh`:

BASH_SCRIPT_PATH = ‘/full/path/to/airflow-etl-passwd-comparison/etl_passwd.sh’



### 4. Copy DAGs to Airflow

Copy the DAG files to your Airflow `dags/` folder:


### 5. Start Airflow


### 6. Enable and run the DAGs

In the Airflow UI:
- Enable `python_etl_passwd_dag` and trigger a run.  
- Enable `bash_etl_passwd_dag` and trigger a run.

---

## 📊 Output files

After a successful run, you will find these files in the same directory as the DAGs:

- `extracted-data.txt` – colon-separated: `username:UID:home_directory`  
- `transformed.txt` – comma-separated: `username,UID,home_directory`  
- `data_for_analytics.csv` – final CSV file (same as `transformed.txt`).



