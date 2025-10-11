class ControlAutomatizaciones:

    """Contiene la logica de todas las automatizaciones"""

    def __init__(self,):
        pass


    def modo_ahorro_energia(self, usuario_obj):
        """
            Activa el Modo Ahorro de Energía:
            Apaga todos los dispositivos que sean luces o electrodomésticos.
        """
        print("\n Activando Modo Ahorro de Energía...")

        dispositivos_apagados = 0
        for disp in usuario_obj.dispositivos:
            if disp.tipo in ['luz', 'electrodomestico']:
                if disp.estado == 'encendido':
                    disp.cambiar_estado('apagado')
                    dispositivos_apagados += 1
                    print(f"Apagando: {disp.nombre} ({disp.tipo})")

        print(f"\n Modo Ahorro de Energía activado. {dispositivos_apagados} dispositivos apagados.\n")


    def modo_noche(self, usuario_obj):
        """
             Activa el Modo Noche:
             - Apaga luces
             - Apaga electrodomésticos
             - Enciende cámaras de seguridad
        """
        print("\n Activando Modo Noche...")

        luces_apagadas = 0
        electro_apagados = 0
        camaras_encendidas = 0

        for disp in usuario_obj.dispositivos:
            if disp.tipo == 'luz' and disp.estado != 'apagado':
                disp.cambiar_estado('apagado')
                luces_apagadas += 1
                print(f"Apagando luz: {disp.nombre}")

            elif disp.tipo == 'electrodomestico' and disp.estado != 'apagado':
                disp.cambiar_estado('apagado')
                electro_apagados += 1
                print(f"Apagando electrodoméstico: {disp.nombre}")

            elif disp.tipo == 'cámara' and disp.estado != 'encendido':
                disp.cambiar_estado('encendido')
                camaras_encendidas += 1
                print(f"Encendiendo cámara: {disp.nombre}")

        print(f"\n Modo Noche activado.")
        print(f"   Luces apagadas: {luces_apagadas}")
        print(f"   Electrodomésticos apagados: {electro_apagados}")
        print(f"   Cámaras encendidas: {camaras_encendidas}\n")

control_automatizaciones = ControlAutomatizaciones() 

def consultar_automatizaciones_activas():
    """Muestra las automatizaciones disponibles."""
    print("\n--- Automatizaciones Disponibles ---")
    print("1. Modo Ahorro de Energía → Apaga todos los dispositivos no esenciales.")
    print("2. Modo Noche → Apaga luces y electrodomésticos, enciende cámaras de seguridad.")
    print("------------------------------------\n")

# def modo_ahorro_energia(usuario_obj):
#     """
#     Activa el Modo Ahorro de Energía, apagando todos los dispositivos no esenciales.
#     """
#     print("\n Activando Modo Ahorro de Energía...")
#     if usuario_obj in USUARIOS:
#         dispositivos = USUARIOS[usuario_obj]['dispositivos']
#         dispositivos_apagados = 0
#         for disp in dispositivos:
#             if disp['tipo'] in ['luz', 'electrodomestico']:
#                 disp['estado'] = 'apagado'
#                 dispositivos_apagados += 1
#                 print(f"Apagando: {disp['nombre']} ({disp['tipo']})")
        
#         print(f" Modo Ahorro de Energía activado. {dispositivos_apagados} dispositivos apagados.")
#     else:
#         print(" Error: Usuario no encontrado.")


# def modo_noche(nombre_usuario):
#     """
#     Activa el Modo Noche:
#     - Apaga luces
#     - Apaga electrodomésticos
#     - Enciende cámaras de seguridad
#     """
#     print("\n Activando Modo Noche...")
#     if nombre_usuario in USUARIOS:
#         dispositivos = USUARIOS[nombre_usuario]['dispositivos']
#         luces_apagadas = 0
#         electro_apagados = 0
#         camaras_encendidas = 0

#         for disp in dispositivos:
#             if disp['tipo'] == 'luz':
#                 disp['estado'] = 'apagado'
#                 luces_apagadas += 1
#                 print(f"Apagando luz: {disp['nombre']}")
#             elif disp['tipo'] == 'electrodomestico':
#                 disp['estado'] = 'apagado'
#                 electro_apagados += 1
#                 print(f"Apagando electrodoméstico: {disp['nombre']}")
#             elif disp['tipo'] == 'cámara':
#                 disp['estado'] = 'encendido'
#                 camaras_encendidas += 1
#                 print(f"Encendiendo cámara de seguridad: {disp['nombre']}")

#         print(f"\n Modo Noche activado. Luces apagadas: {luces_apagadas}, "
#               f"Electrodomésticos apagados: {electro_apagados}, "
#               f"Cámaras encendidas: {camaras_encendidas}.")
#     else:
#         print(" Error: Usuario no encontrado.")


# def consultar_automatizaciones_activas():
#     """
#     Muestra una lista de las automatizaciones activas en el sistema.
#     """
#     print("\n--- Automatizaciones Activas ---")
#     print("1. Modo Ahorro de Energía: Apaga todos los dispositivos no esenciales.")
#     print("2. Modo Noche: Apaga luces y electrodomésticos, enciende cámaras de seguridad.")
#     print("--------------------------------\n")
