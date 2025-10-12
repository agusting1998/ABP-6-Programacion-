from connection import get_connection

class Usuario:
    def __init__(self, nombre, passw, rol, email=None):
        self.nombre = nombre
        self.passw = passw
        self.rol = rol
        self.dispositivos = []
        self.email = email if email else f"{nombre}@smarthome.com"

    def consultar_datos_personales(self):
        print(f"\nDatos de {self.nombre}:")
        print(f"- Rol: {self.rol}")
        print(f"- Dispositivos registrados: {len(self.dispositivos)}")

    def modificar_rol(self, nuevo_rol):
        self.rol = nuevo_rol
        print(f"Rol de {self.nombre} modificado a {nuevo_rol}.")
        # Persistir en DB
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Usuario SET rol=? WHERE email=?", (nuevo_rol, self.email))
        conn.commit()
        conn.close()


class GestorUsuarios:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, nombre, passw, rol, apellido=""):
        if nombre in self.usuarios:
            print("Ya existe un usuario con ese nombre.")
        else:
            usuario = Usuario(nombre, passw, rol)
            self.usuarios[nombre] = usuario
            print(f"Usuario {nombre} registrado con éxito como {rol}.")

            # Guardar en DB
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Usuario (email, nombre, apellido, passw, rol) VALUES (?, ?, ?, ?, ?)",
                (usuario.email, nombre, apellido, passw, rol)
            )
            conn.commit()
            conn.close()

    def iniciar_sesion(self, nombre, passw):
        usuario = self.usuarios.get(nombre)
        if usuario and usuario.passw == passw:
            print(f"Inicio de sesión exitoso. Bienvenido, {nombre}.")
            return usuario
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return None

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados:")
            for usuario in self.usuarios.values():
                print(f"- {usuario.nombre} (rol: {usuario.rol})")
