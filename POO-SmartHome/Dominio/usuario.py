import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Conn'))
from conn.db_conn import get_connection

class Usuario:
    def __init__(self, nombre, passw, rol, email):
        self.nombre = nombre
        self.passw = passw
        self.rol = rol
        self.email = email

    def consultar_datos_personales(self):
        print(f"\nDatos de {self.nombre}:")
        print(f"- Rol: {self.rol}")
        print(f"- Email: {self.email}")

    def modificar_rol(self, nuevo_rol):
        self.rol = nuevo_rol
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Usuario SET rol=%s WHERE email=%s", (nuevo_rol, self.email))
        conn.commit()
        conn.close()
        print(f"Rol de {self.nombre} modificado a {nuevo_rol}.")


class GestorUsuarios:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, nombre, passw, rol, email):

        if email in self.usuarios:
            print("Error: El email ya existe en el sistema.")
            return None
        usuario = Usuario(nombre, passw, rol, email)
        self.usuarios[email] = usuario
        return usuario

    def iniciar_sesion(self, email, passw):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, passw, rol, email FROM Usuario WHERE email=%s", (email,))
        row = cursor.fetchone()
        conn.close()
        if row and row[1] == passw:
            usuario_obj = Usuario(row[0], row[1], row[2], row[3])
            self.usuarios[email] = usuario_obj
            print(f"Bienvenido, {usuario_obj.nombre}.")
            return usuario_obj
        print("Usuario o contraseña incorrectos.")
        return None
