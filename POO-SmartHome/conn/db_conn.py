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
            return conexion
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Diegojosem87

