LOGICA POO Y ESTRUCTURA DEL PROYECTO

Este documento describe la arquitectura del proyecto POO-SmartHome,
centrandose en la Programacion Orientada a Objetos (POO) y su
interaccion con la base de datos (persistencia).

El proyecto se organiza en los siguientes directorios principales:

* Dominio/: Contiene la logica de negocio (Clases y Funciones).
* Dao/: Contiene las clases de acceso a datos (CRUD SQL).
* Conn/: Contiene la configuracion de la conexion a la base de datos.
* test/: Contiene las pruebas unitarias (Unit Tests).

1. DOMINIO (LOGICA POO Y REGLAS DEL SISTEMA)

El directorio Dominio/ encapsula la logica de negocio a traves
de clases que representan los conceptos clave del Hogar Inteligente.

1.1. usuario.py (Clases Usuario y GestorUsuarios)

CLASE USUARIO:
Es la Entidad principal. Representa a un usuario individual (estandar o admin).
ATRIBUTOS: nombre, passw, rol, email.
METODOS: consultar_datos_personales(), modificar_rol().

CLASE GESTORUSUARIOS:
Es una clase Control/Manager. Administra la coleccion de objetos Usuario.
METODOS: registrar_usuario(), iniciar_sesion(). Para la persistencia,
delega las operaciones a usuario_dao.py (en el directorio Dao/).

1.2. dispositivos.py (Clases Dispositivo y LuzInteligente)

CLASE DISPOSITIVO:
Es la Entidad base. Clase padre para todos los aparatos del hogar.
ATRIBUTOS: nombre, tipo, estado.
ABSTRACCION: Usa un contador estatico para asignar IDs unicos en memoria.

CLASE LUZINTELIGENTE (HERENCIA):
Es una Entidad especializada. Extiende Dispositivo para manejar las propiedades
especificas de una luz (ej. brillo).
RELACION: Hereda de Dispositivo (LuzInteligente es un Dispositivo).

Persistencia:
Las funciones o acciones relacionadas se delegan a dispositivo_dao.py
(en el directorio Dao/) para realizar operaciones INSERT, SELECT, DELETE, etc.

1.3. automatizaciones.py (Clase ControlAutomatizaciones)

CLASE CONTROLAUTOMATIZACIONES:
Es una clase Control/Servicio. Ejecuta rutinas que afectan a multiples dispositivos.
METODOS: modo_ahorro_energia(), modo_noche(), guardar_activacion().
LOGICA POO: Modifica objetos Dispositivo y registra la activacion mediante
automatizacion_dao.py (en Dao/).

1.4. menu_manager.py y soporte.py

MENU_MANAGER.PY:
Responsable de la Interfaz de Usuario (UI) por consola. Orquesta las clases del Dominio
y llama a los DAO segun sea necesario.

SOPORTE.PY:
Contiene funciones utilitarias (validar_estado, mostrar_ayuda), separando la logica
auxiliar de la logica principal.

2. DAO (PERSISTENCIA Y CRUD)

El directorio Dao/ contiene los modulos que realizan operaciones directas sobre la
base de datos. Cada entidad cuenta con su propio archivo.

2.1. usuario_dao.py
Maneja la tabla Usuario. Metodos tipicos: agregar(), buscar_por_email(), listar().

2.2. dispositivo_dao.py
Maneja tablas relacionadas con Dispositivos. Metodos: insertar(), eliminar(), listar().

Todos estos modulos se conectan a la BD mediante la capa Conn/.

3. CONN (CONEXION A LA BASE DE DATOS)

El directorio Conn/ centraliza la configuracion y creacion de conexiones.

3.1. db_conn.py
Define funciones como get_connection() para conectar con MySQL
(host, usuario, contraseña, base de datos).
Es reutilizado por todos los archivos DAO.

4. TESTS (PRUEBAS UNITARIAS)

El directorio test/ contiene pruebas que validan la logica interna del Dominio
y la correcta interaccion con los DAO utilizando mocks.

4.1. TestAutomatizaciones
PROPOSITO: Verificar que las rutinas modifiquen el estado de los dispositivos
(ej. Modo Noche).
MOCKING: Usa DispositivoMock, UsuarioMock.

4.2. TestDispositivos (Logica POO)
PROPOSITO: Validar herencia y comportamiento de Dispositivo y LuzInteligente.
PRUEBAS: Se comprueba que los metodos especializados funcionen correctamente.

4.4. TestMenuManager / TestSoporte / TestUsuario
PROPOSITO: Verificar flujo del menu, funciones utilitarias y registro/inicio
de sesion de usuarios.
MOCKING: Se simula input() y se captura sys.stdout para chequear salidas.