usuarios = {
    "usuario1": "contraseña123",
    "usuario2": "abc123",
    "admin": "admin123"
}

def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
    # Verificar credenciales
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"¡Bienvenido, {usuario}!")
        return True  # Inicio de sesión exitoso
    else:
        print("Usuario o contraseña incorrectos.")
        return False  # Inicio de sesión fallido

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Iniciar sesión")
        print("2. Registro ")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            if iniciar_sesion():
                # Redirigir al usuario a otra parte del programa
                print("Acceso concedido a funciones adicionales...")
                break  # Salir del menú después de iniciar sesión
      
        elif opcion == "2":
             print("\n--- Registro de Usuario ---")
             nombre = input("Ingrese su nombre: ")
             apellido = input("Ingrese su apellido: ")
             email = input("Ingrese su email: ")
             usuarios.registrar_usuario_estandar(nombre, apellido, email)
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
