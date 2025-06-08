# Inicio de Sesión, Rol Asignado a: Yazmin Orellana

import dispositivos
import usuario
import automatizaciones

usuarios_admin = {}


def registrar_y_loguear_admin():
    print("\n--- Registro de Administrador ---")
    usuario_nombre = input("Creá un nombre de usuario: ")
    contraseña = input("Creá una contraseña: ")

    if usuario_nombre in usuarios_admin:
        print("Este usuario ya está registrado.")
        return

    # Registrar al nuevo admin
    usuarios_admin[usuario_nombre] = contraseña
    print(f"Administrador {usuario_nombre} registrado exitosamente.")

    # Iniciar sesión automáticamente
    print("\n--- Inicio de Sesión - Admin ---")
    if usuario_nombre in usuarios_admin and usuarios_admin[usuario_nombre] == contraseña:
        print(f"¡Bienvenido, {usuario_nombre}!")
        menu_principal()  # Mostramos menú directamente
    else:
        print("Error al iniciar sesión.")

def gestionar_dispositivos():
    while True:
        print("\n Gestión de Dispositivos")
        print("1. Agregar dispositivo")
        print("2. Eliminar dispositivo")
        print("3. Listar dispositivos")
        print("4. Buscar dispositivo")
        print("5. Cambiar estado de dispositivo")
        print("6. Ver estado de dispositivo")
        print("0. Volver al menú anterior")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            nombre = input("Nombre del dispositivo: ")
            tipo = input("Tipo de dispositivo (luz, cámara, electrodoméstico): ")
            estado = input("Estado inicial (encendido/apagado): ")
            dispositivos.agregar_dispositivo(nombre, tipo, estado)

        elif opcion == "2":
            nombre = input("Nombre del dispositivo a eliminar: ")
            dispositivos.eliminar_dispositivo(nombre)

        elif opcion == "3":
            dispositivos.listar_dispositivos()

        elif opcion == "4":
            nombre = input("Nombre del dispositivo a buscar: ")
            resultado = dispositivos.buscar_dispositivo(nombre)
            if resultado:
                print(f"Dispositivo encontrado: {nombre} - Tipo: {resultado['tipo']}, Estado: {resultado['estado']}")
            else:
                print("Dispositivo no encontrado.")

        elif opcion == "5":
            nombre = input("Nombre del dispositivo: ")
            nuevo_estado = input("Nuevo estado (encendido/apagado): ")
            dispositivos.cambiar_estado(nombre, nuevo_estado)

        elif opcion == "6":
            nombre = input("Nombre del dispositivo: ")
            dispositivos.ver_estado(nombre)

        elif opcion == "0":
            break
        else:
            print("Opción no válida.")


def modificar_rol_usuario():
    print("n\ Modificar rol del usuario")

    usuarios_actuales = usuario.obtener_usuarios()

    if not usuarios_actuales:
        print("No hay usuarios registrados...")
        return
        print("\nUsuarios registrados:")
    for email, datos in usuarios_actuales.items():
        if "rol" not in datos:
            datos["rol"] = "usuario"
        print(f" - {email}: {datos['nombre']} {datos['apellido']} - rol actual -> {datos['rol']}")

    email_usuario = input("\nIngrese el email del usuario a modificar: ")

    if email_usuario not in usuarios_actuales:
        print("Ese usuario no existe.")
        return

    nuevo_rol = input("Ingrese el nuevo rol (usuario/admin): ").lower()
    if nuevo_rol not in {"usuario", "admin"}:
        print("Rol no válido. Debe ser 'usuario' o 'admin'.")
        return

    usuario.modificar_rol(email_usuario, nuevo_rol)


def menu_principal():
    while True:
        print("\n--- Menú Principal - Admin ---")
        print("A) Consultar automatizaciones activas")
        print("B) Gestionar dispositivos")
        print("C) Modificar rol de usuario")
        print("0) Salir")
        
        opcion = input("Seleccione una opción: ").upper()
        
        if opcion == "A":
           print("\nAutomatizaciones activas:")
           automatizaciones.modo_noche()
        elif opcion == "B":
            gestionar_dispositivos()
        elif opcion == "C":
            modificar_rol_usuario()
        elif opcion == "0":
            print("Saliendo del menú de administración.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
