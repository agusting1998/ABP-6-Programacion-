import os
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent / "Dominio"))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Conn'))
from usuario import Usuario
from db_conn import get_connection
from idao import IDAO

class UsuarioDAO(IDAO):
    def agregar(self, usuario_obj: Usuario):
        conn = get_connection()
        if not conn:
            print("No se pudo conectar a la base de datos.")
            return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Usuario (email, nombre, apellido, passw, rol) VALUES (%s, %s, %s, %s, %s)",
                (usuario_obj.email, usuario_obj.nombre, "Apellido", usuario_obj.passw, usuario_obj.rol)
            )
            conn.commit()
            print(f"Usuario '{usuario_obj.nombre}' registrado exitosamente con rol '{usuario_obj.rol}'.")
        except Exception as e:
            print(f"Error al agregar usuario: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def obtener(self, email):
        """Obtiene un usuario por email"""
        return self.obtener_por_email(email)

    def obtener_por_email(self, email):
        conn = get_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT nombre, passw, rol, email FROM Usuario WHERE email=%s", (email,))
            row = cursor.fetchone()
            if row:
                return Usuario(row[0], row[1], row[2], row[3])
            return None
        finally:
            cursor.close()
            conn.close()

    def actualizar(self, usuario_obj: Usuario):
        """Actualiza un usuario existente"""
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE Usuario SET nombre=%s, passw=%s, rol=%s WHERE email=%s",
                (usuario_obj.nombre, usuario_obj.passw, usuario_obj.rol, usuario_obj.email)
            )
            conn.commit()
            print(f"Usuario '{usuario_obj.nombre}' actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def eliminar(self, email):
        """Elimina un usuario por email"""
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Usuario WHERE email=%s", (email,))
            conn.commit()
            print("Usuario eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def listar_todos(self):
        """Lista todos los usuarios"""
        conn = get_connection()
        if not conn:
            return []
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT nombre, passw, rol, email FROM Usuario")
            rows = cursor.fetchall()
            usuarios = []
            for row in rows:
                usuarios.append(Usuario(row[0], row[1], row[2], row[3]))
            return usuarios
        finally:
            cursor.close()
            conn.close()
