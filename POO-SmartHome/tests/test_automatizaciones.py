import sys
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROYECTO_DIR = os.path.join(BASE_DIR, "..", "POO-SmartHome")
DOMINIO_DIR = os.path.join("..", "Dominio")
CONN_DIR = os.path.join("..", "Conn")


for ruta in [PROYECTO_DIR, DOMINIO_DIR, CONN_DIR]:
    if ruta not in sys.path:
        sys.path.append(ruta)


from automatizaciones import ControlAutomatizaciones


class DispositivoSimulado:
    def __init__(self, nombre, tipo, estado):
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado

class UsuarioSimulado:
    def __init__(self, email, dispositivos=None):
        self.email = email
        self.dispositivos = dispositivos or []


class ControlAutomatizacionesMock(ControlAutomatizaciones):
    def guardar_activacion(self, email_usuario, nombre_automatizacion):
        print(f"[SIMULADO] guardar_activacion -> {email_usuario}, {nombre_automatizacion}")

def test_modo_ahorro_energia():
    print("=== TEST: modo_ahorro_energia ===")

    dispositivos = [
        DispositivoSimulado("Luz 1", "luz", "encendido"),
        DispositivoSimulado("TV", "electrodomestico", "encendido"),
        DispositivoSimulado("Ventana", "otro", "encendido"),
        DispositivoSimulado("Lampara", "luz", "apagado")
    ]
    usuario = UsuarioSimulado("user@test.com", dispositivos)

    ctrl = ControlAutomatizacionesMock()
    ctrl.modo_ahorro_energia(usuario)

    for d in usuario.dispositivos:
        print(f"{d.nombre} -> {d.estado}")

def test_modo_noche():
    print("=== TEST: modo_noche ===")

    dispositivos = [
        DispositivoSimulado("Luz 1", "luz", "encendido"),
        DispositivoSimulado("TV", "electrodomestico", "encendido"),
        DispositivoSimulado("Camara 1", "cámara", "apagado")
    ]
    usuario = UsuarioSimulado("user@test.com", dispositivos)

    ctrl = ControlAutomatizacionesMock()
    ctrl.modo_noche(usuario)

    for d in usuario.dispositivos:
        print(f"{d.nombre} -> {d.estado}")

if __name__ == "__main__":
    test_modo_ahorro_energia()
    print()
    test_modo_noche()
