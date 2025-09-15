
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
            # Los dispositivos no esenciales (luz, electrodomestico) se apagan.
            if disp['tipo'] in ['luz', 'electrodomestico']:
                disp['estado'] = 'apagado'
                dispositivos_apagados += 1
                print(f"🔌 Apagando: {disp['nombre']} ({disp['tipo']})")
        
        print(f" Modo Ahorro de Energía activado. {dispositivos_apagados} dispositivos apagados.")
    else:
        print(" Error: Usuario no encontrado.")

def consultar_automatizaciones_activas():
    """
    Muestra una lista de las automatizaciones activas en el sistema.
    """
    print("\n--- Automatizaciones Activas ---")
    print("1. Modo Ahorro de Energía: Apaga todos los dispositivos no esenciales.")
    print("--------------------------------\n")
