from datetime import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Conn'))
from db_conn import get_connection

class ControlAutomatizaciones:
    def modo_ahorro_energia(self, usuario_obj):
        print("\nActivando Modo Ahorro de Energía...")
        dispositivos_apagados = 0

        for disp in getattr(usuario_obj, "dispositivos", []):
            if disp.tipo in ['luz', 'electrodomestico'] and disp.estado == 'encendido':
                disp.estado = 'apagado'
                dispositivos_apagados += 1

        self.guardar_activacion(usuario_obj.email, "Modo_Ahorro_Energia")
        print(f"Modo Ahorro de Energía activado. {dispositivos_apagados} dispositivos apagados.\n")

    def modo_noche(self, usuario_obj):
        print("\nActivando Modo Noche...")

        for disp in getattr(usuario_obj, "dispositivos", []):
            if disp.tipo in ['luz', 'electrodomestico']:
                disp.estado = 'apagado'
            elif disp.tipo == 'cámara':
                disp.estado = 'encendido'

        self.guardar_activacion(usuario_obj.email, "Modo_Noche")
        print("Modo Noche activado.\n")

    def guardar_activacion(self, email_usuario, nombre_automatizacion):
        try:
            conn = get_connection()
            if not conn:
                return
            cursor = conn.cursor()

            cursor.execute("""
                INSERT IGNORE INTO Automatizacion (nombre_automatizacion)
                VALUES (%s)
            """, (nombre_automatizacion,))

            cursor.execute(
                "INSERT INTO Activacion (email_usuario, nombre_automatizacion, fecha_activacion) VALUES (%s, %s, %s)",
                (email_usuario, nombre_automatizacion, datetime.now())
            )

            conn.commit()
            print("Activación registrada exitosamente.")
        except Exception as e:
            print(f"Error al guardar la activación: {e}")
        finally:
            if conn:
                cursor.close()
                conn.close()

control_automatizaciones = ControlAutomatizaciones()

def consultar_automatizaciones_activas():
    print("\n--- Automatizaciones Disponibles ---")
    print("1. Modo Ahorro de Energía")
    print("2. Modo Noche")
    print("------------------------------------\n")
