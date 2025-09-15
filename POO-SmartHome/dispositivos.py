#Rol compartido entre Diego Mayo, Matias Aranda y Santiago Hidalgo

# Diccionario para almacenar los dispositivos
dispositivos = {}

# Funciones generales
# Funcion para agregar un producto
def agregar_dispositivo(nombre_disp, tipo, estado):
    #validaciones
    if not nombre_disp or not tipo or not estado:
        print("No se permiten campos vacíos.")
    if tipo not in {"luz", "cámara", "electrodoméstico"}:
        print("Error: Tipo no válido. Debe ser: luz, cámara o electrodoméstico.")
        return

    if estado not in {"encendido", "apagado"}:
        print("Error: Estado no válido. Debe ser: encendido o apagado.")
        return
    if nombre_disp in dispositivos:
        print(f'El dispositivo {nombre_disp}, ya existe')
    else:
        dispositivos[nombre_disp] = {"tipo": tipo, "estado": estado}
        print(f'Dispositivo {nombre_disp}, agregado.')
    


# Funcion para eliminar un producto
def eliminar_dispositivo(nombre_disp):
    if nombre_disp in dispositivos:
        del dispositivos[nombre_disp]
        print(f' Dispositivo {nombre_disp}, eliminado.')
    else:
        print(f'El dispositivo {nombre_disp}, no existe.')


# Funcion que lista los productos
def listar_dispositivos():
    if not dispositivos:
        print(f'No hay dispositivos registrados...')
    for nombre_disp, info in dispositivos.items():
        print(f'{nombre_disp} - Tipo: {info["tipo"]}, Estado: {info["estado"]}')


# Funcion para buscar un dispositvo
def buscar_dispositivo(nombre_disp):
    return dispositivos.get(nombre_disp, None)


# Funcion para mostrar los dispositivos almacenados
def obtener_dispositivos():
    return dispositivos


# Función para cambiar el estado del dispositivo (Encendido/Apagado)
def cambiar_estado(nombre_disp, nuevo_estado):
    dispositivo = buscar_dispositivo(nombre_disp)
    if dispositivo:
        dispositivo['estado'] = nuevo_estado
        print(
            f"Estado del dispositivo '{nombre_disp}' cambiado a '{nuevo_estado}'.")
    else:
        print(f"No se encontró el dispositivo '{nombre_disp}'.")


# Función que muestra el estado del dispositivo (Encendido/Apagado)
def ver_estado(nombre_disp):
    dispositivo = buscar_dispositivo(nombre_disp)

    if dispositivo:
        print(f"{nombre_disp}: {dispositivo['estado']}")
    else:
        print(f"Dispositivo '{nombre_disp}' no encontrado..")

# Rol de Consultar Dispositivos Interactivos: Diego Mayo
# ==============================================================================
# INICIO DE APORTE: Consulta interactiva de dispositivos - DIEGO MAYO
# Justificación: Cumple con el punto 2.c de la Evidencia 3, una funcionalidad
# de consulta interactiva que mejora la experiencia del usuario.
# La lógica se basa en conceptos
# como bucles 'while', condicionales 'if/elif/else' y manejo de diccionarios.
# ==============================================================================
def consultar_dispositivos_interactivo():
   while True:
       print("\n--- Consulta de Dispositivos ---")
       hay_dispositivos = listar_dispositivos() # Reutiliza función existente
      
       if not hay_dispositivos:
           input("Presione Enter para volver al menú principal...")
           break


       print("\nOpciones:")
       print("1. Ver estado de un dispositivo específico")
       print("0. Volver al menú principal")


       opcion = input("Seleccione una opción: ").strip()


       if opcion == '1':
           nombre_disp = input("Ingrese el nombre del dispositivo para ver su estado: ").strip()
           if nombre_disp in dispositivos:
               info = dispositivos[nombre_disp]
               print(f"-> Detalle: El dispositivo '{nombre_disp}' ({info['tipo']}) está actualmente '{info['estado']}'.")
           else:
               print(f"El dispositivo '{nombre_disp}' no fue encontrado.")
           input("Presione Enter para continuar...")


       elif opcion == '0':
           break
       else:
           print("Opción no válida.")
# ==============================================================================
# FIN DE APORTE: DIEGO MAYO
# ==============================================================================
# # Test cambio DiegoJosem en una línea nueva.(Por algun motivo no puedo desde VS Code)
