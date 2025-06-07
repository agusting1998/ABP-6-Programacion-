#Asignar Rol de Estados: Agustín Gallardo

from dispositivos import obtener_dispositivos

def ver_estado_dispositivo(nombre):
    dispositivos = obtener_dispositivos()
    for dispositivo in dispositivos:
        if dispositivo["nombre"] == nombre:
            print(f"Estado de {nombre}: {dispositivo['estado']}")
            return
    print(f"No se encontró un dispositivo llamado '{nombre}'.")

def cambiar_estado_dispositivo(nombre, nuevo_estado):
    dispositivos = obtener_dispositivos()
    for dispositivo in dispositivos:
        if dispositivo["nombre"] == nombre:
            dispositivo["estado"] = nuevo_estado
            print(f"El estado de {nombre} ha sido cambiado a: {nuevo_estado}")
            return
    print(f"No se encontró un dispositivo llamado '{nombre}'.")
