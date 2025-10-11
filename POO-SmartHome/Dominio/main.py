from usuario import GestorUsuarios
import menu_manager

gestor = GestorUsuarios()  # Gestor de todos los usuarios


def main():
    while True:
        print("\n--- SmartHome Solutions ---")
        print("1. Registrarse como estándar")
        print("2. Registrarse como administrador")
        print("3. Iniciar Sesión")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nombre = input("Ingresa tu nombre de usuario: ")
            contrasena = input("Ingresa tu contraseña: ")
            gestor.registrar_usuario(nombre, contrasena, rol='estandar')

        elif opcion == '2':
            nombre_admin = input("Ingresa tu nombre de usuario: ")
            contrasena = input("Ingresa tu contraseña: ")
            gestor.registrar_usuario(nombre_admin, contrasena, rol='admin')

        elif opcion == '3':
            nombre = input("Ingresa tu nombre de usuario: ")
            contrasena = input("Ingresa tu contraseña: ")
            usuario_obj = gestor.iniciar_sesion(nombre, contrasena)

            if usuario_obj:
                if usuario_obj.rol == 'admin':
                    menu_manager.menu_admin(usuario_obj)
                else:
                    menu_manager.menu_estandar(usuario_obj)

        elif opcion == '4':
            print(" ¡Hasta luego!")
            break
        else:
            print(" Opción inválida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()
