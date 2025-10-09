# import unittest
# from unittest.mock import patch, MagicMock
# import sys
# import os

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# import menu_manager


# class TestMenuManager(unittest.TestCase):

#     @patch("builtins.input", side_effect=["0"])  # Simula que el usuario elige salir
#     @patch("builtins.print")
#     def test_mostrar_menu_principal_salir(self, mock_print, mock_input):
#         menu_manager.mostrar_menu_principal()
#         # Verificamos que se haya mostrado el mensaje de salida
#         mock_print.assert_any_call("Saliendo de la aplicación...")

#     @patch("menu_manager.usuario.registrar_usuario")
#     @patch("builtins.input", side_effect=["A", "Juan", "1234", "0"])  # Opción A -> registrar usuario estándar -> salir
#     @patch("builtins.print")
#     def test_registrar_usuario_estandar(self, mock_print, mock_input, mock_registrar):
#         menu_manager.mostrar_menu_principal()
#         mock_registrar.assert_called_once_with("Juan", "1234", rol="estandar")

#     @patch("menu_manager.usuario.registrar_usuario")
#     @patch("builtins.input", side_effect=["B", "Admin", "abcd", "0"])  # Opción B -> registrar admin -> salir
#     @patch("builtins.print")
#     def test_registrar_usuario_admin(self, mock_print, mock_input, mock_registrar):
#         menu_manager.mostrar_menu_principal()
#         mock_registrar.assert_called_once_with("Admin", "abcd", rol="admin")

#     @patch("menu_manager.usuario.iniciar_sesion")
#     @patch("menu_manager.mostrar_menu_usuario_estandar")
#     @patch("builtins.input", side_effect=["1", "user", "pass", "0"])  # login como usuario estandar
#     @patch("builtins.print")
#     def test_login_usuario_estandar(self, mock_print, mock_input, mock_menu_estandar, mock_login):
#         mock_login.return_value = {"rol": "estandar"}
#         menu_manager.mostrar_menu_principal()
#         mock_menu_estandar.assert_called_once_with("user")

#     @patch("menu_manager.usuario.iniciar_sesion")
#     @patch("menu_manager.mostrar_menu_admin_principal")
#     @patch("builtins.input", side_effect=["1", "admin", "clave", "0"])  # login como admin
#     @patch("builtins.print")
#     def test_login_usuario_admin(self, mock_print, mock_input, mock_menu_admin, mock_login):
#         mock_login.return_value = {"rol": "admin"}
#         menu_manager.mostrar_menu_principal()
#         mock_menu_admin.assert_called_once_with("admin")

#     @patch("menu_manager.automatizaciones.modo_noche")
#     @patch("builtins.input", side_effect=["3", "usuarioX", "0"])  # Activa modo noche
#     @patch("builtins.print")
#     def test_modo_noche(self, mock_print, mock_input, mock_modo_noche):
#         menu_manager.mostrar_menu_principal()
#         mock_modo_noche.assert_called_once_with("usuarioX")

#     @patch("menu_manager.soporte.mostrar_ayuda")
#     @patch("builtins.input", side_effect=["4", "0"])  # Soporte
#     @patch("builtins.print")
#     def test_soporte(self, mock_print, mock_input, mock_ayuda):
#         menu_manager.mostrar_menu_principal()
#         mock_ayuda.assert_called_once()


# if __name__ == "__main__":
#     unittest.main()
