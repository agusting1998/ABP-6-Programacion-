#Registrar Usuario Estandar: Agustín Gallardo
usuarios_estandar = {}

#Realice Tres Funciones:

#Funcion de Registrar Usuarios
def registrar_usuario_estandar(nombre, apellido, email):
    if email in usuarios_estandar:
        print("Ya existe un usuario con ese email.")
    else:
        usuarios_estandar[email] = {
            "nombre": nombre,
            "apellido": apellido,
            "email": email
        }
        print(f"Usuario estándar registrado con éxito: {nombre} {apellido}")

#Funcion de Obtener los Usuarios Registrados
def obtener_usuarios_estandar():
    return usuarios_estandar


#Funcion de Consultar los Usuarios Registrados
def mostrar_usuarios_estandar():
    if not usuarios_estandar:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios estándar registrados: ")
        for usuario in usuarios_estandar.values():
            print(f"- {usuario['nombre']} {usuario['apellido']} ({usuario['email']})")
