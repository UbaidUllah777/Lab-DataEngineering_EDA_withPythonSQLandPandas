# Data Engineering and Exploratory Data Analysis

This project demonstrates an end-to-end data engineering and exploratory data analysis (EDA) workflow using synthetic employee data. The workflow combines Python, Pandas, Faker, PostgreSQL, and data visualization in a Jupyter notebook.

The project is designed for learning and demonstration purposes. All employee records are synthetic and do not represent real people.

## Project Objectives

- Generate realistic synthetic employee records with Faker
- Store employee data in a PostgreSQL database hosted on Neon
- Retrieve SQL data into a Pandas DataFrame
- Inspect and clean the dataset
- Create features such as `start_year` and `years_of_service`
- Scale salary values using Min-Max scaling
- Join employee data with department data
- Explore salary patterns using charts and a heatmap

## Project Files

| File | Description |
| --- | --- |
| `lab_data_engineering_eda.ipynb` | Main notebook containing the complete workflow |
| `requirements.txt` | Pinned Python dependencies for the project environment |
| `.env` | Local database connection configuration; do not commit this file |
| `.gitignore` | Excludes the virtual environment and secret configuration files |

## Technologies Used

- Python 3.13
- Jupyter Notebook
- Pandas and NumPy
- Faker
- PostgreSQL and `psycopg2`
- Matplotlib
- scikit-learn
- python-dotenv
- Neon cloud PostgreSQL

## Setup

### 1. Create or use the virtual environment

From the project directory, create a virtual environment if one does not already exist:

```bash
python -m venv .venv
```

Activate it in Git Bash:

```bash
source .venv/Scripts/activate
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

Install the pinned dependencies and the notebook-specific libraries:

```bash
python -m pip install -r requirements.txt 
```

Register the virtual environment as a Jupyter kernel:

```bash
python -m ipykernel install --user --name lab-data-engineering-eda --display-name "Python (.venv) - Lab Data Engineering EDA"
```

### 3. Configure the database connection

Create a `.env` file in the project root and add your PostgreSQL connection string:

```env
DATABASE_URL=postgresql://username:password@host/database?sslmode=require
```

Use your own Neon connection string. Never publish database credentials or commit `.env` to source control.

## Running the Notebook

1. Open `lab_data_engineering_eda.ipynb` in VS Code.
2. Select the kernel named `Python (.venv) - Lab Data Engineering EDA`.
3. Run the cells from top to bottom.
4. Confirm that the database connection succeeds before running the SQL cells.

The notebook creates 50 synthetic employee records, inserts them into the `employees` PostgreSQL table, and loads the data back into Pandas for analysis.

## Analysis Workflow

### Data generation and storage

Employee records include an ID, name, position, start date, and salary. The records are generated reproducibly using fixed Faker and random seeds, then stored in PostgreSQL.

### Data cleaning and transformation

The notebook checks data types, missing values, duplicate IDs, salary ranges, and date validity. It then derives the employee start year and estimated years of service.

### Salary scaling

Salary values are transformed to a range from 0 to 1 using `MinMaxScaler`.

### Visualizations

1. **Average Salary by Position and Start Year** compares average salaries across IT positions and hiring years.
2. **Average Salary by Department and Position** uses a joined employee and department dataset to compare salary patterns with a heatmap.

## Database Notes

The notebook uses `CREATE TABLE IF NOT EXISTS` and inserts records with conflict handling for existing employee IDs. This allows the notebook to be rerun without creating duplicate employee records for the same IDs.

The database connection remains open during the notebook session. When finished, close the cursor and connection with:

```python
cursor.close()
conn.close()
```

## Reproducibility

The synthetic data generation uses fixed random seeds, so repeated runs produce consistent generated values within the same workflow. The database must be available and the `DATABASE_URL` environment variable must be configured before running the database sections.

## Security

- Keep `.env` private.
- Do not paste database credentials into notebook cells.
- Use a separate development database for experimentation.
