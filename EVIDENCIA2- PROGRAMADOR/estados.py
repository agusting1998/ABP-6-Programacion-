from dispositivos import obtener_dispositivos

def ver_estado_dispositivo(nombre):
    dispositivos = obtener_dispositivos()
    for dispositivo in dispositivos:
        if dispositivo["nombre"] == nombre:
            print(f"Estado de {nombre}: {dispositivo['estado']}")
            return
    print(f"No se encontró un dispositivo llamado '{nombre}'.")
