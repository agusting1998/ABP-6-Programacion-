import dispositivos
import automatizaciones

usuarios = {}

def registrar_usuario_estandar(nombre, apellido, email, rol="usuario"):
    if email in usuarios:
        print("Ya existe un usuario con ese email.")
    else:
        usuarios[email] = {
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "rol": rol
        }
        print(f"Usuario estándar registrado con éxito: {nombre} {apellido} - Rol {rol}")


def obtener_usuarios():
    return usuarios


def mostrar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios estándar registrados: ")
        for usuario in usuarios.values():
            print(f"- {usuario['nombre']} {usuario['apellido']} ({usuario['email']})")


def modificar_rol(email, nuevo_rol):
    if email in usuarios:
        usuarios[email]["rol"] = nuevo_rol
        print(f"Rol de {email} actualizado a '{nuevo_rol}'.")
    else:
        print("Usuario no encontrado")


def mostrar_ayuda():
    print("\n--- Centro de Soporte ---")
    print("1. Si un dispositivo no aparece, verifique que haya sido agregado correctamente.")
    print("2. Use nombres simples y sin espacios para evitar errores.")
    print("3. El modo noche apaga todas las luces y cámaras.")
    print("4. Para asistencia técnica, contacte: soporte@hogarinteligente.com")


def validar_estado(estado):
    estado = estado.lower()
    if estado in ["encendido", "apagado"]:
        return True
    else:
        print("Estado inválido. Use 'encendido' o 'apagado'.")
        return False
