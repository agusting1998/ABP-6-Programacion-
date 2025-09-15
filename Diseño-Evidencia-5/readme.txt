=========================================================
  JUSTIFICACIÓN DEL DISEÑO ORIENTADO A OBJETOS (POO)
         PARA EL SISTEMA POO-SMARTHOME
=========================================================

El siguiente documento justifica el diseño de clases propuesto para el proyecto POO-SmartHome. El objetivo es transformar la estructura actual, basada en módulos funcionales, en un modelo robusto de clases y objetos, aplicando los principios fundamentales de la Programación Orientada a Objetos para mejorar la organización, mantenibilidad y escalabilidad del sistema.


1. ABSTRACCIÓN: DE ENTIDADES A CLASES
---------------------------------------
El primer paso en el diseño es identificar las entidades fundamentales del sistema y abstraerlas en clases. El modelado de software se basa en representar los conceptos clave del dominio del problema como objetos en el programa.

Aplicación en el Diseño:
*   Clase `Usuario`: Es una abstracción directa de la entidad USUARIO. Encapsula las características esenciales (nombre, rol, etc.) y los comportamientos (iniciar_sesion, agregar_dispositivo) de un usuario en el sistema.

*   Clase `Dispositivo`: Modela la entidad DISPOSITIVO. Abstrae las propiedades (id, nombre, tipo, estado) y acciones (cambiar_estado) comunes a todos los dispositivos inteligentes, independientemente de su tipo específico.


2. ENCAPSULAMIENTO: OCULTANDO COMPLEJIDAD Y PROTEGIENDO DATOS
---------------------------------------------------------------
El encapsulamiento agrupa los datos (atributos) con los métodos que operan sobre ellos, ocultando los detalles de implementación para proteger la integridad de los datos.

Aplicación en el Diseño:
*   En lugar de tener diccionarios globales (USUARIOS) que son manipulados directamente desde diferentes módulos, la clase `Usuario` encapsula la información de un usuario. El acceso y la modificación de los datos se realizan a través de su _interfaz pública_ (sus métodos).

*   Esto protege la integridad de los datos y facilita cambios futuros en la estructura de almacenamiento, ya que la lógica de negocio interactúa con los métodos de la clase, no directamente con la estructura de datos interna.


3. HERENCIA: CREANDO JERARQUÍAS Y REUTILIZANDO CÓDIGO
------------------------------------------------------
La herencia permite que una clase (subclase) adquiera los atributos y métodos de otra (superclase). El programa diferencia claramente entre usuarios `estandar` y `admin`, donde un administrador _es un tipo de_ usuario con capacidades adicionales.

Aplicación en el Diseño:
*   La clase `Admin` hereda de la clase `Usuario`. Esto significa que un objeto `Admin` tiene todo lo que tiene un `Usuario` (nombre, contraseña, dispositivos) y además añade funcionalidades exclusivas (modificar_rol_usuario, mostrar_usuarios).

*   Esta relación _es-un_ evita la duplicación de código y establece una jerarquía lógica y clara en el modelo.


4. COMPOSICIÓN: MODELANDO RELACIONES "TIENE-UN"
-------------------------------------------------
La composición es un tipo de relación donde un objeto complejo está compuesto por otros. El análisis del sistema muestra una clara relación de "uno a muchos" entre un usuario y sus dispositivos.

Aplicación en el Diseño:
*   La clase `Usuario` tiene un atributo `dispositivos`, que es una lista de objetos `Dispositivo`. Esto modela una relación de composición donde el usuario _tiene-un_ conjunto de dispositivos.

*   Se considera una composición fuerte porque el ciclo de vida de los `Dispositivos` depende del `Usuario`. Si un usuario es eliminado, sus dispositivos asociados también dejan de existir.


5. JUSTIFICACIÓN GENERAL: EVOLUCIÓN DEL PARADIGMA ESTRUCTURADO
---------------------------------------------------------------
El diseño de clases propuesto es una evolución del código existente, que sigue un paradigma estructurado. 

    *   **Alta Cohesión:** Cada clase tiene una única responsabilidad bien definida (la clase `Usuario` solo gestiona usuarios, `Dispositivo` solo gestiona dispositivos, etc.).
    
    *   **Bajo Acoplamiento:** Las interacciones entre clases se realizan a través de interfaces claras (métodos), reduciendo la dependencia directa de una estructura de datos global y compartida.


CONCLUSIÓN
----------
El diagrama de clases propuesto no es solo una representación visual, sino un diseño fundamentado que aplica principios clave de POO para transformar un programa funcional en una arquitectura de software más robusta, escalable y mantenible. Se basa en la abstracción, el encapsulamiento, la herencia y la composición para crear un sistema más coherente y fácil de evolucionar.