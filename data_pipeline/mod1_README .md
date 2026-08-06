# Data Pipeline

Overview

This module implements a data pipeline using the Titanic dataset. The pipeline demonstrates loading data from CSV, storing it in a SQL database, querying the data using SQL, merging datasets with Pandas, and performing basic data validation.

Features

- Load Titanic dataset
- Create SQLite database
- Store data in SQL tables
- Execute SQL queries
- Merge datasets using Pandas
- Validate merged data
- Display sample outputs

Project Structure

data_pipeline/
│── data_pipeline.ipynb
│── titanic.csv
│── titanic.db
│── README.md
│── requirements.txt

How to Run

1. Install the required packages:

pip install -r requirements.txt

2. Open the notebook:

jupyter notebook data_pipeline.ipynb

3. Run all notebook cells in order.

Pipeline Steps

1. Read the Titanic CSV file.
2. Create an SQLite database.
3. Insert the dataset into SQL tables.
4. Execute SQL queries.
5. Merge SQL and Pandas data.
6. Validate and display the final merged dataset.

Output

- SQLite database ("titanic.db")
- SQL query results
- Merged DataFrame
- Validation output
