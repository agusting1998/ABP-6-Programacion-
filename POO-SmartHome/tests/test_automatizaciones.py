import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Dominio.automatizaciones import ControlAutomatizaciones

class DispositivoMock:
    def __init__(self, nombre, tipo, estado):
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

class UsuarioMock:
    def __init__(self, dispositivos):
        self.dispositivos = dispositivos

class TestControlAutomatizaciones(unittest.TestCase):
    def test_modo_ahorro_energia(self):
        dispositivos = [
            DispositivoMock("Luz 1", "luz", "encendido"),
            DispositivoMock("Heladera", "electrodomestico", "encendido"),
            DispositivoMock("Cámara 1", "cámara", "encendido"),
            DispositivoMock("Luz 2", "luz", "apagado"),
        ]
        usuario = UsuarioMock(dispositivos)
        control = ControlAutomatizaciones()
        control.modo_ahorro_energia(usuario)
        self.assertEqual(dispositivos[0].estado, "apagado")
        self.assertEqual(dispositivos[1].estado, "apagado")
        self.assertEqual(dispositivos[2].estado, "encendido")
        self.assertEqual(dispositivos[3].estado, "apagado")

    def test_modo_noche(self):
        dispositivos = [
            DispositivoMock("Luz 1", "luz", "encendido"),
            DispositivoMock("Heladera", "electrodomestico", "encendido"),
            DispositivoMock("Cámara 1", "cámara", "apagado"),
            DispositivoMock("Luz 2", "luz", "apagado"),
        ]
        usuario = UsuarioMock(dispositivos)
        control = ControlAutomatizaciones()
        control.modo_noche(usuario)
        self.assertEqual(dispositivos[0].estado, "apagado")
        self.assertEqual(dispositivos[1].estado, "apagado")
        self.assertEqual(dispositivos[2].estado, "encendido")
        self.assertEqual(dispositivos[3].estado, "apagado")

if __name__ == '__main__':
    unittest.main()
