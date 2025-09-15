import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dispositivos

class TestDispositivos(unittest.TestCase):
    def setUp(self):
        dispositivos.dispositivos.clear()

    def test_agregar_dispositivo(self):
        dispositivos.agregar_dispositivo("Luz Cocina", "luz", "apagado")
        self.assertIn("Luz Cocina", dispositivos.dispositivos)

    def test_dispositivo_duplicado(self):
        dispositivos.agregar_dispositivo("Luz Cocina", "luz", "apagado")
        dispositivos.agregar_dispositivo("Luz Cocina", "luz", "apagado")
        self.assertEqual(len(dispositivos.dispositivos), 1)

    def test_cambiar_estado(self):
        dispositivos.agregar_dispositivo("TV", "electrodoméstico", "apagado")
        dispositivos.cambiar_estado("TV", "encendido")
        self.assertEqual(dispositivos.dispositivos["TV"]["estado"], "encendido")

    def test_ver_estado(self):
        dispositivos.agregar_dispositivo("Camara", "cámara", "apagado")
        estado = dispositivos.buscar_dispositivo("Camara")["estado"]
        self.assertEqual(estado, "apagado")

if __name__ == "__main__":
    unittest.main()
