import dispositivos

#Automatización elegida "Modo Noche", activa las camaras y apaga las luces
def modo_noche():
    for nombre, info in dispositivos.dispositivos.items():
        if info['tipo'] == 'luz':
            info['estado'] = 'apagado'
        elif info['tipo'] == 'cámara':
            info['estado'] = 'encendido'
    print("Modo noche activado: luces apagadas, cámaras encendidas.")