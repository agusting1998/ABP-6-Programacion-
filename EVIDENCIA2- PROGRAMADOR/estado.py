import dispositivos

#Función para cambiar el estado del dispositivo (Encendido/Apagado)
def cambiar_estado(nombre, nuevo_estado):
    dispositivo = dispositivos.buscar_dispositivo(nombre)
    if dispositivo:
        dispositivo['estado'] = nuevo_estado
        print(f"Estado del dispositivo '{nombre}' cambiado a '{nuevo_estado}'.")
    else:
        print(f"No se encontró el dispositivo '{nombre}'.")

#Función que muestra el estado del dispositivo (Encendido/Apagado)
def ver_estado(nombre):
    dispositivo = dispositivos.buscar_dispositivo(nombre)

    if dispositivo:
        print(f"{nombre}: {dispositivo['estado']}")
    else:
        print(f"Dispositivo '{nombre}' no encontrado..")