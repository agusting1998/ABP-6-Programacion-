# import unittest
# from usuario import Usuario, GestorUsuarios


# class TestUsuario(unittest.TestCase):
#     """Pruebas unitarias para la clase Usuario."""

#     def setUp(self):
#         self.usuario = Usuario("Matías", "1234", "usuario")

#     def test_creacion_usuario(self):
#         """Verifica que el usuario se cree correctamente."""
#         self.assertEqual(self.usuario.nombre, "Matías")
#         self.assertEqual(self.usuario.contrasena, "1234")
#         self.assertEqual(self.usuario.rol, "usuario")
#         self.assertEqual(self.usuario.dispositivos, [])

#     def test_modificar_rol(self):
#         """Verifica que el rol se modifique correctamente."""
#         self.usuario.modificar_rol("admin")
#         self.assertEqual(self.usuario.rol, "admin")


# class TestGestorUsuarios(unittest.TestCase):
#     """Pruebas unitarias para la clase GestorUsuarios."""

#     def setUp(self):
#         self.gestor = GestorUsuarios()

#     def test_registrar_usuario(self):
#         """Prueba registrar un nuevo usuario."""
#         self.gestor.registrar_usuario("Lucía", "abcd", "usuario")
#         self.assertIn("Lucía", self.gestor.usuarios)
#         self.assertIsInstance(self.gestor.usuarios["Lucía"], Usuario)
#         self.assertEqual(self.gestor.usuarios["Lucía"].rol, "usuario")

#     def test_registrar_usuario_existente(self):
#         """Prueba intentar registrar un usuario repetido (no debe duplicarse)."""
#         self.gestor.registrar_usuario("Lucía", "abcd", "usuario")
#         usuarios_antes = len(self.gestor.usuarios)
#         self.gestor.registrar_usuario("Lucía", "abcd", "usuario")
#         usuarios_despues = len(self.gestor.usuarios)
#         self.assertEqual(usuarios_antes, usuarios_despues)

#     def test_registrar_usuario_admin(self):
#         """Prueba registrar un usuario administrador."""
#         self.gestor.registrar_usuario_admin("Admin1", "adminpass")
#         self.assertIn("Admin1", self.gestor.usuarios)
#         self.assertEqual(self.gestor.usuarios["Admin1"].rol, "admin")

#     def test_iniciar_sesion_exitoso(self):
#         """Prueba iniciar sesión correctamente."""
#         self.gestor.registrar_usuario("Carlos", "clave", "usuario")
#         usuario = self.gestor.iniciar_sesion("Carlos", "clave")
#         self.assertIsNotNone(usuario)
#         self.assertEqual(usuario.nombre, "Carlos")

#     def test_iniciar_sesion_fallido(self):
#         """Prueba iniciar sesión con datos incorrectos."""
#         self.gestor.registrar_usuario("Carlos", "clave", "usuario")
#         usuario = self.gestor.iniciar_sesion("Carlos", "incorrecta")
#         self.assertIsNone(usuario)

#     def test_mostrar_usuarios_vacio(self):
#         """Prueba mostrar usuarios cuando no hay ninguno (solo verifica que no falle)."""
#         try:
#             self.gestor.mostrar_usuarios()
#             resultado = True
#         except Exception:
#             resultado = False
#         self.assertTrue(resultado)

#     def test_mostrar_usuarios_existentes(self):
#         """Prueba mostrar usuarios cuando ya hay registrados."""
#         self.gestor.registrar_usuario("María", "555", "usuario")
#         try:
#             self.gestor.mostrar_usuarios()
#             resultado = True
#         except Exception:
#             resultado = False
#         self.assertTrue(resultado)


# if __name__ == "__main__":
#     unittest.main()
