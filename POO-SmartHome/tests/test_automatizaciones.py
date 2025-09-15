import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import dispositivos
import automatizaciones

class TestAutomatizaciones(unittest.TestCase):
    def setUp(self):
        dispositivos.dispositivos.clear()
        dispositivos.agregar_dispositivo("Luz Cocina", "luz", "encendido")
        dispositivos.agregar_dispositivo("Camara Garage", "cámara", "apagado")

    def test_modo_noche(self):
        automatizaciones.modo_noche()
        self.assertEqual(dispositivos.dispositivos["Luz Cocina"]["estado"], "apagado")
        self.assertEqual(dispositivos.dispositivos["Camara Garage"]["estado"], "encendido")

if __name__ == "__main__":
    unittest.main()
