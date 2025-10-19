import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Conn'))
from db_conn import get_connection

class Dispositivo:
    _id_counter = 1

    def __init__(self, nombre, tipo, estado="apagado"):
        self.id = Dispositivo._id_counter
        Dispositivo._id_counter += 1
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado

class LuzInteligente(Dispositivo):
    def __init__(self, nombre, estado="apagado"):
        super().__init__(nombre, "luz", estado)

def agregar_dispositivo(usuario_email, nombre, tipo, estado="apagado"):
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
        return disp
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
        return None
    finally:
        cursor.close()
        conn.close()

def listar_dispositivos(usuario_obj):
    conn = get_connection()
    if not conn:
        print("Error de conexión.")
        return
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT d.nombre_dispositivo, d.tipo, d.estado "
            "FROM Dispositivo d JOIN Gestion g ON d.nombre_dispositivo = g.nombre_dispositivo "
            "WHERE g.email_usuario = %s", (usuario_obj.email,)
        )
        rows = cursor.fetchall()
        if not rows:
            print("No hay dispositivos registrados.")
        else:
            print("\n--- Dispositivos Registrados ---")
            for idx, (nombre, tipo, estado) in enumerate(rows, start=1):
                print(f"  {idx}. {nombre} | Tipo: {tipo} | Estado: {estado}")
    finally:
        cursor.close()
        conn.close()

def cambiar_estado(usuario_obj, nombre_dispositivo, nuevo_estado):
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
        print(f"{nombre_dispositivo} ahora está {nuevo_estado}.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def eliminar_dispositivo(usuario_obj, nombre_dispositivo):
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
        print(f"Dispositivo {nombre_dispositivo} eliminado.")
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
