from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    """ Conexión a la base de datos """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Huevos123",
        database="db"
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Verificar si la tabla tiene datos
        cursor.execute('SELECT COUNT(*) FROM students')
        count = cursor.fetchone()[0]

        if count == 0:
            print("⚠️ No hay datos, insertando registros...")
            cursor.execute("INSERT INTO students (name, age) VALUES ('Juan Pérez', 20), ('María López', 22)")
            conn.commit()  # Guardar cambios

        # Obtener los datos después de la inserción
        cursor.execute('SELECT * FROM students')
        result = cursor.fetchall()

        cursor.close()
        conn.close()

        print(f"📊 Datos obtenidos de MySQL: {result}")

    except mysql.connector.Error as err:
        print(f"❌ Error conectando a MySQL: {err}")
        result = []  

    return render_template('index.html', students=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
