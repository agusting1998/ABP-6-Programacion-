# menu_manager.py

import dispositivos
from automatizaciones import control_automatizaciones, consultar_automatizaciones_activas
from connection import get_connection

# --- MENÚS ---

def menu_estandar(usuario_obj):
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
            control_automatizaciones.modo_ahorro_energia(usuario_obj)
        elif opcion == '4':
            print(" Sesión cerrada.")
            break
        else:
            print(" Opción inválida. Inténtalo de nuevo.")


def menu_admin(usuario_obj, gestor):
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
            consultar_automatizaciones_activas()
        elif opcion == '3':
            nombre_target = input("Ingresa el nombre del usuario a modificar: ")
            nuevo_rol = input("Ingresa el nuevo rol ('admin' o 'estandar'): ").lower()
            target = gestor.usuarios.get(nombre_target)
            if target:
                target.modificar_rol(nuevo_rol)
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE Usuario SET rol=? WHERE nombre=?",
                    (nuevo_rol, nombre_target)
                )
                conn.commit()
                conn.close()
            else:
                print(f"El usuario {nombre_target} no existe.")
        elif opcion == '4':
            print(" Sesión cerrada.")
            break
        else:
            print(" Opción inválida. Inténtalo de nuevo.")


def menu_gestion_dispositivos(usuario_obj):
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
            nuevo_disp = dispositivos.agregar_dispositivo(lista_dispositivos, nombre_disp, tipo_disp)
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT OR IGNORE INTO Dispositivo (nombre_dispositivo, tipo, estado) VALUES (?, ?, ?)",
                (nuevo_disp.nombre, nuevo_disp.tipo, nuevo_disp.estado)
            )
            cursor.execute(
                "INSERT OR IGNORE INTO Gestion (email_usuario, nombre_dispositivo) VALUES (?, ?)",
                (usuario_obj.email, nuevo_disp.nombre)
            )
            conn.commit()
            conn.close()

        elif opcion == '2':
            dispositivos.listar_dispositivos(lista_dispositivos)

        elif opcion == '3':
            try:
                dispositivo_id = int(input("ID del dispositivo a eliminar: "))
                disp_eliminado = None
                for d in lista_dispositivos:
                    if d.id == dispositivo_id:
                        disp_eliminado = d
                        break
                if dispositivos.eliminar_dispositivo(lista_dispositivos, dispositivo_id) and disp_eliminado:
                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.execute(
                        "DELETE FROM Gestion WHERE email_usuario=? AND nombre_dispositivo=?",
                        (usuario_obj.email, disp_eliminado.nombre)
                    )
                    cursor.execute(
                        "DELETE FROM Dispositivo WHERE nombre_dispositivo=?",
                        (disp_eliminado.nombre,)
                    )
                    conn.commit()
                    conn.close()
            except ValueError:
                print(" Entrada inválida. El ID debe ser un número.")

        elif opcion == '4':
            try:
                dispositivo_id = int(input("ID del dispositivo a cambiar: "))
                nuevo_estado = input("Nuevo estado (encendido/apagado): ").lower()
                if nuevo_estado in ['encendido', 'apagado']:
                    dispositivos.cambiar_estado(lista_dispositivos, dispositivo_id, nuevo_estado)
                    disp_actualizado = None
                    for d in lista_dispositivos:
                        if d.id == dispositivo_id:
                            disp_actualizado = d
                            break
                    if disp_actualizado:
                        conn = get_connection()
                        cursor = conn.cursor()
                        cursor.execute(
                            "UPDATE Dispositivo SET estado=? WHERE nombre_dispositivo=?",
                            (disp_actualizado.estado, disp_actualizado.nombre)
                        )
                        conn.commit()
                        conn.close()
                else:
                    print(" Estado inválido. Usa 'encendido' o 'apagado'.")
            except ValueError:
                print(" Entrada inválida. El ID debe ser un número.")

        elif opcion == '5':
            break
        else:
            print(" Opción inválida. Inténtalo de nuevo.")


# --- MENÚ PRINCIPAL ---

def menu_principal(gestor):
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Usuario: ")
            passw = input("Contraseña: ")
            usuario_obj = gestor.iniciar_sesion(nombre, passw)
            if usuario_obj:
                if usuario_obj.rol == "admin":
                    menu_admin(usuario_obj, gestor)
                else:
                    menu_estandar(usuario_obj)

        elif opcion == "2":
            nombre = input("Nombre: ")
            email = input("Email: ")
            passw = input("Contraseña: ")
            rol = input("Rol ('admin' o 'estandar'): ").lower()

            # Guardar usuario en gestor y DB
            gestor.registrar_usuario(nombre, passw, rol)

        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
