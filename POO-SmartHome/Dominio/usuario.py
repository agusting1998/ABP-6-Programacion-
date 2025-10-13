import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Conn'))
from db_conn import get_connection

class Usuario:
    def __init__(self, nombre, passw, rol, email):
        self.nombre = nombre
        self.passw = passw
        self.rol = rol
        self.email = email
        self.dispositivos = [] 

    def consultar_datos_personales(self):
        print(f"\nDatos de {self.nombre}:")
        print(f"- Rol: {self.rol}")
        print(f"- Email: {self.email}")
        print(f"- Dispositivos registrados: {len(self.dispositivos)}")

    def modificar_rol(self, nuevo_rol):
        self.rol = nuevo_rol

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Usuario SET rol=%s WHERE email=%s", (nuevo_rol, self.email))
            conn.commit()
            conn.close()
        except Exception as e:
            pass 

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

        print(f"Usuario {nombre} registrado con éxito como {rol}") 
        return usuario

    def iniciar_sesion(self, email, passw):
        usuario_obj = self.usuarios.get(email) 
        
        if usuario_obj and usuario_obj.passw == passw:
            print(f"Bienvenido, {usuario_obj.nombre}.") 
            return usuario_obj

        print("Usuario o contraseña incorrectos.") 
        return None

    def modificar_rol(self, email, nuevo_rol):
        usuario_obj = self.usuarios.get(email)
        if usuario_obj:
            usuario_obj.modificar_rol(nuevo_rol)
        else:
            print("Usuario no encontrado.")

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.") 
            return
            
        for u in self.usuarios.values():
            print(f"- {u.nombre} | {u.email} | {u.rol}")
