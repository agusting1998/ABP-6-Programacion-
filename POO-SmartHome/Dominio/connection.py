import sqlite3
import os

# Ruta absoluta a la base de datos SQLite
DB_PATH = os.path.join(os.path.dirname(__file__), '../../BD-Evidencia-5/database.db')

def get_connection():
    """
    Devuelve una conexión a la base de datos SQLite.
    La conexión usa row_factory para permitir acceder a columnas por nombre.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
