# Diccionario para almacenar los dispositivos
dispositivos = {}

<<<<<<< HEAD
# Funciones generales
# Funcion para agregar un producto
def agregar_dispositivo(nombre, tipo, estado):
    #validaciones
    if not nombre or not tipo or not estado:
        print("No se permiten campos vacíos.")

=======
#--------------Funciones generales-----------

#Funcion para agregar un producto
def agregar_dispositivo(nombre, tipo, estado):
    #Validaciones
    if not nombre or not tipo or not estado:
        print("❌ No se permiten campos vacíos.")
        return
    if tipo not in ("luz, camara, electrodomestico"):
        print("❌Tipo no válido, debe ser luz, camara, electrodomestico.")
        return
    if estado not in ("encendido", "apagado"):
        print("❌ Estado no válido. Debe ser: encendido o apagado.")
        return
    
>>>>>>> dispositivos-validaciones
    if nombre in dispositivos:
        print(f'El dispositivo {nombre}, ya existe')
    else:
        dispositivos[nombre] = {"tipo": tipo, "estado": estado}
        print(f'Dispositivo {nombre}, agregado.')
    

<<<<<<< HEAD

# Funcion para eliminar un producto
=======
#Funcion para eliminar un producto--------------
>>>>>>> dispositivos-validaciones
def eliminar_dispositivo(nombre):
    if nombre in dispositivos:
        del dispositivos[nombre]
        print(f' Dispositivo {nombre}, eliminado.')
    else:
        print(f'El dispositivo {nombre}, no existe.')

<<<<<<< HEAD

# Funcion que lista los productos
=======
#Funcion que lista los productos-------------------
>>>>>>> dispositivos-validaciones
def listar_dispositivos():
    if not dispositivos:
        print(f'No hay dispositivos registrados...')
    for nombre, info in dispositivos.items():
        print(f'{nombre} - Tipo: {info["tipo"]}, Estado: {info["estado"]}')


# Funcion para buscar un dispositvo
def buscar_dispositivo(nombre):
    return dispositivos.get(nombre, None)


# Funcion para mostrar los dispositivos almacenados
def obtener_dispositivos():
    return dispositivos

<<<<<<< HEAD

# Función para cambiar el estado del dispositivo (Encendido/Apagado)
def cambiar_estado(nombre, nuevo_estado):
    dispositivo = dispositivos.buscar_dispositivo(nombre)
    if dispositivo:
        dispositivo['estado'] = nuevo_estado
        print(
            f"Estado del dispositivo '{nombre}' cambiado a '{nuevo_estado}'.")
    else:
        print(f"No se encontró el dispositivo '{nombre}'.")


# Función que muestra el estado del dispositivo (Encendido/Apagado)
def ver_estado(nombre):
    dispositivo = dispositivos.buscar_dispositivo(nombre)
=======
#Función para cambiar el estado del dispositivo (Encendido/Apagado)
def cambiar_estado(nombre, nuevo_estado):
    dispositivo = buscar_dispositivo(nombre)
    if dispositivo:
        dispositivo['estado'] = nuevo_estado
        print(f"Estado del dispositivo '{nombre}' cambiado a '{nuevo_estado}'.")
    else:
        print(f"No se encontró el dispositivo '{nombre}'.")

#Función que muestra el estado del dispositivo (Encendido/Apagado)
def ver_estado(nombre):
    dispositivo = buscar_dispositivo(nombre)
>>>>>>> dispositivos-validaciones

    if dispositivo:
        print(f"{nombre}: {dispositivo['estado']}")
    else:
<<<<<<< HEAD
        print(f"Dispositivo '{nombre}' no encontrado..")
=======
        print(f"Dispositivo '{nombre}' no encontrado..")
>>>>>>> dispositivos-validaciones
