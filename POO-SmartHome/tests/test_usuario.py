import unittest
from unittest.mock import patch
import io
import sys
import os

# Agregamos la ruta al módulo Dominio
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Dominio')))

from usuario import Usuario, GestorUsuarios

class TestUsuario(unittest.TestCase):

    def setUp(self):
        self.gestor = GestorUsuarios()

    def test_crear_usuario(self):
        usuario = Usuario("Agustin", "1234", "estandar")
        self.assertEqual(usuario.nombre, "Agustin")
        self.assertEqual(usuario.contrasena, "1234")
        self.assertEqual(usuario.rol, "estandar")
        self.assertEqual(usuario.dispositivos, [])

    def test_consultar_datos_personales(self):
        usuario = Usuario("Agustin", "1234", "estandar")
        usuario.dispositivos.append("Dispositivo 1")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            usuario.consultar_datos_personales()
            output = fake_out.getvalue()
        self.assertIn("Datos de Agustin", output)
        self.assertIn("- Rol: estandar", output)
        self.assertIn("- Dispositivos registrados: 1", output)

    def test_modificar_rol(self):
        usuario = Usuario("Agustin", "1234", "estandar")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            usuario.modificar_rol("admin")
            output = fake_out.getvalue()
        self.assertEqual(usuario.rol, "admin")
        self.assertIn("Rol de Agustin modificado a admin", output)

    def test_registrar_usuario_exitoso(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.gestor.registrar_usuario("Agustin", "1234", "estandar")
            output = fake_out.getvalue()
        self.assertIn("Usuario Agustin registrado con éxito como estandar", output)
        self.assertIn("Agustin", self.gestor.usuarios)
        self.assertIsInstance(self.gestor.usuarios["Agustin"], Usuario)

    def test_registrar_usuario_duplicado(self):
        self.gestor.registrar_usuario("Agustin", "1234", "estandar")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.gestor.registrar_usuario("Agustin", "5678", "admin")
            output = fake_out.getvalue()
        self.assertIn("Ya existe un usuario con ese nombre", output)

    def test_iniciar_sesion_exitoso(self):
        self.gestor.registrar_usuario("Agustin", "1234", "estandar")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            usuario = self.gestor.iniciar_sesion("Agustin", "1234")
            output = fake_out.getvalue()
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.nombre, "Agustin")
        self.assertIn("Inicio de sesión exitoso", output)

    def test_iniciar_sesion_fallido(self):
        self.gestor.registrar_usuario("Agustin", "1234", "estandar")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            usuario = self.gestor.iniciar_sesion("Agustin", "0000")
            output = fake_out.getvalue()
        self.assertIsNone(usuario)
        self.assertIn("Nombre de usuario o contraseña incorrectos", output)

    def test_mostrar_usuarios(self):
        self.gestor.registrar_usuario("Agustin", "1234", "estandar")
        self.gestor.registrar_usuario("Maria", "abcd", "admin")
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.gestor.mostrar_usuarios()
            output = fake_out.getvalue()
        self.assertIn("- Agustin (rol: estandar)", output)
        self.assertIn("- Maria (rol: admin)", output)

    def test_mostrar_usuarios_vacio(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.gestor.mostrar_usuarios()
            output = fake_out.getvalue()
        self.assertIn("No hay usuarios registrados", output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
