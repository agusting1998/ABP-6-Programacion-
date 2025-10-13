import unittest
from unittest.mock import patch
import io
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Dominio')))

from usuario import Usuario, GestorUsuarios

class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorUsuarios()

    def test_crear_usuario(self):
        usuario = Usuario("Agustin", "1234", "estandar", "agustin@test.com")
        self.assertEqual(usuario.nombre, "Agustin")
        self.assertEqual(usuario.passw, "1234") 
        self.assertEqual(usuario.rol, "estandar")
        self.assertEqual(usuario.email, "agustin@test.com") 

    def test_consultar_datos_personales(self):
        usuario = Usuario("Agustin", "1234", "estandar", "agustin@test.com")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            usuario.consultar_datos_personales()
            output = fake_out.getvalue()
        self.assertIn("Datos de Agustin", output)
        self.assertIn("- Rol: estandar", output)
        self.assertIn("- Email: agustin@test.com", output)

    def test_modificar_rol(self):
        usuario = Usuario("Agustin", "1234", "estandar", "agustin@test.com")
        with patch('usuario.get_connection'), \
             patch('sys.stdout', new=io.StringIO()) as fake_out:
            usuario.modificar_rol("admin")
            output = fake_out.getvalue()
        self.assertEqual(usuario.rol, "admin")
        self.assertIn("Rol de Agustin modificado a admin", output)

    def test_registrar_usuario_exitoso(self):

        self.gestor.registrar_usuario("Agustin", "1234", "estandar", "agustin@test.com")
        self.assertIn("agustin@test.com", self.gestor.usuarios)
        self.assertIsInstance(self.gestor.usuarios["agustin@test.com"], Usuario)
        
    def test_registrar_usuario_duplicado(self):
        self.gestor.registrar_usuario("Agustin", "1234", "estandar", "agustin@test.com")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.gestor.registrar_usuario("Agustin 2", "5678", "admin", "agustin@test.com")
            output = fake_out.getvalue()
        self.assertIn("Error: El email ya existe en el sistema.", output)

    def test_iniciar_sesion_exitoso(self):
        self.gestor.registrar_usuario("Agustin", "1234", "estandar", "agustin@test.com")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            usuario = self.gestor.iniciar_sesion("agustin@test.com", "1234")
            output = fake_out.getvalue()
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.nombre, "Agustin")
        self.assertIn("Bienvenido, Agustin.", output) 
        
    def test_iniciar_sesion_fallido(self):
        self.gestor.registrar_usuario("Agustin", "1234", "estandar", "agustin@test.com")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            usuario = self.gestor.iniciar_sesion("agustin@test.com", "0000")
            output = fake_out.getvalue()
        self.assertIsNone(usuario)
        self.assertIn("Usuario o contraseña incorrectos.", output)
        
    def test_mostrar_usuarios(self):
        self.gestor.registrar_usuario("Agustin", "1234", "estandar", "agustin@test.com")
        self.gestor.registrar_usuario("Maria", "abcd", "admin", "maria@test.com")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.gestor.mostrar_usuarios()
            output = fake_out.getvalue()
        self.assertIn("- Agustin | agustin@test.com | estandar", output)
        self.assertIn("- Maria | maria@test.com | admin", output)

    def test_mostrar_usuarios_vacio(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.gestor.mostrar_usuarios()
            output = fake_out.getvalue()
        self.assertIn("No hay usuarios registrados.", output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
