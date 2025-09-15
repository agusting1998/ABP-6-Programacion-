
from data import USUARIOS

def agregar_dispositivo(nombre_usuario, nombre_dispositivo, tipo_dispositivo, estado_inicial='apagado'):
    """
    Agrega un nuevo dispositivo al usuario actual.
    """
    if nombre_usuario in USUARIOS:
        dispositivo_id = len(USUARIOS[nombre_usuario]['dispositivos']) + 1
        nuevo_dispositivo = {
            'id': dispositivo_id,
            'nombre': nombre_dispositivo,
            'tipo': tipo_dispositivo,
            'estado': estado_inicial
        }
        USUARIOS[nombre_usuario]['dispositivos'].append(nuevo_dispositivo)
        print(f" Dispositivo '{nombre_dispositivo}' agregado exitosamente.")
        return True
    return False

def listar_dispositivos(nombre_usuario):
    """
    Muestra una lista de todos los dispositivos del usuario.
    """
    if nombre_usuario in USUARIOS:
        dispositivos = USUARIOS[nombre_usuario]['dispositivos']
        if not dispositivos:
            print(" No tienes dispositivos registrados.")
            return

        print("\n--- Tus Dispositivos ---")
        for disp in dispositivos:
            print(f"ID: {disp['id']} | Nombre: {disp['nombre']} | Tipo: {disp['tipo']} | Estado: {disp['estado']}")
        print("-----------------------\n")
    else:
        print(" Error: Usuario no encontrado.")

def eliminar_dispositivo(nombre_usuario, dispositivo_id):
    """
    Elimina un dispositivo por su ID.
    """
    if nombre_usuario in USUARIOS:
        dispositivos = USUARIOS[nombre_usuario]['dispositivos']
        for disp in dispositivos:
            if disp['id'] == dispositivo_id:
                dispositivos.remove(disp)
                print(f"🗑️ Dispositivo ID {dispositivo_id} eliminado exitosamente.")
                return True
        print(f"Error: No se encontró un dispositivo con el ID {dispositivo_id}.")
        return False
    return False

def buscar_dispositivo(nombre_usuario, nombre_dispositivo):
    """
    Busca un dispositivo por su nombre.
    """
    if nombre_usuario in USUARIOS:
        dispositivos = USUARIOS[nombre_usuario]['dispositivos']
        for disp in dispositivos:
            if disp['nombre'] == nombre_dispositivo:
                print(f"🔍 Dispositivo encontrado: ID {disp['id']} | Nombre: {disp['nombre']} | Tipo: {disp['tipo']} | Estado: {disp['estado']}")
                return disp
        print(f" Dispositivo '{nombre_dispositivo}' no encontrado.")
        return None
    return None

def cambiar_estado_dispositivo(nombre_usuario, dispositivo_id, nuevo_estado):
    """
    Cambia el estado de un dispositivo (encendido/apagado).
    """
    if nombre_usuario in USUARIOS:
        dispositivos = USUARIOS[nombre_usuario]['dispositivos']
        for disp in dispositivos:
            if disp['id'] == dispositivo_id:
                disp['estado'] = nuevo_estado
                print(f" El estado de '{disp['nombre']}' ha cambiado a '{nuevo_estado}'.")
                return True
        print(f"Error: Dispositivo ID {dispositivo_id} no encontrado.")
        return False
    return False