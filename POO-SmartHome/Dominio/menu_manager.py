import os
import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent / "Dao"))

from usuario_dao import UsuarioDAO
from dispositivos import agregar_dispositivo, listar_dispositivos, cambiar_estado, eliminar_dispositivo
from automatizaciones import control_automatizaciones, consultar_automatizaciones_activas
from usuario import GestorUsuarios

usuario_dao = UsuarioDAO()
gestor = GestorUsuarios()

def menu_estandar(usuario_obj):
    while True:
        print(f"\n--- Menú Usuario Estándar ({usuario_obj.nombre}) ---")
        print("1. Consultar datos")
        print("2. Consultar dispositivos")
        print("3. Activar Modo Ahorro de Energía")
        print("4. Cerrar sesión")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            usuario_obj.consultar_datos_personales()
        elif opcion == '2':
            listar_dispositivos(usuario_obj)
        elif opcion == '3':
            control_automatizaciones.modo_ahorro_energia(usuario_obj)
        elif opcion == '4':
            break
        else:
            print("Opción inválida.")

def menu_admin(usuario_obj):
    while True:
        print(f"\n--- Menú Admin ({usuario_obj.nombre}) ---")
        print("1. Gestionar dispositivos")
        print("2. Consultar automatizaciones")
        print("3. Modificar rol usuario")
        print("4. Cerrar sesión")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            menu_gestion_dispositivos(usuario_obj)
        elif opcion == '2':
            consultar_automatizaciones_activas()
        elif opcion == '3':
            email_target = input("Email del usuario: ")
            nuevo_rol = input("Nuevo rol: ").lower()
            target = gestor.usuarios.get(email_target)
            if target:
                target.modificar_rol(nuevo_rol)
            else:
                print("Usuario no encontrado.")
        elif opcion == '4':
            break
        else:
            print("Opción inválida.") 

def menu_gestion_dispositivos(usuario_obj):
    while True:
        print("\n--- Gestión Dispositivos ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Cambiar estado dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Volver")
        opcion = input("Elige opción: ")

        if opcion == '1':
            nombre = input("Nombre dispositivo: ")
            tipo = input("Tipo: ")
            agregar_dispositivo(usuario_obj.email, nombre, tipo)
        elif opcion == '2':
            listar_dispositivos(usuario_obj)
        elif opcion == '3':
            nombre = input("Nombre dispositivo: ")
            estado = input("Nuevo estado: ")
            cambiar_estado(usuario_obj, nombre, estado)
        elif opcion == '4':
            nombre = input("Nombre dispositivo: ")
            eliminar_dispositivo(usuario_obj, nombre)
        elif opcion == '5':
            break
        else:
            print("Opción inválida.") 

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("0. Salir")
        opcion = input("Elige opción: ")

        if opcion == "1":
            email = input("Email: ")
            passw = input("Contraseña: ")
            usuario_obj = gestor.iniciar_sesion(email, passw)
            if usuario_obj:
                if usuario_obj.rol == "admin":
                    menu_admin(usuario_obj)
                else:
                    menu_estandar(usuario_obj)

        elif opcion == "2":
            nombre = input("Nombre: ")
            passw = input("Contraseña: ")
            rol = input("Rol ('admin' o 'estandar'): ").lower()
            email = input("Email único para este usuario: ")
            nuevo_usuario = gestor.registrar_usuario(nombre, passw, rol, email)
            if nuevo_usuario:
                usuario_dao.agregar(nuevo_usuario)
                print(f"Usuario {nombre} registrado como {rol}.")
            else:
                print("No se pudo registrar el usuario.")

        elif opcion == "0":
            break
        
        else:
            print("Opción inválida.") 

if __name__ == "__main__":
    menu_principal()
