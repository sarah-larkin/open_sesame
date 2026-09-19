# open_sesame

## Mini ETL Practice Project - JSON --> SQLite 

This is a small ETL pipeline to practice extracting JSON data from a public API. The data is extracted, nested structures are normalised, and the resulting tables are loaded into a relational SQLite database. 

## Features

- Extracts product data from the DummyJSON API (https://dummyjson.com/products)
- Normalises nested JSON fields into separate relational tables
- Loads all tables into a local SQLite database
- Uses a modular ETL structure (extract.py, transform.py, load.py)
- Stores configuration in a .env file (practice)
- Includes a Jupyter notebook for data exploration
- Mirrors real-world data engineering patterns

## Tech Stack 

Language & Runtime:
- Python 3.13 — core ETL logic
- pip / venv — dependency + environment management

Libraries:
- requests — API extraction
- pandas — transformation + normalisation
- sqlite3 — database connection
- python-dotenv — environment variable management
- loguru — logging
- pytest — unit testing

Storage:
- SQLite — lightweight relational database stored locally in /data/database.sqlite

Development Tools:
- VS Code — IDE
- Jupyter Notebooks — exploration + debugging
- Black / Isort — formatting
- Pylint — linting

API Source:
- DummyJSON — public API providing nested product data for ETL practice

## How to Run 

Clone the repo: 
```bash
git clone https://github.com/sarah-larkin/open_sesame.git
cd open_sesame 
```

set up the virtual environment 
```bash
python -m venv venv
source venv/bin/activate
```

install dependancies 
```bash
pip install -r requirements.txt
```

create .env file 
```bash 
API_URL=https://dummyjson.com/products
DB_PATH=data/database.sqlite
LOG_PATH=logs/etl.log
```

run the pipeline 
```bash
python src/main.py
```






