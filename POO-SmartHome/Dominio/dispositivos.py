# dispositivos.py

# CLASES DE DISPOSITIVOS
class Dispositivo:
    def __init__(self, nombre, device_id, estado_inicial="apagado"):
        self.nombre = nombre
        self.id = device_id
        self.estado = estado_inicial

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ['encendido', 'apagado']:
            self.estado = nuevo_estado
            print(f"El dispositivo '{self.nombre}' cambió su estado a '{nuevo_estado}'.")
            return True
        print("Error: Estado inválido. Use 'encendido' o 'apagado'.")
        return False

    def __str__(self):
        return f'ID: {self.id} | Nombre: {self.nombre} | Estado: {self.estado}'


class LuzInteligente(Dispositivo):
    def __init__(self, nombre, device_id, estado_inicial="apagado", brillo=0):
        super().__init__(nombre, device_id, estado_inicial)
        self.brillo = brillo

    def cambiar_estado(self, nuevo_estado):
        if super().cambiar_estado(nuevo_estado):
            if nuevo_estado == 'encendido':
                self.brillo = 100
            elif nuevo_estado == 'apagado':
                self.brillo = 0
            print(f"'Dispositivo {self.nombre}' cambiado a {nuevo_estado}. Brillo {self.brillo}%")
            return True
        return False

    def __str__(self):
        return f'ID: {self.id} | Nombre: {self.nombre} | Estado: {self.estado} | Brillo: {self.brillo}%'


# FUNCIONES PARA LA LISTA DE DISPOSITIVOS

def agregar_dispositivo(lista_dispositivos, nombre, tipo, estado_inicial="apagado"):
    """
    Agrega un nuevo dispositivo a la lista de dispositivos de un usuario.
    """
    device_id = len(lista_dispositivos) + 1

    if tipo.lower() == "luz inteligente":
        nuevo_disp = LuzInteligente(nombre, device_id, estado_inicial)
    else:
        nuevo_disp = Dispositivo(nombre, device_id, estado_inicial)

    lista_dispositivos.append(nuevo_disp)
    print(f"Dispositivo '{nombre}' agregado exitosamente.")
    return nuevo_disp


def listar_dispositivos(lista_dispositivos):
    """
    Lista todos los dispositivos de un usuario.
    """
    if not lista_dispositivos:
        print("No tienes dispositivos registrados.")
        return

    print("\n--- Tus dispositivos ---")
    for disp in lista_dispositivos:
        print(disp)
    print("------------------------\n")


def eliminar_dispositivo(lista_dispositivos, device_id):
    """
    Elimina un dispositivo por su ID.
    """
    for disp in lista_dispositivos:
        if disp.id == device_id:
            lista_dispositivos.remove(disp)
            print(f"Dispositivo ID {device_id} eliminado exitosamente.")
            return True
    print(f"No se encontró ningún dispositivo con ID {device_id}.")
    return False


def cambiar_estado(lista_dispositivos, device_id, nuevo_estado):
    """
    Cambia el estado de un dispositivo según su ID.
    """
    for disp in lista_dispositivos:
        if disp.id == device_id:
            return disp.cambiar_estado(nuevo_estado)
    print(f"No se encontró ningún dispositivo con ID {device_id}.")
    return False


































# def agregar_dispositivo(nombre_usuario, nombre_dispositivo, tipo_dispositivo, estado_inicial='apagado'):
#     """
#     Agrega un nuevo dispositivo al usuario actual.
#     """
#     if nombre_usuario in USUARIOS:
#         dispositivo_id = len(USUARIOS[nombre_usuario]['dispositivos']) + 1
#         nuevo_dispositivo = {
#             'id': dispositivo_id,
#             'nombre': nombre_dispositivo,
#             'tipo': tipo_dispositivo,
#             'estado': estado_inicial
#         }
#         USUARIOS[nombre_usuario]['dispositivos'].append(nuevo_dispositivo)
#         print(f" Dispositivo '{nombre_dispositivo}' agregado exitosamente.")
#         return True
#     return False

# def listar_dispositivos(nombre_usuario):
#     """
#     Muestra una lista de todos los dispositivos del usuario.
#     """
#     if nombre_usuario in USUARIOS:
#         dispositivos = USUARIOS[nombre_usuario]['dispositivos']
#         if not dispositivos:
#             print(" No tienes dispositivos registrados.")
#             return

#         print("\n--- Tus Dispositivos ---")
#         for disp in dispositivos:
#             print(f"ID: {disp['id']} | Nombre: {disp['nombre']} | Tipo: {disp['tipo']} | Estado: {disp['estado']}")
#         print("-----------------------\n")
#     else:
#         print(" Error: Usuario no encontrado.")

# def eliminar_dispositivo(nombre_usuario, dispositivo_id):
#     """
#     Elimina un dispositivo por su ID.
#     """
#     if nombre_usuario in USUARIOS:
#         dispositivos = USUARIOS[nombre_usuario]['dispositivos']
#         for disp in dispositivos:
#             if disp['id'] == dispositivo_id:
#                 dispositivos.remove(disp)
#                 print(f"Dispositivo ID {dispositivo_id} eliminado exitosamente.")
#                 return True
#         print(f"Error: No se encontró un dispositivo con el ID {dispositivo_id}.")
#         return False
#     return False

# def buscar_dispositivo(nombre_usuario, nombre_dispositivo):
#     """
#     Busca un dispositivo por su nombre.
#     """
#     if nombre_usuario in USUARIOS:
#         dispositivos = USUARIOS[nombre_usuario]['dispositivos']
#         for disp in dispositivos:
#             if disp['nombre'] == nombre_dispositivo:
#                 print(f"Dispositivo encontrado: ID {disp['id']} | Nombre: {disp['nombre']} | Tipo: {disp['tipo']} | Estado: {disp['estado']}")
#                 return disp
#         print(f" Dispositivo '{nombre_dispositivo}' no encontrado.")
#         return None
#     return None

# def cambiar_estado(nombre_usuario, dispositivo_id, nuevo_estado):
#     """
#     Cambia el estado de un dispositivo (encendido/apagado).
#     """
#     if nombre_usuario in USUARIOS:
#         dispositivos = USUARIOS[nombre_usuario]['dispositivos']
#         for disp in dispositivos:
#             if disp['id'] == dispositivo_id:
#                 disp['estado'] = nuevo_estado
#                 print(f" El estado de '{disp['nombre']}' ha cambiado a '{nuevo_estado}'.")
#                 return True
#         print(f"Error: Dispositivo ID {dispositivo_id} no encontrado.")
#         return False

#     return False


# def ver_estado(nombre_usuario, nombre_dispositivo):
#     """
#     Muestra el estado de un dispositivo específico de un usuario.
#     """
#     if nombre_usuario in USUARIOS:
#         dispositivos = USUARIOS[nombre_usuario]['dispositivos']
#         for disp in dispositivos:
#             if disp['nombre'] == nombre_dispositivo:
#                 print(f" El dispositivo '{disp['nombre']}' está actualmente '{disp['estado']}'.")
#                 return disp['estado']
#         print(f"Error: Dispositivo '{nombre_dispositivo}' no encontrado.")
#         return None
#     else:
#         print(" Error: Usuario no encontrado.")
#         return None
