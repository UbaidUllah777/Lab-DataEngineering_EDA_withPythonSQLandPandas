import random

import pandas as pd
from faker import Faker


class DataCollection:
    def __init__(self, seed=42):
        self.seed = seed
        self.fake = Faker()
        self.positions = [
            "Software Developer",
            "Data Analyst",
            "Data Engineer",
            "Web Developer",
            "Database Administrator",
            "Cybersecurity Analyst",
            "Cloud Engineer",
            "Machine Learning Engineer",
            "Systems Analyst",
            "IT Support Specialist",
        ]
        random.seed(seed)
        Faker.seed(seed)

    def get_positions(self):
        return self.positions

    def set_positions(self, positions):
        self.positions = positions

    def generate_employees(self, number_of_employees=50):
        employees = []

        for employee_id in range(1, number_of_employees + 1):
            employees.append(
                {
                    "employee_id": employee_id,
                    "name": self.fake.name(),
                    "position": random.choice(self.positions),
                    "start_date": self.fake.date_between(
                        start_date="-11y",
                        end_date="-2y",
                    ),
                    "salary": random.randint(60000, 200000),
                }
            )

        return pd.DataFrame(employees)

    def add_department_ids(self, employees_df):
        department_ids = [1, 2, 3, 4, 5]
        random.seed(self.seed)
        employees_df = employees_df.copy()
        employees_df["department_id"] = [
            random.choice(department_ids) for _ in range(len(employees_df))
        ]
        return employees_df

    def create_departments(self):
        return pd.DataFrame(
            {
                "department_id": [1, 2, 3, 4, 5],
                "department_name": [
                    "Software Development",
                    "Data & Analytics",
                    "Cybersecurity",
                    "Cloud & Infrastructure",
                    "IT Support",
                ],
                "location": [
                    "Toronto",
                    "Waterloo",
                    "Ottawa",
                    "Mississauga",
                    "Hamilton",
                ],
                "budget": [2500000, 2200000, 1800000, 2100000, 1500000],
            }
        )
