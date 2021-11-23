import os
import psycopg2
from dotenv import load_dotenv

CONN = None
TESTING_MODE = False

def setup():
    load_dotenv()

    
    # def connect():
        # global CONN

    DATABASE_URL = os.getenv('DATABASE_URL')
    try:
        
        print('PostgreSQL connection successful')
        return psycopg2.connect(DATABASE_URL, sslmode='require')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def query(sql, args=()):
    ''' query the database and get back rows selected/modified '''
    cur = CONN.cursor()
    try:
        cur.execute(sql, args)
    except Exception as e:
        print(type(e).__name__, e)
        raise e
    if cur.description is None:
        rows = []
    else:
        rows = cur.fetchall()
    if not TESTING_MODE:
        CONN.commit()
    cur.close()
    return rows
