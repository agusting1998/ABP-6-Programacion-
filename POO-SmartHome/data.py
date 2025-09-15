USUARIOS = {}
"""
Almacena la información de los usuarios.
Formato:
{
    'nombre_usuario': {
        'contrasena': '...',
        'rol': 'estandar' | 'admin',
        'dispositivos': [
            {'id': 1, 'nombre': 'Luz Sala', 'tipo': 'luz', 'estado': 'encendido'},
            ...
        ]
    }
}
"""