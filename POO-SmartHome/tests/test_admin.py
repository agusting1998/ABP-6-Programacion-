import unittest
import admin
import usuario

class TestAdmin(unittest.TestCase):
    def setUp(self):
        usuario.usuarios.clear()
        admin.usuarios_admin.clear()

    def test_registrar_admin(self):
        admin.usuarios_admin["yazmin"] = "1234"
        self.assertIn("yazmin", admin.usuarios_admin)

    def test_modificar_rol_usuario(self):
        usuario.registrar_usuario_estandar("Agustin", "Gallardo", "agus@mail.com")
        usuario.modificar_rol("agus@mail.com", "admin")
        self.assertEqual(usuario.usuarios["agus@mail.com"]["rol"], "admin")
