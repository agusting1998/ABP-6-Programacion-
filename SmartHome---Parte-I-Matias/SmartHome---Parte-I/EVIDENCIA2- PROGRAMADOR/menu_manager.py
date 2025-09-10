# Este módulo se encarga de la presentación de menús y la interacción con el usuario.

import dispositivos
import usuario
import automatizaciones
import admin # Necesario para llamar a las funciones de admin

def mostrar_menu_principal():
    """Muestra el menú principal de la aplicación."""
    while True:
        print("\n--- Menú Principal ---")
        print("A. Registrar usuario estándar")
        print("B. Registrar usuario admin")
        print("1. Gestionar Dispositivos (Acceso General)")
        print("2. Activar modo noche")
        print("3. Soporte")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").upper()

        if opcion == "A":
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            email = input("Ingrese su email: ")
            usuario.registrar_usuario_estandar(nombre, apellido, email)
            # Después de registrar, podríamos querer ir al menú de usuario estándar
            if email in usuario.obtener_usuarios(): # Verificar si el registro fue exitoso
                mostrar_menu_usuario_estandar(nombre)
        elif opcion == "B":
            admin.registrar_y_loguear_admin() # Esta función ya llama a mostrar_menu_admin_principal() internamente
        elif opcion == "1":
            mostrar_menu_gestion_dispositivos_general() # Nuevo menú de gestión de dispositivos para todos
        elif opcion == "2":
            automatizaciones.modo_noche()
        elif opcion == "3":
            import soporte # Importar aquí si no se usa en todo el módulo
            soporte.mostrar_ayuda()
        elif opcion == "0":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def mostrar_menu_admin_principal():
    """Muestra el menú principal para administradores."""
    while True:
        print("\n--- Menú Principal - Admin ---")
        print("A) Consultar automatizaciones activas")
        print("B) Gestionar dispositivos")
        print("C) Modificar rol de usuario")
        print("0) Volver al menú principal") # Cambiado para volver al menú principal general
        
        opcion = input("Seleccione una opción: ").upper()
        
        if opcion == "A":
           print("\nAutomatizaciones activas:")
           automatizaciones.modo_noche()
        elif opcion == "B":
            mostrar_menu_gestion_dispositivos_admin() # Llama al menú de gestión de dispositivos específico de admin
        elif opcion == "C":
            admin.modificar_rol_usuario() # La lógica de modificar rol sigue en admin.py
        elif opcion == "0":
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def mostrar_menu_gestion_dispositivos_admin():
    """Muestra el menú de gestión de dispositivos para administradores."""
    while True:
        print("\n--- Gestión de Dispositivos (Admin) ---")
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

def mostrar_menu_gestion_dispositivos_general():
    """Muestra un menú de gestión de dispositivos más limitado para usuarios generales."""
    while True:
        print("\n--- Gestión de Dispositivos (General) ---")
        print("1. Listar dispositivos")
        print("2. Ver estado de dispositivo")
        print("0. Volver al menú anterior")

        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            dispositivos.listar_dispositivos()
        elif opcion == "2":
            nombre = input("Nombre del dispositivo: ")
            dispositivos.ver_estado(nombre)
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")

def mostrar_menu_usuario_estandar(nombre_usuario):
    """Muestra el menú para usuarios estándar."""
    while True:
        print(f"\n--- Menú Usuario Estándar ({nombre_usuario}) ---")
        print("1. Consultar mis datos")
        print("2. Ejecutar automatización (Modo Noche)")
        print("3. Consultar estado de un dispositivo")
        print("0. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Datos personales:")
            usuario.mostrar_usuarios() # Esto muestra todos los usuarios, quizás quieras mostrar solo el del usuario logueado
        elif opcion == "2":
            automatizaciones.modo_noche()
        elif opcion == "3":
            # La función consultar_dispositivos_interactivo ya maneja su propio bucle y salida
            dispositivos.consultar_dispositivos_interactivo()
        elif opcion == "0":
            print("Cerrando sesión del usuario estándar.")
            break
        else:
            print("Opción inválida.")

