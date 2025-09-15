from data import USUARIOS

def registrar_usuario(nombre_usuario, contrasena):
    """
    Registra un nuevo usuario en la base de datos y le asigna un rol.
    """
    if nombre_usuario in USUARIOS:
        print("Error: El nombre de usuario ya existe.")
        return False
    
    # El primer usuario registrado es el admin, los demás son estándar.
    rol = 'admin' if not USUARIOS else 'estandar'
    
    USUARIOS[nombre_usuario] = {'contrasena': contrasena, 'rol': rol, 'dispositivos': []}
    print(f" Usuario '{nombre_usuario}' registrado exitosamente con el rol '{rol}'.")
    return True

def iniciar_sesion(nombre_usuario, contrasena):
    """
    Verifica las credenciales del usuario y retorna sus datos completos.
    """
    if nombre_usuario in USUARIOS and USUARIOS[nombre_usuario]['contrasena'] == contrasena:
        print(f" ¡Bienvenido, {nombre_usuario}!")
        return USUARIOS[nombre_usuario]
    else:
        print("Error: Usuario o contraseña incorrectos.")
        return None

def consultar_datos_personales(nombre_usuario):
    """
    Muestra los datos del usuario actual.
    """
    if nombre_usuario in USUARIOS:
        usuario = USUARIOS[nombre_usuario]
        print("\n--- Tus Datos Personales ---")
        print(f" Usuario: {nombre_usuario}")
        print(f" Rol: {usuario['rol']}")
        print(f" Dispositivos registrados: {len(usuario['dispositivos'])}")
        print("----------------------------\n")

def modificar_rol_usuario(nombre_usuario, nuevo_rol):
    """
    Permite al administrador cambiar el rol de otro usuario.
    """
    if nombre_usuario in USUARIOS:
        if nuevo_rol not in ['admin', 'estandar']:
            print(" Rol inválido. Usa 'admin' o 'estandar'.")
            return False
        
        USUARIOS[nombre_usuario]['rol'] = nuevo_rol
        print(f" Rol del usuario '{nombre_usuario}' modificado a '{nuevo_rol}'.")
        return True
    else:
        print(f" Error: Usuario '{nombre_usuario}' no encontrado.")
        return False