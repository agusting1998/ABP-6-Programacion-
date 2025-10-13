import sys
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROYECTO_DIR = os.path.join(BASE_DIR, "..", "POO-SmartHome")
DOMINIO_DIR = os.path.join("..", "Dominio")
CONN_DIR = os.path.join("..", "Conn")


for ruta in [PROYECTO_DIR, DOMINIO_DIR, CONN_DIR]:
    if ruta not in sys.path:
        sys.path.append(ruta)


from dispositivos import agregar_dispositivo, listar_dispositivos, cambiar_estado, eliminar_dispositivo

class UsuarioSimulado:
    def __init__(self, email):
        self.email = email

class DispositivoMock:
    def __init__(self, nombre, tipo, estado="apagado"):
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado

def mock_agregar_dispositivo(usuario_email, nombre, tipo, estado="apagado"):
    print(f"[MOCK] Agregado: {nombre} ({tipo}) para {usuario_email} con estado {estado}")
    return DispositivoMock(nombre, tipo, estado)

def mock_listar_dispositivos(usuario_obj):
    print(f"[MOCK] Listar dispositivos de {usuario_obj.email}")
    return [
        DispositivoMock("Lámpara Test", "luz", "encendido"),
        DispositivoMock("TV", "electrodomestico", "apagado")
    ]

def mock_cambiar_estado(usuario_obj, nombre_dispositivo, nuevo_estado):
    print(f"[MOCK] Cambiar estado de {nombre_dispositivo} a {nuevo_estado} para {usuario_obj.email}")

def mock_eliminar_dispositivo(usuario_obj, nombre_dispositivo):
    print(f"[MOCK] Eliminar {nombre_dispositivo} para {usuario_obj.email}")

# --- Tests ---
def test_agregar_dispositivo():
    print("\n=== TEST: agregar_dispositivo ===")
    usuario = UsuarioSimulado("user@test.com")
    disp = mock_agregar_dispositivo(usuario.email, "Lámpara Test", "luz", "encendido")
    print(f"Resultado: {disp.nombre} - {disp.tipo} - {disp.estado}")

def test_listar_dispositivos():
    print("\n=== TEST: listar_dispositivos ===")
    usuario = UsuarioSimulado("user@test.com")
    dispositivos = mock_listar_dispositivos(usuario)
    for d in dispositivos:
        print(f"{d.nombre} - {d.tipo} - {d.estado}")

def test_cambiar_estado():
    print("\n=== TEST: cambiar_estado ===")
    usuario = UsuarioSimulado("user@test.com")
    mock_cambiar_estado(usuario, "Lámpara Test", "apagado")

def test_eliminar_dispositivo():
    print("\n=== TEST: eliminar_dispositivo ===")
    usuario = UsuarioSimulado("user@test.com")
    mock_eliminar_dispositivo(usuario, "Lámpara Test")

if __name__ == "__main__":
    test_agregar_dispositivo()
    test_listar_dispositivos()
    test_cambiar_estado()
    test_eliminar_dispositivo()
