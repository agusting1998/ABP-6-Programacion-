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
        opcion = input("Elige una opción: ").strip()

        if opcion == '1':
            usuario_obj.consultar_datos_personales()
        elif opcion == '2':
            listar_dispositivos(usuario_obj)
        elif opcion == '3':
            control_automatizaciones.modo_ahorro_energia(usuario_obj)
        elif opcion == '4':
            print("Sesión cerrada exitosamente.")
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
        opcion = input("Elige una opción: ").strip()

        if opcion == '1':
            menu_gestion_dispositivos(usuario_obj)
        elif opcion == '2':
            consultar_automatizaciones_activas()
        elif opcion == '3':
            email_target = input("Email del usuario: ").strip()
            if not email_target:
                print("El email no puede estar vacío.")
                continue
            nuevo_rol = input("Nuevo rol (admin/usuario): ").strip().lower()
            if nuevo_rol not in ["admin", "usuario"]:
                print("Rol inválido. Use 'admin' o 'usuario'.")
                continue
            target = gestor.usuarios.get(email_target)
            if target:
                target.modificar_rol(nuevo_rol)
                print(f"Rol de '{target.nombre}' actualizado a '{nuevo_rol}'.")
            else:
                print("Usuario no encontrado.")
        elif opcion == '4':
            print("Sesión cerrada exitosamente.")
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
        opcion = input("Elige opción: ").strip()

        if opcion == '1':
            nombre = input("Nombre dispositivo: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            tipo = input("Tipo (luz/electrodoméstico/cámara/sensor/cerradura): ").strip()
            if not tipo:
                print("El tipo no puede estar vacío.")
                continue
            resultado = agregar_dispositivo(usuario_obj.email, nombre, tipo)
            if resultado:
                print(f"Dispositivo '{nombre}' registrado correctamente.")
            else:
                print("Error al registrar el dispositivo.")
                
        elif opcion == '2':
            listar_dispositivos(usuario_obj)
            
        elif opcion == '3':
            nombre = input("Nombre dispositivo: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            estado = input("Nuevo estado (encendido/apagado): ").strip().lower()
            if estado not in ["encendido", "apagado"]:
                print("Estado inválido. Use 'encendido' o 'apagado'.")
                continue
            cambiar_estado(usuario_obj, nombre, estado)
            
        elif opcion == '4':
            nombre = input("Nombre dispositivo: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            confirmar = input(f"¿Deseas eliminar '{nombre}'? (s/n): ").strip().lower()
            if confirmar == 's':
                eliminar_dispositivo(usuario_obj, nombre)
                print("Dispositivo eliminado.")
            else:
                print("Operación cancelada.")
                
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
        opcion = input("Elige opción: ").strip()

        if opcion == "1":
            email = input("Email: ").strip()
            if not email:
                print("El email no puede estar vacío.")
                continue
            passw = input("Contraseña: ").strip()
            if not passw:
                print("La contraseña no puede estar vacía.")
                continue
            usuario_obj = gestor.iniciar_sesion(email, passw)
            if usuario_obj:
                if usuario_obj.rol == "admin":
                    menu_admin(usuario_obj)
                else:
                    menu_estandar(usuario_obj)
            else:
                print("Email o contraseña incorrectos.")

        elif opcion == "2":
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            apellido = input("Apellido: ").strip()
            if not apellido:
                print("El apellido no puede estar vacío.")
                continue
            passw = input("Contraseña: ").strip()
            if not passw:
                print("La contraseña no puede estar vacía.")
                continue
            rol = input("Rol ('admin' o 'usuario'): ").strip().lower()
            if rol not in ["admin", "usuario"]:
                print("Rol inválido. Use 'admin' o 'usuario'.")
                continue
            email = input("Email único: ").strip()
            if not email:
                print("El email no puede estar vacío.")
                continue
            nuevo_usuario = gestor.registrar_usuario(nombre, passw, rol, email)
            if nuevo_usuario:
                usuario_dao.agregar(nuevo_usuario)
                print(f"Usuario '{nombre}' registrado correctamente como {rol}.")
            else:
                print("No se pudo registrar el usuario. El email puede estar duplicado.")

        elif opcion == "0":
            print("Gracias por usar Smart Home. Hasta luego!")
            break
        
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()
