#Menu Main - Rol Asignado a Matias Aranda.

#Importamos los modulos
import dispositivos
import automatizaciones
import soporte
import dispositivos
import usuario
import admin

#Manejamos todo desde el menú interactivo
def menu():
#Mientras la funcion sea verdadera, ingresa al bucle, sale cuando el usuario ingresa la opción "0", ya que se rompe con un break.
    while True:
        print("\n--- Menú ---")
        print("A. Registrar usuario")
        print("B. Registrar usuario admin")
        print("1. Agregar dispositivo")
        print("2. Eliminar dispositivo")
        print("3. Listar dispositivos")
        print("4. Cambiar estado")
        print("5. Ver estado")
        print("6. Activar modo noche")
        print("7. Soporte")
        print("0. Salir")

        opcion = input("Selecciones una opcion: ")

#Llamamos a todas las funciones en los módulos
        if opcion == "A":
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            email = input("Ingrese su email: ")
            usuario.registrar_usuario_estandar(nombre, apellido, email)
            usuario.mostrar_usuarios()
            usuario.menu_usuario_estandar(nombre)
        elif opcion == "B":
            usuario_nombre = input("Ingrese su nombre de usuario: ")
            usuario_pass = input("Ingrese su contraseña: ")
            admin.registrar_y_loguear_admin()
            admin.menu_principal()
        elif opcion == "1":
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
            nombre = input("Nombre del dispositivo: ")
            nuevo_estado = input("Nuevo estado (encendido/apagado): ")
            dispositivos.cambiar_estado(nombre, nuevo_estado)
        elif opcion == "5":
            nombre = input("Nombre del dispositivo: ")
            dispositivos.ver_estado(nombre)
        elif opcion == "6":
            automatizaciones.modo_noche()
        elif opcion == "7":
            soporte.mostrar_ayuda()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción invalida")


#Llamamos a la funcion principal, que se encarga de ejecutar la lógica, en este caso las opciones
if __name__ == "__main__":
    menu()
   
    
