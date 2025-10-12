# main.py

from menu_manager import menu_principal
from usuario import GestorUsuarios, Usuario
from connection import get_connection

gestor = GestorUsuarios()

def cargar_usuarios_desde_db():
    """
    Carga los usuarios y sus dispositivos desde la base de datos al gestor en memoria.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Cargar usuarios
    cursor.execute("SELECT email, nombre, apellido, passw, rol FROM Usuario")
    usuarios_db = cursor.fetchall()
    for email, nombre, apellido, passw, rol in usuarios_db:
        usuario_obj = Usuario(nombre, passw, rol)
        usuario_obj.email = email  # Guardamos el email como atributo
        gestor.usuarios[nombre] = usuario_obj

    # Cargar dispositivos y relaciones
    cursor.execute("""
        SELECT g.email_usuario, d.nombre_dispositivo, d.tipo, d.estado
        FROM Gestion g
        JOIN Dispositivo d ON g.nombre_dispositivo = d.nombre_dispositivo
    """)
    relaciones = cursor.fetchall()
    for email_usuario, nombre_disp, tipo_disp, estado in relaciones:
        # Buscar usuario en memoria
        for usuario_obj in gestor.usuarios.values():
            if getattr(usuario_obj, "email", None) == email_usuario:
                # Crear dispositivo en memoria
                from dispositivos import agregar_dispositivo
                disp_obj = agregar_dispositivo(usuario_obj.dispositivos, nombre_disp, tipo_disp, estado)
                break

    conn.close()

if __name__ == "__main__":
    # Cargar datos de la base al iniciar
    cargar_usuarios_desde_db()
    # Ejecutar menú principal
    menu_principal(gestor)
