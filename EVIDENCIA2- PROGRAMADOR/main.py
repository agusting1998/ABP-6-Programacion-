#Importamos los modulos
import dispositivos
import automatizaciones
import usuarios
import estado
import soporte
import dispositivos

#Manejamos todo desde el menú interactivo
def menu():
#Mientras la funcion sea verdadera, ingresa al bucle, sale cuando el usuario ingresa la opción "0", ya que se rompe con un break.
    while True:
        print("\n--- Menú ---")
        print("1. Agregar dispositivo")
        print("2. Eliminar dispositivo")
        print("3. Listar dispositivos")
        print("4. Consultar Dispositivo")
        print("5. Cambiar estado")
        print("6. Ver estado")
        print("7. Activar modo noche")
        print("8. Ver todo")
        print("9. Soporte")
        print("0. Salir")

        opcion = input("Selecciones una opcion: ")

#Llamamos a todas las funciones en los módulos
        if opcion == "1":
            nombre = input("Nombre del dispositivo: ")
            tipo = input("Tipo:(luz, camara, electrodoméstico): ")
            estado_ini = input("Estado inicial (encendido/apagado): ")
            dispositivos.agregar_dispositivo(nombre, tipo, estado_ini)
        elif opcion == "2":
            nombre = input("Nombre del dispositivo a eliminar: ")
            dispositivos.eliminar_dispositivo(nombre)
        elif opcion == "3":
            dispositivos.listar_dispositivos()
        elif opcion == "4":
            dispositivos.consultar_dispositivos()
        elif opcion == "5":
            nombre = input("Nombre del dispositivo: ")
            nuevo_estado = input("Nuevo estado (encendido/apagado): ")
            estado.cambiar_estado_dispositivo(nombre, nuevo_estado)
        elif opcion == "6":
            nombre = input("Nombre del dispositivo: ")
            estado.ver_estado_dispositivo(nombre)
        elif opcion == "7":
            automatizaciones.modo_noche()
        elif opcion == "8":
            ver_todo()
        elif opcion == "9":
            soporte.mostrar_ayuda()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción invalida")

#Esta función permite mostrar los dispositivos almacenados en el diccionario.
def ver_todo():
    #La variable "todos" igualamos a la funcion "obtener_dispositivos" y recorremos el diccionario con for
    todos = obtener_dispositivos()
    print("\n--- Dispositivos registrados ---")
    for d in todos:
        print(d)

#Llamamos a la funcion principal, que se encarga de ejecutar la lógica, en este caso las opciones
if __name__ == "__main__":
    menu()
   
    
