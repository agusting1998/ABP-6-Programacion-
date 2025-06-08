#Registrar Usuario Estandar: Agustín Gallardo

import dispositivos
import automatizaciones
usuarios = {}

#Realice Tres Funciones:

#Funcion de Registrar Usuarios
def registrar_usuario_estandar(nombre, apellido, email, rol="usuario"):
    if email in usuarios:
        print("Ya existe un usuario con ese email.")
    else:
        usuarios[email] = {
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "Rol": rol
        }
        print(f"Usuario estándar registrado con éxito: {nombre} {apellido} - Rol {rol}")

#Funcion de Obtener los Usuarios Registrados
def obtener_usuarios():
    return usuarios


#Funcion de Consultar los Usuarios Registrados
def mostrar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios estándar registrados: ")
        for usuario in usuarios.values():
            print(f"- {usuario['nombre']} {usuario['apellido']} ({usuario['email']})")

def modificar_rol(email, nuevo_rol):
    if email in usuarios:
        usuarios[email]["rol"] = nuevo_rol
        print("f Rol de {email} actualizado a '{nuevo_rol}.")
    else:
        print("Usuario no encontrado")

def menu_usuario_estandar(nombre):
    while True:
        print(f"\n--- Menú Usuario Estándar")
        print("1. Consultar datos")
        print("2. Ejecutar automatización")
        print("3. Consultar estado de un dispositivo")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Datos personales:")
            mostrar_usuarios()
        elif opcion == "2":
            automatizaciones.modo_noche()
        elif opcion == "3":
            nombre_disp = input("Ingrese el nombre del dispositivo: ")
            dispositivos.consultar_dispositivos_interactivo()
        elif opcion == "0":
            print("Cerrando sesión del usuario estándar...")
            break
        else:
            print("Opción inválida.")   