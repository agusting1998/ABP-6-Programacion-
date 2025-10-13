from db_conn import get_connection
from usuario import Usuario
import os
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent / "Dominio"))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Conn'))


class UsuarioDAO:
    def agregar(self, usuario_obj: Usuario):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Usuario (email, nombre, passw, rol) VALUES (%s, %s, %s, %s)",
                (usuario_obj.email, usuario_obj.nombre,
                 usuario_obj.passw, usuario_obj.rol)
            )
            conn.commit()
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
        finally:
            conn.close()

    def obtener_por_email(self, email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT nombre, passw, rol, email FROM Usuario WHERE email=%s", (email,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Usuario(row[0], row[1], row[2], row[3])
        return None

    def actualizar_rol(self, usuario_obj: Usuario):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Usuario SET rol=%s WHERE email=%s",
            (usuario_obj.rol, usuario_obj.email)
        )
        conn.commit()
        conn.close()


    def eliminar(self, email):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Usuario WHERE email=%s", (email,))
        conn.commit()
        conn.close()
