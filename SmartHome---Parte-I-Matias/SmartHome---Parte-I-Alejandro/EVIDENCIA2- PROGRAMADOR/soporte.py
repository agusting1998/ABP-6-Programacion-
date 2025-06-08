#Rol del Modulo Soporte: Agustín Gallardo

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
