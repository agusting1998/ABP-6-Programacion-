import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import soporte

class TestSoporte(unittest.TestCase):
    def test_validar_estado_valido(self):
        self.assertTrue(soporte.validar_estado("encendido"))
        self.assertTrue(soporte.validar_estado("apagado"))

    def test_validar_estado_invalido(self):
        self.assertFalse(soporte.validar_estado("prendido"))

if __name__ == "__main__":
    unittest.main()
