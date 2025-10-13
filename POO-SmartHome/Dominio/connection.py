import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conexion = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='1234',
            database='hogar_inteligente' 
        )
        if conexion.is_connected():
            print("Conexión exitosa a MySQL")
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def usar_schema_hogar_inteligente():
    conexion = get_connection()
    if not conexion:
        return

    cursor = conexion.cursor()


    cursor.execute("USE hogar_inteligente;")
    print("Schema 'hogar_inteligente' seleccionado.")


    cursor.execute("SHOW TABLES;")
    tablas = cursor.fetchall()
    print("Tablas en hogar_inteligente:", tablas)

    cursor.close()
    conexion.close()
    print("Conexión cerrada.")

if __name__ == "__main__":
    usar_schema_hogar_inteligente()
