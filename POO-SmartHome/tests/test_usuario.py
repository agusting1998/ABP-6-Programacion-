import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import usuario

class TestUsuario(unittest.TestCase):
    def setUp(self):
        usuario.usuarios.clear()

    def test_registrar_usuario(self):
        usuario.registrar_usuario_estandar("Agustin", "Gallardo", "agus@mail.com")
        self.assertIn("agus@mail.com", usuario.usuarios)

    def test_registrar_usuario_existente(self):
        usuario.registrar_usuario_estandar("Agustin", "Gallardo", "agus@mail.com")
        usuario.registrar_usuario_estandar("Agustin", "Gallardo", "agus@mail.com")
        self.assertEqual(len(usuario.usuarios), 1)

    def test_modificar_rol(self):
        usuario.registrar_usuario_estandar("Agustin", "Gallardo", "agus@mail.com")
        usuario.modificar_rol("agus@mail.com", "admin")
        self.assertEqual(usuario.usuarios["agus@mail.com"]["rol"], "admin")

if __name__ == "__main__":
    unittest.main()
