import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import admin
import usuario
from data import USUARIOS, USUARIOS_ADMIN

class TestAdmin(unittest.TestCase):
    def setUp(self):
        USUARIOS.clear()
        USUARIOS_ADMIN.clear()

    def test_registrar_admin(self):
        admin.registrar_admin("yazmin", "1234")
        self.assertIn("yazmin", USUARIOS_ADMIN)

    def test_modificar_rol_usuario(self):
        usuario.registrar_usuario("Agustin", "1234")
        usuario.modificar_rol_usuario("Agustin", "admin")
        self.assertEqual(USUARIOS["Agustin"]["rol"], "admin")

if __name__ == "__main__":
    unittest.main()
