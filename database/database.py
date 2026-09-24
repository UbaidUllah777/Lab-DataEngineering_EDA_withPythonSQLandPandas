import os

import pandas as pd
import psycopg2

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    load_dotenv = None


class Database:
    def __init__(self, connection_string=None):
        if load_dotenv:
            load_dotenv()
        self.connection_string = connection_string or os.getenv("DATABASE_URL")
        self.connection = None
        self.cursor = None

    def connect(self):
        if not self.connection_string:
            raise ValueError("DATABASE_URL is not set.")

        self.connection = psycopg2.connect(self.connection_string)
        self.cursor = self.connection.cursor()
        return self.connection

    def create_employees_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            position VARCHAR(100),
            start_date DATE,
            salary INTEGER
        );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_employees(self, employees_df):
        insert_query = """
        INSERT INTO employees (employee_id, name, position, start_date, salary)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (employee_id) DO NOTHING;
        """

        for _, row in employees_df.iterrows():
            self.cursor.execute(
                insert_query,
                (
                    row["employee_id"],
                    row["name"],
                    row["position"],
                    row["start_date"],
                    row["salary"],
                ),
            )

        self.connection.commit()

    def count_employees(self):
        self.cursor.execute("SELECT COUNT(*) FROM employees;")
        return self.cursor.fetchone()[0]

    def get_employees(self):
        return pd.read_sql_query("SELECT * FROM employees;", self.connection)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
