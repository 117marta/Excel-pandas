import sqlite3 as sql
from flask import Flask, render_template


# Type query to database
SQL = 'SELECT * FROM "new_table"'


# Instance of Flask class
app = Flask(__name__)


# Function - executes sql query
def execute_sql(sql_code):
    try:
        cnx = sql.connect('my_database')
        print('Opened database successfully!')
        cursor = cnx.cursor()
        cursor.execute(sql_code)
        print('Query committed!')
        result = cursor.fetchall()
        return result
    except Exception as e:
        print('Connection error!', e)
    finally:
        cursor.close()
        cnx.close()


# Decorator - tells Flask what URL should trigger execute_sql function
@app.route('/', methods=['GET'])
def show_result():
    data = execute_sql(SQL)
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
