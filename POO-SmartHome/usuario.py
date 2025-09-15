from data import USUARIOS

def registrar_usuario(nombre, contrasena, rol="estandar"):
    """Registrar un usuario nuevo en el sistema."""
    if nombre in USUARIOS:
        print("Ya existe un usuario con ese nombre.")
    else:
        USUARIOS[nombre] = {
            "contrasena": contrasena,
            "rol": rol,
            "dispositivos": []
        }
        print(f"Usuario {nombre} registrado con éxito como {rol}.")

def iniciar_sesion(nombre, contrasena):
    """Iniciar sesión de un usuario. Retorna sus datos si la autenticación es correcta."""
    if nombre in USUARIOS and USUARIOS[nombre]["contrasena"] == contrasena:
        print(f"Inicio de sesión exitoso. Bienvenido, {nombre}.")
        return USUARIOS[nombre]
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        return None

def consultar_datos_personales(nombre_usuario):
    """Consultar los datos personales de un usuario."""
    if nombre_usuario in USUARIOS:
        datos = USUARIOS[nombre_usuario]
        print(f"\nDatos de {nombre_usuario}:")
        print(f"- Rol: {datos['rol']}")
        print(f"- Dispositivos registrados: {len(datos['dispositivos'])}")
    else:
        print(f"El usuario {nombre_usuario} no existe.")

def mostrar_usuarios():
    """Mostrar todos los usuarios registrados."""
    if not USUARIOS:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for nombre, datos in USUARIOS.items():
            print(f"- {nombre} (rol: {datos['rol']})")

def modificar_rol_usuario(nombre, nuevo_rol):
    """Modificar el rol de un usuario existente."""
    if nombre in USUARIOS:
        USUARIOS[nombre]["rol"] = nuevo_rol
        print(f"Rol de {nombre} modificado a {nuevo_rol}.")
    else:
        print(f"El usuario {nombre} no existe.")
