import unittest
from unittest.mock import patch
import io
import sys
import os

# Agregamos la ruta al módulo Dominio
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Dominio')))

import soporte

class TestSoporte(unittest.TestCase):

    def test_mostrar_ayuda(self):
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            soporte.mostrar_ayuda()
            output = fake_out.getvalue()
        
        self.assertIn("Centro de Soporte", output)
        self.assertIn("1. Si un dispositivo no aparece", output)
        self.assertIn("4. Para asistencia técnica", output)

    def test_validar_estado_valido(self):
        self.assertTrue(soporte.validar_estado("encendido"))
        self.assertTrue(soporte.validar_estado("apagado"))
        # Mayúsculas también deben ser válidas
        self.assertTrue(soporte.validar_estado("ENCENDIDO"))
        self.assertTrue(soporte.validar_estado("Apagado"))

    def test_validar_estado_invalido(self):
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            resultado = soporte.validar_estado("standby")
            output = fake_out.getvalue()
        
        self.assertFalse(resultado)
        self.assertIn("Estado inválido", output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
