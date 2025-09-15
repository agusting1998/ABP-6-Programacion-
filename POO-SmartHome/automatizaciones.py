from data import USUARIOS

def modo_ahorro_energia(nombre_usuario):
    """
    Activa el Modo Ahorro de Energía, apagando todos los dispositivos no esenciales.
    """
    print("\n Activando Modo Ahorro de Energía...")
    if nombre_usuario in USUARIOS:
        dispositivos = USUARIOS[nombre_usuario]['dispositivos']
        dispositivos_apagados = 0
        for disp in dispositivos:
            if disp['tipo'] in ['luz', 'electrodomestico']:
                disp['estado'] = 'apagado'
                dispositivos_apagados += 1
                print(f"Apagando: {disp['nombre']} ({disp['tipo']})")
        
        print(f" Modo Ahorro de Energía activado. {dispositivos_apagados} dispositivos apagados.")
    else:
        print(" Error: Usuario no encontrado.")


def modo_noche(nombre_usuario):
    """
    Activa el Modo Noche:
    - Apaga luces
    - Apaga electrodomésticos
    - Enciende cámaras de seguridad
    """
    print("\n Activando Modo Noche...")
    if nombre_usuario in USUARIOS:
        dispositivos = USUARIOS[nombre_usuario]['dispositivos']
        luces_apagadas = 0
        electro_apagados = 0
        camaras_encendidas = 0

        for disp in dispositivos:
            if disp['tipo'] == 'luz':
                disp['estado'] = 'apagado'
                luces_apagadas += 1
                print(f"Apagando luz: {disp['nombre']}")
            elif disp['tipo'] == 'electrodomestico':
                disp['estado'] = 'apagado'
                electro_apagados += 1
                print(f"Apagando electrodoméstico: {disp['nombre']}")
            elif disp['tipo'] == 'cámara':
                disp['estado'] = 'encendido'
                camaras_encendidas += 1
                print(f"Encendiendo cámara de seguridad: {disp['nombre']}")

        print(f"\n Modo Noche activado. Luces apagadas: {luces_apagadas}, "
              f"Electrodomésticos apagados: {electro_apagados}, "
              f"Cámaras encendidas: {camaras_encendidas}.")
    else:
        print(" Error: Usuario no encontrado.")


def consultar_automatizaciones_activas():
    """
    Muestra una lista de las automatizaciones activas en el sistema.
    """
    print("\n--- Automatizaciones Activas ---")
    print("1. Modo Ahorro de Energía: Apaga todos los dispositivos no esenciales.")
    print("2. Modo Noche: Apaga luces y electrodomésticos, enciende cámaras de seguridad.")
    print("--------------------------------\n")
