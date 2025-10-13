BASE DE DATOS: POO-SmartHome

Este archivo documenta los scripts SQL para la base de datos
del proyecto del Hogar Inteligente.

Contiene:
1. DDL.sql (Data Definition Language) - Estructura.
2. DML.sql (Data Manipulation Language) - Datos de inicio.


1. DDL.sql (Data Definition Language)


DESCRIPCION:
Define la estructura completa de la base de datos,
incluyendo todas las tablas, columnas, claves primarias
(PK) y claves foráneas (FK) que aseguran la integridad
referencial.

ESTRUCTURA DE TABLAS:

* TABLA USUARIO:
  - Almacena datos de acceso y roles (admin/usuario).
  - PK: email

* TABLA DISPOSITIVO:
  - Almacena los aparatos físicos (luz, cámara, termostato).
  - PK: nombre_dispositivo

* TABLA AUTOMATIZACION:
  - Define las rutinas o escenas (ej. "Modo Noche").
  - PK: nombre_automatizacion

* TABLA GESTION (Relación N:M):
  - Define qué Usuario tiene control sobre qué Dispositivo.
  - PK: (email_usuario, nombre_dispositivo)
  - FKs: a Usuario y Dispositivo.

* TABLA ACTIVACION (Relación N:M + Timestamp):
  - Registra quién y cuándo activó una Automatización.
  - PK: (email_usuario, nombre_automatizacion, fecha_activacion)
  - FKs: a Usuario y Automatizacion.

* TABLA CONTROL (Relación N:M):
  - Define qué Dispositivo es afectado por una Automatizacion.
  - PK: (nombre_automatizacion, nombre_dispositivo)
  - FKs: a Automatizacion y Dispositivo.

PASOS DE EJECUCION:
1. CREAR la base de datos 'hogar_inteligente'.
2. Crear las 6 tablas principales.
3. Establecer las Claves Foráneas para asegurar las relaciones.


2. DML.sql (Data Manipulation Language)


DESCRIPCION:
Inserta datos iniciales (datos semilla o 'seed data') para
permitir la prueba inmediata del sistema. Estos datos
simulan la configuración inicial del SmartHome.

CONTENIDO DE LA INSERCION:

* USUARIO: 5 registros (3 administradores y 2 usuarios normales).
* DISPOSITIVO: 15 registros (luces, cámaras, electrodomésticos, etc.).
* AUTOMATIZACION: 5 rutinas predefinidas.
* GESTION: 8 asignaciones de dispositivos a usuarios.
* ACTIVACION: 5 registros de activaciones históricas.
* CONTROL: 10 relaciones que definen qué dispositivos son parte de las rutinas ("Modo Noche" y "Modo Día").

COMO USAR ESTOS SCRIPTS:

1. Conéctate a tu gestor de base de datos (MySQL/MariaDB).
2. Ejecuta el contenido completo del archivo DDL.sql.
3. Ejecuta el contenido completo del archivo DML.sql.

La base de datos 'hogar_inteligente' estará lista para ser usada por la aplicación POO-SmartHome.




3. COMO EJECUTAR EN ONE COMPILER (O SIMILAR)


Debido a que los compiladores SQL online como One Compiler
(https://onecompiler.com/mysql) generalmente no permiten crear
bases de datos (CREATE DATABASE) ni seleccionarlas (USE),
debemos adaptar el script para que solo contenga la creacion
de tablas, la insercion de datos y la verificacion final.

PASOS:
1.  Abre un entorno de MySQL online (ej. One Compiler).
2.  Copia y pega el **código SQL completo** de los archivos DML y DLL dentro de la carpeta "db-onecompiler"
    (DDL + DML + SELECT) en el editor.
3.  Presiona el boton "Run" o "Ejecutar".

El resultado mostrara:
a)  Mensajes de exito en la creacion de las 6 tablas.
b)  Mensajes de exito en la insercion de todos los datos.
c)  Las 6 tablas resultantes (Usuario, Dispositivo, etc.)
    mediante las sentencias SELECT al final del script.

