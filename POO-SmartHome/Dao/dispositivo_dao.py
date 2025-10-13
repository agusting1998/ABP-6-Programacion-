import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Dominio'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Conn'))

from conn.db_conn import get_connection
from dispositivos import Dispositivo, LuzInteligente


class DispositivoDAO:
    def agregar(self, usuario_email, nombre, tipo, estado="apagado"):
        if tipo.lower() == "luz":
            disp = LuzInteligente(nombre, estado)
        else:
            disp = Dispositivo(nombre, tipo, estado)
        conn = get_connection()
        if not conn:
            return None
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Dispositivo (nombre_dispositivo, tipo, estado) VALUES (%s, %s, %s)",
            (disp.nombre, disp.tipo, disp.estado)
        )
        cursor.execute(
            "INSERT INTO Gestion (email_usuario, nombre_dispositivo) VALUES (%s, %s)",
            (usuario_email, disp.nombre)
        )
        conn.commit()
        conn.close()
        return disp

    def listar_por_usuario(self, usuario_obj):
        conn = get_connection()
        if not conn:
            return []
        cursor = conn.cursor()
        cursor.execute(
            "SELECT d.nombre_dispositivo, d.tipo, d.estado "
            "FROM Dispositivo d JOIN Gestion g ON d.nombre_dispositivo = g.nombre_dispositivo "
            "WHERE g.email_usuario = %s", (usuario_obj.email,)
        )
        rows = cursor.fetchall()
        conn.close()
        dispositivos = []
        for r in rows:
            if r[1] == "luz":
                dispositivos.append(LuzInteligente(r[0], r[2]))
            else:
                dispositivos.append(Dispositivo(r[0], r[1], r[2]))
        return dispositivos

    def cambiar_estado(self, usuario_obj, nombre_dispositivo, nuevo_estado):
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Dispositivo d JOIN Gestion g ON d.nombre_dispositivo = g.nombre_dispositivo "
            "SET d.estado=%s WHERE g.email_usuario=%s AND d.nombre_dispositivo=%s",
            (nuevo_estado, usuario_obj.email, nombre_dispositivo)
        )
        conn.commit()
        conn.close()

    def eliminar(self, usuario_obj, nombre_dispositivo):
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM Gestion WHERE email_usuario=%s AND nombre_dispositivo=%s",
            (usuario_obj.email, nombre_dispositivo)
        )
        cursor.execute(
            "DELETE FROM Dispositivo WHERE nombre_dispositivo=%s",
            (nombre_dispositivo,)
        )
        conn.commit()
        conn.close()
