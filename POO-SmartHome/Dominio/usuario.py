# usuario.py

class Usuario:
    def __init__(self, nombre, contrasena, rol):
        self.nombre = nombre
        self.contrasena = contrasena
        self.rol = rol
        self.dispositivos = []

    def consultar_datos_personales(self):
        """Consultar los datos personales de este usuario."""
        print(f"\nDatos de {self.nombre}:")
        print(f"- Rol: {self.rol}")
        print(f"- Dispositivos registrados: {len(self.dispositivos)}")

    def modificar_rol(self, nuevo_rol):
        """Modificar el rol de este usuario."""
        self.rol = nuevo_rol
        print(f"Rol de {self.nombre} modificado a {nuevo_rol}.")


class GestorUsuarios:
    """Clase que gestiona todos los usuarios."""
    def __init__(self):
        self.usuarios = {}  # diccionario {nombre: objeto Usuario}

    def registrar_usuario(self, nombre, contrasena, rol):
        if nombre in self.usuarios:
            print("Ya existe un usuario con ese nombre.")
        else:
            usuario = Usuario(nombre, contrasena, rol)
            self.usuarios[nombre] = usuario
            print(f"Usuario {nombre} registrado con éxito como {rol}.")
            
    def registrar_usuario_admin(self, nombre, contrasena, rol='admin'):
        if nombre in self.usuarios:
            print("Ya existe un admin con ese nombre.")
        else:
            usuario = Usuario(nombre, contrasena, rol)
            self.usuarios[nombre] = usuario
            print(f"Usuario {nombre} registrado con éxito como {rol}.")

    def iniciar_sesion(self, nombre, contrasena):
        usuario = self.usuarios.get(nombre)
        if usuario and usuario.contrasena == contrasena:
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
