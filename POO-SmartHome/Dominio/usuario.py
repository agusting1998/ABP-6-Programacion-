from connection import get_connection

class Usuario:
    def __init__(self, nombre, passw, rol, email=None):
        self.nombre = nombre
        self.passw = passw
        self.rol = rol
        self.email = email if email else f"{nombre}@smarthome.com"

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

    def registrar_usuario(self, nombre, passw, rol, email=None):
        usuario = Usuario(nombre, passw, rol, email)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Usuario (email, nombre, passw, rol) VALUES (%s, %s, %s, %s)",
            (usuario.email, nombre, passw, rol)
        )
        conn.commit()
        conn.close()
        self.usuarios[nombre] = usuario
        print(f"Usuario {nombre} registrado como {rol}.")

    def iniciar_sesion(self, nombre, passw):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, passw, rol, email FROM Usuario WHERE nombre=%s", (nombre,))
        row = cursor.fetchone()
        conn.close()
        if row and row[1] == passw:
            usuario_obj = Usuario(row[0], row[1], row[2], row[3])
            self.usuarios[nombre] = usuario_obj
            print(f"Bienvenido, {nombre}.")
            return usuario_obj
        print("Usuario o contraseña incorrectos.")
        return None
