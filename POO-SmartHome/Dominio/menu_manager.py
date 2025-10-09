# Este módulo se encarga de la presentación de menús y la interacción con el usuario.

import dispositivos
import usuario
import automatizaciones
from main import gestor  # Importamos el gestor de usuarios desde main.py

def menu_estandar(usuario_obj):
    """
    Menú de opciones para un usuario estándar.
    """
    while True:
        print(f"\n--- Menú de Usuario Estándar ({usuario_obj.nombre}) ---")
        print("1. Consultar mis datos personales")
        print("2. Consultar mis dispositivos")
        print("3. Activar 'Modo Ahorro de Energía'")
        print("4. Cerrar Sesión")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            usuario_obj.consultar_datos_personales()
        elif opcion == '2':
            dispositivos.listar_dispositivos(usuario_obj.dispositivos)
        elif opcion == '3':
            automatizaciones.modo_ahorro_energia(usuario_obj)
        elif opcion == '4':
            print(" Sesión cerrada.")
            break
        else:
            print(" Opción inválida. Inténtalo de nuevo.")

def menu_admin(usuario_obj):
    """
    Menú de opciones para un usuario administrador.
    """
    while True:
        print(f"\n--- Menú de Administrador ({usuario_obj.nombre}) ---")
        print("1. Gestionar dispositivos")
        print("2. Consultar automatizaciones activas")
        print("3. Modificar rol de un usuario")
        print("4. Cerrar Sesión")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            menu_gestion_dispositivos(usuario_obj)
        elif opcion == '2':
            automatizaciones.consultar_automatizaciones_activas()
        elif opcion == '3':
            nombre_target = input("Ingresa el nombre del usuario a modificar: ")
            nuevo_rol = input("Ingresa el nuevo rol ('admin' o 'estandar'): ").lower()
            target = gestor.usuarios.get(nombre_target)
            if target:
                target.modificar_rol(nuevo_rol)
            else:
                print(f"El usuario {nombre_target} no existe.")
        elif opcion == '4':
            print(" Sesión cerrada.")
            break
        else:
            print(" Opción inválida. Inténtalo de nuevo.")

def menu_gestion_dispositivos(usuario_obj):
    """
    Sub-menú para gestionar dispositivos (solo admin).
    """
    lista_dispositivos = usuario_obj.dispositivos

    while True:
        print("\n--- Sub-menú de Gestión de Dispositivos ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Eliminar dispositivo")
        print("4. Encender/Apagar dispositivo")
        print("5. Volver al menú de Administrador")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre_disp = input("Nombre del dispositivo: ")
            tipo_disp = input("Tipo (luz, termostato, camara, electrodomestico): ")
            dispositivos.agregar_dispositivo(lista_dispositivos, nombre_disp, tipo_disp)

        elif opcion == '2':
            dispositivos.listar_dispositivos(lista_dispositivos)

        elif opcion == '3':
            try:
                dispositivo_id = int(input("ID del dispositivo a eliminar: "))
                dispositivos.eliminar_dispositivo(lista_dispositivos, dispositivo_id)
            except ValueError:
                print(" Entrada inválida. El ID debe ser un número.")

        elif opcion == '4':
            try:
                dispositivo_id = int(input("ID del dispositivo a cambiar: "))
                nuevo_estado = input("Nuevo estado (encendido/apagado): ").lower()
                if nuevo_estado in ['encendido', 'apagado']:
                    dispositivos.cambiar_estado(lista_dispositivos, dispositivo_id, nuevo_estado)
                else:
                    print(" Estado inválido. Usa 'encendido' o 'apagado'.")
            except ValueError:
                print(" Entrada inválida. El ID debe ser un número.")

        elif opcion == '5':
            break
        else:
            print(" Opción inválida. Inténtalo de nuevo.")































# def mostrar_menu_principal():
#     """Muestra el menú principal de la aplicación."""
#     while True:
#         print("\n--- Menú Principal ---")
#         print("A. Registrar usuario estándar")
#         print("B. Registrar usuario admin")
#         print("1. Iniciar sesión")
#         print("2. Gestionar Dispositivos (Acceso General)")
#         print("3. Activar modo noche")
#         print("4. Soporte")
#         print("0. Salir")

#         opcion = input("Seleccione una opción: ").upper()

#         if opcion == "A":
#             nombre = input("Ingrese su nombre de usuario: ")
#             contrasena = input("Ingrese su contraseña: ")
#             usuario.registrar_usuario(nombre, contrasena, rol="estandar")

#         elif opcion == "B":
#             nombre = input("Ingrese su nombre de usuario admin: ")
#             contrasena = input("Ingrese su contraseña: ")
#             usuario.registrar_usuario(nombre, contrasena, rol="admin")

#         elif opcion == "1":
#             nombre = input("Usuario: ")
#             contrasena = input("Contraseña: ")
#             datos = usuario.iniciar_sesion(nombre, contrasena)
#             if datos:  # Si el login fue exitoso
#                 if datos["rol"] == "admin":
#                     mostrar_menu_admin_principal(nombre)
#                 else:
#                     mostrar_menu_usuario_estandar(nombre)

#         elif opcion == "2":
#             mostrar_menu_gestion_dispositivos_general()

#         elif opcion == "3":
#             # Para el modo noche general en el menú principal, pedimos usuario
#             nombre_usuario = input("Ingrese su nombre de usuario para activar Modo Noche: ")
#             automatizaciones.modo_noche(nombre_usuario)

#         elif opcion == "4":
#             import soporte
#             soporte.mostrar_ayuda()

#         elif opcion == "0":
#             print("Saliendo de la aplicación...")
#             break

#         else:
#             print("Opción inválida. Intente nuevamente.")


# def mostrar_menu_admin_principal(nombre_usuario):
#     """Muestra el menú principal para administradores."""
#     while True:
#         print("\n--- Menú Principal - Admin ---")
#         print("A) Consultar automatizaciones activas")
#         print("B) Gestionar dispositivos")
#         print("C) Modificar rol de usuario")
#         print("D) Ver usuarios registrados")
#         print("0) Volver al menú principal")

#         opcion = input("Seleccione una opción: ").upper()

#         if opcion == "A":
#             print("\nAutomatizaciones activas:")
#             # Modo noche para el admin actual
#             automatizaciones.modo_noche(nombre_usuario)

#         elif opcion == "B":
#             mostrar_menu_gestion_dispositivos_admin(nombre_usuario)

#         elif opcion == "C":
#             nombre = input("Usuario a modificar: ")
#             nuevo_rol = input("Nuevo rol: ")
#             usuario.modificar_rol_usuario(nombre, nuevo_rol)

#         elif opcion == "D":
#             usuario.mostrar_usuarios()

#         elif opcion == "0":
#             print("Volviendo al menú principal.")
#             break

#         else:
#             print("Opción no válida. Intente nuevamente.")


# def mostrar_menu_gestion_dispositivos_admin(nombre_usuario):
#     """Muestra el menú de gestión de dispositivos para administradores."""
#     while True:
#         print("\n--- Gestión de Dispositivos (Admin) ---")
#         print("1. Agregar dispositivo")
#         print("2. Eliminar dispositivo")
#         print("3. Listar dispositivos")
#         print("4. Buscar dispositivo")
#         print("5. Cambiar estado de dispositivo")
#         print("6. Ver estado de dispositivo")
#         print("0. Volver al menú anterior")

#         opcion = input("Seleccione una opcion: ")
#         if opcion == "1":
#             nombre_disp = input("Nombre del dispositivo: ")
#             tipo = input("Tipo de dispositivo (luz, cámara, electrodoméstico): ")
#             estado = input("Estado inicial (encendido/apagado): ")
#             dispositivos.agregar_dispositivo(nombre_usuario, nombre_disp, tipo, estado)
#         elif opcion == "2":
#             try:
#                 disp_id = int(input("ID del dispositivo a eliminar: "))
#                 dispositivos.eliminar_dispositivo(nombre_usuario, disp_id)
#             except ValueError:
#                 print("ID inválido.")
#         elif opcion == "3":
#             dispositivos.listar_dispositivos(nombre_usuario)
#         elif opcion == "4":
#             nombre_disp = input("Nombre del dispositivo a buscar: ")
#             dispositivos.buscar_dispositivo(nombre_usuario, nombre_disp)
#         elif opcion == "5":
#             try:
#                 disp_id = int(input("ID del dispositivo: "))
#                 nuevo_estado = input("Nuevo estado (encendido/apagado): ").lower()
#                 dispositivos.cambiar_estado(nombre_usuario, disp_id, nuevo_estado)
#             except ValueError:
#                 print("ID inválido.")
#         elif opcion == "6":
#             nombre_disp = input("Nombre del dispositivo: ")
#             dispositivos.ver_estado(nombre_usuario, nombre_disp)
#         elif opcion == "0":
#             break
#         else:
#             print("Opción no válida.")


# def mostrar_menu_gestion_dispositivos_general():
#     """Muestra un menú de gestión de dispositivos más limitado para usuarios generales."""
#     while True:
#         print("\n--- Gestión de Dispositivos (General) ---")
#         print("1. Listar dispositivos")
#         print("2. Ver estado de dispositivo")
#         print("0. Volver al menú anterior")

#         opcion = input("Seleccione una opcion: ")
#         if opcion == "1":
#             nombre_usuario = input("Ingrese su nombre de usuario: ")
#             dispositivos.listar_dispositivos(nombre_usuario)
#         elif opcion == "2":
#             nombre_usuario = input("Ingrese su nombre de usuario: ")
#             nombre_disp = input("Nombre del dispositivo: ")
#             dispositivos.ver_estado(nombre_usuario, nombre_disp)
#         elif opcion == "0":
#             break
#         else:
#             print("Opción no válida.")


# def mostrar_menu_usuario_estandar(nombre_usuario):
#     """Muestra el menú para usuarios estándar."""
#     while True:
#         print(f"\n--- Menú Usuario Estándar ({nombre_usuario}) ---")
#         print("1. Consultar mis datos")
#         print("2. Ejecutar automatización (Modo Noche)")
#         print("3. Consultar estado de un dispositivo")
#         print("0. Cerrar sesión")

#         opcion = input("Seleccione una opción: ")

#         if opcion == "1":
#             usuario.consultar_datos_personales(nombre_usuario)
#         elif opcion == "2":
#             automatizaciones.modo_noche(nombre_usuario)
#         elif opcion == "3":
#             nombre_usuario = input("Ingrese su nombre de usuario: ")
#             nombre_disp = input("Nombre del dispositivo: ")
#             dispositivos.ver_estado(nombre_usuario, nombre_disp)
#         elif opcion == "0":
#             print("Cerrando sesión del usuario estándar.")
#             break
#         else:
#             print("Opción inválida.")


if __name__ == "__main__":
    mostrar_menu_principal()
