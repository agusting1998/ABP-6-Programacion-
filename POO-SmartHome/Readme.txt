LOGICA POO Y ESTRUCTURA DEL PROYECTO

Este documento describe la arquitectura del proyecto POO-SmartHome,
centrandose en la Programacion Orientada a Objetos (POO) y su
interaccion con la base de datos (persistencia).

El proyecto se divide en dos directorios principales:
- Dominio/: Contiene la logica de negocio (Clases y Funciones).
- test/: Contiene las pruebas unitarias (Unit Tests).

1. DOMINIO (LOGICA POO Y PERSISTENCIA)

El directorio Dominio/ encapsula la logica de negocio a traves
de clases que representan los conceptos clave del Hogar Inteligente.

1.1. usuario.py (Clases Usuario y GestorUsuarios)

CLASE USUARIO:
  Es la Entidad principal. Representa a un usuario individual (estandar o admin).
  ATRIBUTOS: nombre, passw, rol, email.
  METODOS: consultar_datos_personales(), modificar_rol().

CLASE GESTORUSUARIOS:
  Es una clase Control/Manager. Administra la coleccion de objetos Usuario.
  METODOS: registrar_usuario(), iniciar_sesion(). Ambos interactuan con la tabla Usuario de la BD.

1.2. dispositivos.py (Clases Dispositivo y LuzInteligente)

CLASE DISPOSITIVO:
  Es la Entidad base. Clase base para todos los aparatos del hogar.
  ATRIBUTOS: nombre, tipo, estado.
  ABSTRACCION: Usa un contador estatico para asignar IDs unicos a cada objeto en memoria.

CLASE LUZINTELIGENTE (HERENCIA):
  Es una Entidad especializada. Extiende Dispositivo para manejar las propiedades especificas de una luz (ej. brillo).
  RELACION: Hereda de Dispositivo (LuzInteligente es un Dispositivo).

FUNCIONES DE MODULO:
  El modulo utiliza funciones (ej. agregar_dispositivo, listar_dispositivos, eliminar_dispositivo) para la mayoria de las operaciones de persistencia (INSERT, SELECT, DELETE en las tablas Dispositivo y Gestion).

1.3. automatizaciones.py (Clase ControlAutomatizaciones)

CLASE CONTROLAUTOMATIZACIONES:
  Es una clase Control/Servicio. Ejecuta rutinas predefinidas que afectan a multiples dispositivos.
  METODOS: modo_ahorro_energia(), modo_noche(), guardar_activacion().
  LOGICA POO: Delega la modificacion de estado a los objetos Dispositivo dentro de la coleccion que posee el objeto Usuario. Registra la activacion en la tabla Activacion.

1.4. connection.py (Persistencia)

RESPONSABILIDAD: Gestiona la conexion y comunicacion con la base de datos MySQL.
FUNCION GET_CONNECTION(): Encapsula los detalles de conexion (host, user, passw, database) y maneja la deteccion de errores. Permite la persistencia en todo el Dominio.

1.5. main.py / menu_manager.py / soporte.py

MAIN.PY: Punto de entrada.
MENU_MANAGER.PY: Responsable de la Interfaz de Usuario (UI). Une las clases del Dominio en respuesta a la interaccion del usuario.
SOPORTE.PY: Contiene funciones utilitarias (validar_estado, mostrar_ayuda), separando la logica de soporte de la logica principal.

2. TESTS (PRUEBAS UNITARIAS)

El directorio test/ contiene pruebas que validan la logica interna de las
clases del Dominio, utilizando la tecnica de Mocking para aislar el codigo.

2.1. TestControlAutomatizaciones
  PROPOSITO: Asegurar que las rutinas de automatizacion modifiquen el estado de los dispositivos segun lo esperado (ej. Modo Noche apaga luces y enciende camaras).
  MOCKING: Usa clases Mock (DispositivoMock, UsuarioMock) para simular el entorno sin conectarse a la BD.

2.2. TestClasesDispositivo (Logica POO)
  PROPOSITO: Validar la correcta inicializacion, herencia y metodos de las clases Dispositivo y LuzInteligente.
  PRUEBAS CLAVE: Verifica que LuzInteligente herede de Dispositivo y que sus metodos especializados (ej. cambiar estado afectando el brillo) funcionen correctamente.

2.3. TestFuncionesDispositivo (Logica de Persistencia)
  PROPOSITO: Originalmente probaba funciones que operaban sobre listas. En la implementacion actual con SQL, se centraria en probar la interaccion con la BD. (Nota: Para un testing ideal, estas pruebas deberian simular las llamadas a la BD usando 'patch').

2.4. TestMenuManager / TestSoporte / TestUsuario
  PROPOSITO: Validar el flujo del menu, las funciones de utilidad y la gestion de usuarios.
  MOCKING: Utiliza 'patch' para simular la entrada del usuario ('builtins.input') y capturar la salida en consola ('sys.stdout') para verificar que los mensajes y las acciones del menu sean correctas.