import usuario
import dispositivo
import automatizacion
from data import USUARIOS

def menu_estandar(usuario_data):
    """
    Menú de opciones para un usuario estándar.
    """
    nombre_usuario = list(USUARIOS.keys())[list(USUARIOS.values()).index(usuario_data)]
    while True:
        print(f"\n--- Menú de Usuario Estándar ({nombre_usuario}) ---")
        print("1. Consultar mis datos personales")
        print("2. Consultar mis dispositivos")
        print("3. Activar 'Modo Ahorro de Energía'")
        print("4. Cerrar Sesión")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            usuario.consultar_datos_personales(nombre_usuario)
        elif opcion == '2':
            dispositivo.listar_dispositivos(nombre_usuario)
        elif opcion == '3':
            automatizacion.modo_ahorro_energia(nombre_usuario)
        elif opcion == '4':
            print(" Sesión cerrada.")
            break
        else:
            print(" Opción inválida. Inténtalo de nuevo.")

def menu_admin(usuario_data):
    """
    Menú de opciones para un usuario administrador.
    """
    nombre_usuario = list(USUARIOS.keys())[list(USUARIOS.values()).index(usuario_data)]
    while True:
        print(f"\n--- Menú de Administrador ({nombre_usuario}) ---")
        print("1. Gestionar dispositivos")
        print("2. Consultar automatizaciones activas")
        print("3. Modificar rol de un usuario")
        print("4. Cerrar Sesión")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            menu_gestion_dispositivos(nombre_usuario)
        elif opcion == '2':
            automatizacion.consultar_automatizaciones_activas()
        elif opcion == '3':
            nombre_target = input("Ingresa el nombre del usuario a modificar: ")
            nuevo_rol = input("Ingresa el nuevo rol ('admin' o 'estandar'): ").lower()
            usuario.modificar_rol_usuario(nombre_target, nuevo_rol)
        elif opcion == '4':
            print(" Sesión cerrada.")
            break
        else:
            print(" Opción inválida. Inténtalo de nuevo.")

def menu_gestion_dispositivos(nombre_usuario):
    """
    Sub-menú para gestionar dispositivos, accesible solo para el administrador.
    """
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
            dispositivo.agregar_dispositivo(nombre_usuario, nombre_disp, tipo_disp)
        elif opcion == '2':
            dispositivo.listar_dispositivos(nombre_usuario)
        elif opcion == '3':
            try:
                dispositivo_id = int(input("ID del dispositivo a eliminar: "))
                dispositivo.eliminar_dispositivo(nombre_usuario, dispositivo_id)
            except ValueError:
                print(" Entrada inválida. El ID debe ser un número.")
        elif opcion == '4':
            try:
                dispositivo_id = int(input("ID del dispositivo a cambiar: "))
                nuevo_estado = input("Nuevo estado (encendido/apagado): ").lower()
                if nuevo_estado in ['encendido', 'apagado']:
                    dispositivo.cambiar_estado_dispositivo(nombre_usuario, dispositivo_id, nuevo_estado)
                else:
                    print(" Estado inválido. Usa 'encendido' o 'apagado'.")
            except ValueError:
                print(" Entrada inválida. El ID debe ser un número.")
        elif opcion == '5':
            break
        else:
            print(" Opción inválida. Inténtalo de nuevo.")

def main():
    """
    Función principal para la interfaz de línea de comandos.
    """
    while True:
        print("\n--- SmartHome Solutions ---")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Ingresa tu nombre de usuario: ")
            contrasena = input("Ingresa tu contraseña: ")
            usuario.registrar_usuario(nombre, contrasena)
        elif opcion == '2':
            nombre = input("Ingresa tu nombre de usuario: ")
            contrasena = input("Ingresa tu contraseña: ")
            usuario_data = usuario.iniciar_sesion(nombre, contrasena)
            if usuario_data:
                if usuario_data['rol'] == 'admin':
                    menu_admin(usuario_data)
                else:
                    menu_estandar(usuario_data)
        elif opcion == '3':
            print(" ¡Hasta luego!")
            break
        else:
            print(" Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()