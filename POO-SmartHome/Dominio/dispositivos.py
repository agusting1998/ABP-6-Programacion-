# dispositivos.py

class Dispositivo:
    _id_counter = 1

    def __init__(self, nombre, tipo, estado="apagado"):
        self.id = Dispositivo._id_counter
        Dispositivo._id_counter += 1
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado


# Ejemplo de clases especializadas (puedes agregar más)
class LuzInteligente(Dispositivo):
    def __init__(self, nombre, estado="apagado"):
        super().__init__(nombre, "luz", estado)


def agregar_dispositivo(lista_dispositivos, nombre, tipo, estado="apagado"):
    """
    Crea un dispositivo y lo agrega a la lista.
    """
    # Crear instancia según tipo
    if tipo.lower() == "luz":
        disp = LuzInteligente(nombre, estado)
    else:
        disp = Dispositivo(nombre, tipo, estado)
    lista_dispositivos.append(disp)
    return disp


def listar_dispositivos(lista_dispositivos):
    if not lista_dispositivos:
        print("No hay dispositivos registrados.")
    else:
        print("\nDispositivos registrados:")
        for d in lista_dispositivos:
            print(f"ID: {d.id} | Nombre: {d.nombre} | Tipo: {d.tipo} | Estado: {d.estado}")


def cambiar_estado(lista_dispositivos, dispositivo_id, nuevo_estado):
    for d in lista_dispositivos:
        if d.id == dispositivo_id:
            d.estado = nuevo_estado
            print(f"{d.nombre} ahora está {nuevo_estado}.")
            return True
    print("Dispositivo no encontrado.")
    return False


def eliminar_dispositivo(lista_dispositivos, dispositivo_id):
    for d in lista_dispositivos:
        if d.id == dispositivo_id:
            lista_dispositivos.remove(d)
            print(f"Dispositivo {d.nombre} eliminado.")
            return True
    print("Dispositivo no encontrado.")
    return False
