#Diccionario para almacenar los dispositivos
dispositivos = {}

#Funciones generales
#Funcion para agregar un producto
def agregar_dispositivo(nombre, tipo, estado):
    if nombre in dispositivos:
        print(f'El dispositivo {nombre}, ya existe')
    else:
        dispositivos[nombre] = {"tipo": tipo, "estado": estado}
        print(f'Dispositivo {nombre}, agregado.')

#Funcion para eliminar un producto
def eliminar_dispositivo(nombre):
    if nombre in dispositivos:
        del dispositivos[nombre]
        print(f' Dispositivo {nombre}, eliminado.')
    else:
        print(f'El dispositivo{nombre}, no existe.')

#Funcion que lista los productos
def listar_dispositivos():
    if not dispositivos:
        print(f'No hay dispositivos registrados...')
    for nombre, info in dispositivos.items():
        print(f'{nombre} - Tipo: {info["tipo"]}, Estado: {info["estado"]}')

#Funcion para buscar un dispositvo
def buscar_dispositivo(nombre):
    return dispositivos.get(nombre, None)

#Funcion para mostrar los dispositivos almacenados
def obtener_dispositivos():
    return dispositivos