# Rol de Agregar, Eliminar y Listar Dispositivos: Santiago Hidalgo
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


