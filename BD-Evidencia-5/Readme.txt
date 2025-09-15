Guía de Ejecución de Scripts SQL
Este documento te guiará a través de los pasos necesarios para ejecutar los scripts DDL y DML de la base de datos hogar_inteligente usando MySQL Workbench o en One Compiler (el gestor de base de datos que utilizamos en el grupo).




a) Requisitos

Tener acceso a una base de datos MySQL (ya sea local o en la nube).
Tener instalado MySQL Workbench o una herramienta similar (por ejemplo, DBeaver, HeidiSQL).



b) Pasos para la Ejecución (MySQL Workbench)

1. Ejecutar el Script DDL (Definición de Datos)
El script ddl_script.sql es el que crea la estructura de la base de datos y todas sus tablas. Es crucial que este script se ejecute primero.

Abre MySQL Workbench y conéctate a tu instancia de MySQL.
Haz clic en File -> Open SQL Script... y selecciona el archivo ddl_script.sql.
Una vez que el script esté abierto, haz clic en el botón de "ejecutar" (el icono del rayo) o presiona Ctrl + Shift + Enter.
Si el script se ejecuta correctamente, verás un mensaje de éxito. Esto significa que la base de datos hogar_inteligente y todas sus tablas han sido creadas.

2. Ejecutar el Script DML (Manipulación de Datos)
El script dml_script.sql es el que llena la base de datos con los registros de prueba que hemos creado. Este script debe ejecutarse después del DDL para evitar errores.
En MySQL Workbench, asegúrate de que estás conectado a la base de datos hogar_inteligente. Puedes hacerlo haciendo doble clic en el nombre de la base de datos en el panel del lado izquierdo.
Haz clic en File -> Open SQL Script... y selecciona el archivo dml_script.sql.
Una vez que el script esté abierto, haz clic en el botón de "ejecutar" (el icono del rayo) o presiona Ctrl + Shift + Enter.
Si la ejecución es exitosa, todos los datos de prueba habrán sido insertados en las tablas.

c) Aclaraciones en la ejecucion (OneCompiler)

- Se adopta la herramienta de OneCompiler dado a que es la que mejor se adapta a la hora de ejecutar el codigo.
- Se creo un directorio, con el codigo adaptado para esa plataforma.
- En DLL, se hicieron cambios minimos como; eliminar CREATE DATABASE y USE, para su correcta ejecucion.
- En DML, agregamos SELECT al final del codigo, para la correcta visualizacion de las tablas. 

Nota Importante

El script ddl_script.sql incluye la línea DROP DATABASE IF EXISTS hogar_inteligente; al inicio. Esto es para evitar errores de duplicados si lo ejecutas varias veces. Al ejecutar el DDL, la base de datos anterior se eliminará y se creará una nueva, permitiendo que el script DML se ejecute sin problemas.

