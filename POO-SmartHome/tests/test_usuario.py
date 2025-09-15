import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import usuario

class TestUsuario(unittest.TestCase):
    def setUp(self):
        usuario.USUARIOS.clear()

    def test_registrar_usuario(self):
        usuario.registrar_usuario("Agustin", "Gallardo", "agus@mail.com")
        self.assertIn("agus@mail.com", usuario.USUARIOS)

    def test_registrar_usuario_existente(self):
        usuario.registrar_usuario("Agustin", "Gallardo", "agus@mail.com")
        usuario.registrar_usuario("Agustin", "Gallardo", "agus@mail.com")
        self.assertEqual(len(usuario.USUARIOS), 1)

    def test_modificar_rol(self):
        usuario.registrar_usuario("Agustin", "Gallardo", "agus@mail.com")
        usuario.modificar_rol_usuario("agus@mail.com", "admin")
        self.assertEqual(usuario.USUARIOS["agus@mail.com"]["rol"], "admin")

if __name__ == "__main__":
    unittest.main()
