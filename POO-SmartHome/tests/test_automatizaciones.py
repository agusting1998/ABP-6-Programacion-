import unittest
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
