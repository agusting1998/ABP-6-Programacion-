import unittest
import sys
import os
from unittest.mock import patch
import io

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Dominio')))

import menu_manager
import dispositivos

class MockUsuario:
    def __init__(self, nombre, rol='estandar'):
        self.nombre = nombre
        self.rol = rol
        self.dispositivos = []
        self.datos_consultados = False
        self.rol_modificado = None

    def consultar_datos_personales(self):
        self.datos_consultados = True
        print(f"{self.nombre}: datos consultados")

    def modificar_rol(self, nuevo_rol):
        self.rol_modificado = nuevo_rol
        print(f"{self.nombre}: rol cambiado a {nuevo_rol}")


class TestMenuManager(unittest.TestCase):

    def test_menu_estandar_consulta_datos(self):
        user = MockUsuario("Juan")
        with patch('builtins.input', side_effect=['1','4']), \
             patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            menu_manager.menu_estandar(user)
        
        output = fake_out.getvalue()
        self.assertIn("datos consultados", output)
        self.assertTrue(user.datos_consultados)
        self.assertIn("--- Menú de Usuario Estándar (Juan) ---", output)

    def test_menu_estandar_opcion_invalida(self):
        user = MockUsuario("Ana")
        with patch('builtins.input', side_effect=['99','4']), \
             patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            menu_manager.menu_estandar(user)
        
        output = fake_out.getvalue()
        self.assertIn("Opción inválida", output)

    def test_menu_admin_modificar_rol_usuario_existente(self):
        admin_user = MockUsuario("Admin", rol='admin')
        # Creamos un mock del gestor de usuarios
        gestor_mock = type('Gestor', (), {})()
        gestor_mock.usuarios = {"Carlos": MockUsuario("Carlos")}
        menu_manager.gestor = gestor_mock

        with patch('builtins.input', side_effect=['3', 'Carlos', 'admin', '4']), \
             patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            menu_manager.menu_admin(admin_user)

        output = fake_out.getvalue()
        self.assertIn("rol cambiado a admin", output)
        self.assertEqual(gestor_mock.usuarios["Carlos"].rol_modificado, 'admin')

    def test_menu_admin_opcion_invalida(self):
        admin_user = MockUsuario("Admin", rol='admin')
        gestor_mock = type('Gestor', (), {})()
        gestor_mock.usuarios = {}
        menu_manager.gestor = gestor_mock

        with patch('builtins.input', side_effect=['99','4']), \
             patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            menu_manager.menu_admin(admin_user)

        output = fake_out.getvalue()
        self.assertIn("Opción inválida", output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
