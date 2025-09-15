from data import USUARIOS, USUARIOS_ADMIN

def registrar_admin(nombre, contrasena):
    """Registrar un administrador."""
    if nombre in USUARIOS_ADMIN:
        print("Ya existe un administrador con ese nombre.")
    else:
        USUARIOS_ADMIN[nombre] = contrasena
        print(f"Administrador {nombre} registrado con éxito.")

def mostrar_admins():
    """Mostrar todos los administradores registrados."""
    if not USUARIOS_ADMIN:
        print("No hay administradores registrados.")
    else:
        print("Administradores registrados:")
        for nombre in USUARIOS_ADMIN:
            print(f"- {nombre}")
