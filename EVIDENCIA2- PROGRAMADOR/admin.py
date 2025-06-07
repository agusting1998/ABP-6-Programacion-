import main
import usuario

usuarios = {
    "usuario1": "contraseña123",
    "usuario2": "abc123",
    "admin": "admin123"
}

def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    usuario_nombre = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
    # Verificar credenciales
    if usuario_nombre in usuarios and usuarios[usuario_nombre] == contraseña:
        print(f"¡Bienvenido, {usuario_nombre}!")
        main.menu()
    else:
        print("Usuario o contraseña incorrectos.")

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión")
        print("2. Registro")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            print("\n--- Registro de Usuario ---")
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            email = input("Ingrese su email: ")
            usuario.registrar_usuario_estandar(nombre, apellido, email)
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
