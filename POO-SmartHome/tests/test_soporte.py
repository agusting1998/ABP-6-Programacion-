import unittest
import soporte

class TestSoporte(unittest.TestCase):
    def test_validar_estado_valido(self):
        self.assertTrue(soporte.validar_estado("encendido"))
        self.assertTrue(soporte.validar_estado("apagado"))

    def test_validar_estado_invalido(self):
        self.assertFalse(soporte.validar_estado("prendido"))
