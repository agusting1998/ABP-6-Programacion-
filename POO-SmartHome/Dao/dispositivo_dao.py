import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Dominio'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Conn'))

from dispositivos import Dispositivo, LuzInteligente
from db_conn import get_connection
from idao import IDAO

class DispositivoDAO(IDAO):
    def agregar(self, usuario_email, nombre, tipo, estado="apagado"):
        if tipo.lower() == "luz":
            disp = LuzInteligente(nombre, estado)
        else:
            disp = Dispositivo(nombre, tipo, estado)
        conn = get_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO Dispositivo (nombre_dispositivo, tipo, estado) VALUES (%s, %s, %s)",
                (disp.nombre, disp.tipo, disp.estado)
            )
            cursor.execute(
                "INSERT INTO Gestion (email_usuario, nombre_dispositivo) VALUES (%s, %s)",
                (usuario_email, disp.nombre)
            )
            conn.commit()
            print(f"Dispositivo '{disp.nombre}' agregado exitosamente.")
            return disp
        except Exception as e:
            print(f"Error al agregar dispositivo: {e}")
            conn.rollback()
            return None
        finally:
            cursor.close()
            conn.close()

    def obtener(self, nombre_dispositivo):
        """Obtiene un dispositivo por nombre"""
        conn = get_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT nombre_dispositivo, tipo, estado FROM Dispositivo WHERE nombre_dispositivo=%s",
                (nombre_dispositivo,)
            )
            row = cursor.fetchone()
            if row:
                if row[1] == "luz":
                    return LuzInteligente(row[0], row[2])
                else:
                    return Dispositivo(row[0], row[1], row[2])
            return None
        finally:
            cursor.close()
            conn.close()

    def listar_por_usuario(self, usuario_obj):
        conn = get_connection()
        if not conn:
            return []
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT d.nombre_dispositivo, d.tipo, d.estado "
                "FROM Dispositivo d JOIN Gestion g ON d.nombre_dispositivo = g.nombre_dispositivo "
                "WHERE g.email_usuario = %s", (usuario_obj.email,)
            )
            rows = cursor.fetchall()
            dispositivos = []
            for r in rows:
                if r[1] == "luz":
                    dispositivos.append(LuzInteligente(r[0], r[2]))
                else:
                    dispositivos.append(Dispositivo(r[0], r[1], r[2]))
            return dispositivos
        finally:
            cursor.close()
            conn.close()

    def cambiar_estado(self, usuario_obj, nombre_dispositivo, nuevo_estado):
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE Dispositivo d JOIN Gestion g ON d.nombre_dispositivo = g.nombre_dispositivo "
                "SET d.estado=%s WHERE g.email_usuario=%s AND d.nombre_dispositivo=%s",
                (nuevo_estado, usuario_obj.email, nombre_dispositivo)
            )
            conn.commit()
            print(f"Estado de '{nombre_dispositivo}' cambió a '{nuevo_estado}'.")
        except Exception as e:
            print(f"Error al cambiar estado: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def eliminar(self, usuario_obj, nombre_dispositivo):
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "DELETE FROM Gestion WHERE email_usuario=%s AND nombre_dispositivo=%s",
                (usuario_obj.email, nombre_dispositivo)
            )
            cursor.execute(
                "DELETE FROM Dispositivo WHERE nombre_dispositivo=%s",
                (nombre_dispositivo,)
            )
            conn.commit()
            print(f"Dispositivo '{nombre_dispositivo}' eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar dispositivo: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def actualizar(self, dispositivo):
        """Actualiza un dispositivo existente"""
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        try:
            cursor.execute(
                "UPDATE Dispositivo SET tipo=%s, estado=%s WHERE nombre_dispositivo=%s",
                (dispositivo.tipo, dispositivo.estado, dispositivo.nombre)
            )
            conn.commit()
            print(f"Dispositivo '{dispositivo.nombre}' actualizado exitosamente.")
        except Exception as e:
            print(f"Error al actualizar dispositivo: {e}")
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def listar_todos(self):
        """Lista todos los dispositivos"""
        conn = get_connection()
        if not conn:
            return []
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT nombre_dispositivo, tipo, estado FROM Dispositivo")
            rows = cursor.fetchall()
            dispositivos = []
            for row in rows:
                if row[1] == "luz":
                    dispositivos.append(LuzInteligente(row[0], row[2]))
                else:
                    dispositivos.append(Dispositivo(row[0], row[1], row[2]))
            return dispositivos
        finally:
            cursor.close()
            conn.close()
