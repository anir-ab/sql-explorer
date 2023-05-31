from flask import Flask, render_template, request
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="explore"
)

app = Flask(__name__)

@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    return render_template('index.html', tables=tables)

@app.route('/query', methods=['POST'])
def query():
    query = request.form['query']
    cursor = db.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    return render_template('index.html', tables=tables, result=result, query=query)

if __name__ == '__main__':
    app.run(debug=True)
