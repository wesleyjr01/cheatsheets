from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from airflow.models import Connection
from airflow.utils.session import create_session

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
}


@dag(
    default_args=default_args,
    schedule_interval=None,
    description="Add an Airflow connection",
    tags=["example"],
)
def add_airflow_connection_dag():
    @task
    def add_connection():
        new_conn = Connection(
            conn_id="mysql-main-conn",  # Unique identifier for the connection
            conn_type="mysql",  # Type of the connection
            host="host.com",  # Hostname of the connection
            schema="schema",  # Schema/Dataset
            login="username",  # Username
            password="password",  # Password
            port=3306,  # Port number
        )
        # Use the create_session context manager to handle the session
        with create_session() as session:
            session.add(new_conn)
            session.commit()  # This commits the new connection to the database

    add_connection()


# Assign the DAG to a variable to be detected and loaded by Airflow
dag_instance = add_airflow_connection_dag()
