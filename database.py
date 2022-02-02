from main import concated_df
import sqlite3 as sql


# Specify the database and table name
DATABASE = 'my_database'
TABLE = 'new_table'


# Create database and fill it with data
try:
    conn = sql.connect(DATABASE)
    concated_df.to_sql(TABLE, con=conn, if_exists='replace', index=False)
    print('Database successfully filled with data!')
except Exception as e:
    print('Error!', e)
finally:
    conn.close()
