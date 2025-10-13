import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Dominio'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Conn'))

from conn.db_conn import get_connection
from usuario import Usuario

class UsuarioDAO:
    def crear(self, email, nombre, password, rol="estandar"):
        conn = get_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Usuario (email, nombre, password, rol) VALUES (%s, %s, %s, %s)",
            (email, nombre, password, rol)
        )
        conn.commit()
        conn.close()
        return Usuario(email, nombre, password, rol)

    def buscar_por_email(self, email):
        conn = get_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        cursor.execute(
            "SELECT email, nombre, password, rol FROM Usuario WHERE email=%s",
            (email,)
        )
        row = cursor.fetchone()
        conn.close()
        if row:
            return Usuario(row[0], row[1], row[2], row[3])
        return None

    def listar_todos(self):
        conn = get_connection()
        if not conn:
            return []
        cursor = conn.cursor()
        cursor.execute("SELECT email, nombre, password, rol FROM Usuario")
        rows = cursor.fetchall()
        conn.close()
        usuarios = []
        for r in rows:
            usuarios.append(Usuario(r[0], r[1], r[2], r[3]))
        return usuarios
