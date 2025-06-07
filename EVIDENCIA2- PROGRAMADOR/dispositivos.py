# Funciones para dispositivos (solo admin)
def agregar_dispositivo(nombre, tipo, estado):
    if not nombre or not tipo or not estado:
        print("Todos los campos son obligatorios.")
        return
    if tipo not in {"luz", "camara", "electrodomestico"}:
        print("Tipo no válido. Use luz, cámara o electrodomestico.")
        return
    if estado not in {"encendido", "apagado"}:
        print("Estado no válido. Use encendido o apagado.")
        return
    if nombre in dispositivos:
        print("El dispositivo ya existe.")
        return
    dispositivos[nombre] = {"tipo": tipo, "estado": estado}
    print("Dispositivo agregado correctamente.")

def eliminar_dispositivo(nombre):
    if nombre in dispositivos:
        del dispositivos[nombre]
        print("Dispositivo eliminado correctamente.")
    else:
        print("Dispositivo no encontrado.")

def listar_dispositivos():
    if not dispositivos:
        print("No hay dispositivos registrados.")
        return
    for nombre, info in dispositivos.items():
        print(f"{nombre} - Tipo: {info['tipo']}, Estado: {info['estado']}")
