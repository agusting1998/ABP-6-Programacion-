from datetime import datetime
from connection import get_connection

class ControlAutomatizaciones:
    def modo_ahorro_energia(self, usuario_obj):
        print("\nActivando Modo Ahorro de Energía...")
        dispositivos_apagados = 0
        for disp in usuario_obj.dispositivos if hasattr(usuario_obj, "dispositivos") else []:
            if disp.tipo in ['luz', 'electrodomestico'] and disp.estado == 'encendido':
                disp.estado = 'apagado'
                dispositivos_apagados += 1
        self.guardar_activacion(usuario_obj.email, "Modo Ahorro de Energía")
        print(f"Modo Ahorro de Energía activado. {dispositivos_apagados} dispositivos apagados.\n")

    def modo_noche(self, usuario_obj):
        print("\nActivando Modo Noche...")
        for disp in usuario_obj.dispositivos if hasattr(usuario_obj, "dispositivos") else []:
            if disp.tipo in ['luz', 'electrodomestico']:
                disp.estado = 'apagado'
            elif disp.tipo == 'cámara':
                disp.estado = 'encendido'
        self.guardar_activacion(usuario_obj.email, "Modo Noche")
        print("Modo Noche activado.\n")

    def guardar_activacion(self, email_usuario, nombre_automatizacion):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Activacion (email_usuario, nombre_automatizacion, fecha_activacion) VALUES (%s, %s, %s)",
            (email_usuario, nombre_automatizacion, datetime.now())
        )
        conn.commit()
        conn.close()

control_automatizaciones = ControlAutomatizaciones()

def consultar_automatizaciones_activas():
    print("\n--- Automatizaciones Disponibles ---")
    print("1. Modo Ahorro de Energía")
    print("2. Modo Noche")
    print("------------------------------------\n")
