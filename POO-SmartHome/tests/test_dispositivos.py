import unittest
import sys
import os
from unittest.mock import patch
import io

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Dominio.dispositivos import (
    Dispositivo, LuzInteligente,
    agregar_dispositivo, listar_dispositivos,
    eliminar_dispositivo, cambiar_estado
)

class TestClasesDispositivo(unittest.TestCase):

    def test_dispositivo_inicializacion(self):
        disp = Dispositivo("Ventilador", 1, "encendido", "electrodomestico")
        self.assertEqual(disp.nombre, "Ventilador")
        self.assertEqual(disp.id, 1)
        self.assertEqual(disp.estado, "encendido")
        self.assertEqual(disp.tipo, "electrodomestico")

    def test_dispositivo_cambiar_estado(self):
        disp = Dispositivo("Termostato", 2)
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            success = disp.cambiar_estado('encendido')
            self.assertTrue(success)
            self.assertEqual(disp.estado, 'encendido')
            self.assertIn("cambió su estado a 'encendido'", fake_out.getvalue())
        with patch('sys.stdout', new=io.StringIO()):
            success = disp.cambiar_estado('apagado')
            self.assertTrue(success)
            self.assertEqual(disp.estado, 'apagado')
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            success = disp.cambiar_estado('standby')
            self.assertFalse(success)
            self.assertEqual(disp.estado, 'apagado')
            self.assertIn("Estado inválido", fake_out.getvalue())

    def test_luz_inteligente_inicializacion(self):
        luz = LuzInteligente("Luz Patio", 3, "apagado", brillo=50)
        self.assertEqual(luz.nombre, "Luz Patio")
        self.assertEqual(luz.tipo, "luz")
        self.assertEqual(luz.estado, "apagado")
        self.assertEqual(luz.brillo, 50)

    def test_luz_inteligente_cambiar_estado_afecta_brillo(self):
        luz = LuzInteligente("Luz Dormitorio", 4, "apagado", brillo=0)
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            luz.cambiar_estado('encendido')
            self.assertEqual(luz.estado, 'encendido')
            self.assertEqual(luz.brillo, 100)
            self.assertIn("Brillo 100%", fake_out.getvalue())
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            luz.cambiar_estado('apagado')
            self.assertEqual(luz.estado, 'apagado')
            self.assertEqual(luz.brillo, 0)
            self.assertIn("Brillo 0%", fake_out.getvalue())
        with patch('sys.stdout', new=io.StringIO()):
            luz.cambiar_estado('pausa')
            self.assertEqual(luz.estado, 'apagado')
            self.assertEqual(luz.brillo, 0)

class TestFuncionesDispositivo(unittest.TestCase):

    def setUp(self):
        self.lista_dispositivos = []

    def test_agregar_dispositivo_luz_inteligente(self):
        with patch('sys.stdout', new=io.StringIO()):
            nuevo_disp = agregar_dispositivo(self.lista_dispositivos, "Luz Principal", "luz inteligente", "encendido")
        self.assertEqual(len(self.lista_dispositivos), 1)
        self.assertIsInstance(nuevo_disp, LuzInteligente)
        self.assertEqual(nuevo_disp.estado, 'encendido')
        self.assertEqual(nuevo_disp.id, 1)

    def test_agregar_dispositivo_generico(self):
        with patch('sys.stdout', new=io.StringIO()):
            nuevo_disp = agregar_dispositivo(self.lista_dispositivos, "Tostadora", "electrodomestico")
        self.assertEqual(len(self.lista_dispositivos), 1)
        self.assertIsInstance(nuevo_disp, Dispositivo)
        self.assertEqual(nuevo_disp.tipo, 'electrodomestico')

    def test_listar_dispositivos_vacio(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            listar_dispositivos(self.lista_dispositivos)
            self.assertIn("No tienes dispositivos registrados.", fake_out.getvalue())

    def test_listar_dispositivos_con_contenido(self):
        self.lista_dispositivos.append(Dispositivo("Campana", 1, tipo='extractor'))
        self.lista_dispositivos.append(LuzInteligente("Foco", 2))
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            listar_dispositivos(self.lista_dispositivos)
            output = fake_out.getvalue()
            self.assertIn("ID: 1 | Nombre: Campana (Tipo: extractor) | Estado: apagado", output)
            self.assertIn("ID: 2 | Nombre: Foco | Estado: apagado | Brillo: 0%", output)

    def test_eliminar_dispositivo_exitoso(self):
        disp_a = Dispositivo("A", 1)
        disp_b = Dispositivo("B", 2)
        self.lista_dispositivos.extend([disp_a, disp_b])
        with patch('sys.stdout', new=io.StringIO()):
            success = eliminar_dispositivo(self.lista_dispositivos, 1)
        self.assertTrue(success)
        self.assertEqual(len(self.lista_dispositivos), 1)
        self.assertEqual(self.lista_dispositivos[0].nombre, "B")

    def test_eliminar_dispositivo_no_encontrado(self):
        self.lista_dispositivos.append(Dispositivo("A", 1))
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            success = eliminar_dispositivo(self.lista_dispositivos, 99)
        self.assertFalse(success)
        self.assertEqual(len(self.lista_dispositivos), 1)
        self.assertIn("No se encontró ningún dispositivo con ID 99", fake_out.getvalue())

    def test_cambiar_estado_exitoso(self):
        disp = Dispositivo("Toldo", 1, estado_inicial='encendido')
        self.lista_dispositivos.append(disp)
        with patch('sys.stdout', new=io.StringIO()):
            success = cambiar_estado(self.lista_dispositivos, 1, 'apagado')
        self.assertTrue(success)
        self.assertEqual(disp.estado, 'apagado')

    def test_cambiar_estado_id_no_encontrado(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            success = cambiar_estado(self.lista_dispositivos, 10, 'encendido')
        self.assertFalse(success)
        self.assertIn("No se encontró ningún dispositivo con ID 10", fake_out.getvalue())

if __name__ == '__main__':
    unittest.main(verbosity=2)
