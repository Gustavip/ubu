from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    conn = mysql.connector.connect(
        host="mysql",
        user="root",
        password='root',
        database="db"
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', students=result)

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000,debug=True)