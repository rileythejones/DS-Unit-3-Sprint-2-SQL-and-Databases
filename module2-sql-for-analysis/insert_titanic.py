import pandas as pd
import psycopg2
from sqlalchemy import create_engine 
import io 

from dotenv import load_dotenv
from pathlib import Path  
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


df = pd.read_csv('titanic.csv')
dbname = DBNAME
user = USER
password = PASSWORD
host = HOST
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
pg_curs = pg_conn.cursor()
pg_curs.execute("""CREATE TABLE titanic_table (
    survived BOOLEAN,
    pclass SMALLINT, 
    name VARCHAR,
    sex BOOLEAN, 
    age SMALLINT,
    siblings_spouses_aboard SMALLINT,
    parents_children_aboard SMALLINT,
    fare FLOAT
)""")
pg_curs.close()
pg_conn.commit()
engine = create_engine(URL)
df.to_sql('titanic_table', engine)