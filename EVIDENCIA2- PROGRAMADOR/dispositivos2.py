# Diccionarios de datos
dispositivos = {}
usuarios = {
    "admin": {"password": "admin123", "rol": "admin", "datos": {"nombre": "Administrador"}}
}

# Registro de usuario estándar
def registrar_usuario():
    username = input("Ingrese nombre de usuario: ").strip()
    if username in usuarios:
        print("Usuario ya existe.")
        return
    password = input("Ingrese contraseña: ").strip()
    nombre = input("Ingrese su nombre: ").strip()
    usuarios[username] = {
        "password": password,
        "rol": "estandar",
        "datos": {"nombre": nombre}
    }
    print("Usuario registrado correctamente.")

# Inicio de sesión
def iniciar_sesion():
    username = input("Usuario: ").strip()
    password = input("Contraseña: ").strip()
    if username in usuarios and usuarios[username]["password"] == password:
        print(f"Inicio de sesión exitoso. Bienvenido, {usuarios[username]['datos']['nombre']}.")
        return username
    else:
        print("Usuario o contraseña incorrectos.")
        return None

# Funciones para dispositivos (solo admin)
def agregar_dispositivo(nombre, tipo, estado):
    if not nombre or not tipo or not estado:
        print("Todos los campos son obligatorios.")
        return
    if tipo not in {"luz", "camara", "electrodomestico"}:
        print("Tipo no válido. Use luz, cámara o electrodomestico.")
        return
    if estado not in {"encendido", "apagado"}:
        print("Estado no válido. Use encendido o apagado.")
        return
    if nombre in dispositivos:
        print("El dispositivo ya existe.")
        return
    dispositivos[nombre] = {"tipo": tipo, "estado": estado}
    print("Dispositivo agregado correctamente.")

def eliminar_dispositivo(nombre):
    if nombre in dispositivos:
        del dispositivos[nombre]
        print("Dispositivo eliminado correctamente.")
    else:
        print("Dispositivo no encontrado.")

def listar_dispositivos():
    if not dispositivos:
        print("No hay dispositivos registrados.")
        return
    for nombre, info in dispositivos.items():
        print(f"{nombre} - Tipo: {info['tipo']}, Estado: {info['estado']}")

# Menú para usuarios estándar
def menu_estandar(usuario):
    while True:
        print("\nMenú Usuario Estándar")
        print("1. Consultar datos personales")
        print("0. Cerrar sesión")
        opcion = input("Opción: ")

        if opcion == "1":
            print("Datos personales:")
            for clave, valor in usuarios[usuario]["datos"].items():
                print(f"{clave.capitalize()}: {valor}")
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

# Menú para administrador
def menu_admin():
    while True:
        print("\nMenú Administrador")
        print("1. Agregar dispositivo")
        print("2. Eliminar dispositivo")
        print("3. Listar dispositivos")
        print("0. Cerrar sesión")
        opcion = input("Opción: ")

        if opcion == "1":
            nombre = input("Nombre del dispositivo: ").strip()
            tipo = input("Tipo (luz/cámara/electrodoméstico): ").strip()
            estado = input("Estado (encendido/apagado): ").strip()
            agregar_dispositivo(nombre, tipo, estado)
        elif opcion == "2":
            nombre = input("Nombre del dispositivo a eliminar: ").strip()
            eliminar_dispositivo(nombre)
        elif opcion == "3":
            listar_dispositivos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")

# Menú principal
def menu_principal():
    while True:
        print("\n--- SmartHome ---")
        print("1. Iniciar sesión")
        print("2. Registrar nuevo usuario")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            usuario = iniciar_sesion()
            if usuario:
                if usuarios[usuario]["rol"] == "estandar":
                    menu_estandar(usuario)
                elif usuarios[usuario]["rol"] == "admin":
                    menu_admin()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "0":
            print("Fin del programa.")
            break
        else:
            print("Opción inválida.")

# Ejecutar programa
menu_principal()
