=========================================================
  JUSTIFICACION DEL DISEÑO ORIENTADO A OBJETOS (POO)
         PARA EL SISTEMA POO-SMARTHOME
=========================================================

El siguiente documento justifica el diseño de clases propuesto para el proyecto POO-SmartHome. El objetivo es transformar la estructura actual, basada en modulos funcionales, en un modelo robusto de clases y objetos, aplicando los principios fundamentales de la Programacion Orientada a Objetos para mejorar la organizacion, mantenibilidad y escalabilidad del sistema.

---

1. ABSTRACCION: DE ENTIDADES A CLASES

La abstraccion consiste en identificar las caracteristicas y comportamientos esenciales de un objeto del mundo real y modelarlos en una clase, ignorando los detalles irrelevantes. En nuestro sistema SmartHome, hemos identificado dos entidades fundamentales: el Usuario y el Dispositivo.

*   Analisis del codigo actual: El sistema actual maneja estas entidades a traves de diccionarios globales (USUARIOS en data.py). Por ejemplo, un usuario es un diccionario con claves como 'contrasena' y 'rol', y un dispositivo es otro diccionario dentro de una lista. Aunque funcional, esta representacion mezcla los datos con la logica que los manipula, la cual esta dispersa en modulos como usuario.py y dispositivos.py.

*   Propuesta de diseño con clases:
    *   Clase Usuario: Proponemos crear una clase Usuario que abstraiga toda la informacion y las acciones de un usuario. Sus atributos serian nombre, contrasena y rol. Sus metodos (comportamientos) serian iniciar_sesion(), consultar_datos_personales() y modificar_rol(). De esta forma, un objeto Usuario no solo contiene sus datos, sino que tambien es responsable de gestionar sus propias acciones.
    *   Clase Dispositivo: De igual manera, la clase Dispositivo representara cualquier aparato conectado. Sus atributos esenciales son id, nombre, tipo y estado. Sus metodos serian cambiar_estado() y ver_estado().

Al usar clases, pasamos de manejar estructuras de datos pasivas a interactuar con objetos activos que representan fielmente las entidades del sistema.

---

2. ENCAPSULAMIENTO: OCULTANDO COMPLEJIDAD Y PROTEGIENDO DATOS

El encapsulamiento es el principio de agrupar los datos (atributos) y los metodos que operan sobre esos datos dentro de una misma unidad (la clase), y controlar el acceso a ellos.

*   Analisis del codigo actual: El principal problema de la estructura actual es la falta de encapsulamiento. El diccionario global USUARIOS es accesible y modificable directamente desde cualquier modulo (main.py, dispositivos.py, automatizaciones.py). Esto es peligroso, ya que un cambio incorrecto en un modulo podria corromper los datos de todo el sistema sin ningun control. Por ejemplo, nada impide que una funcion asigne un estado invalido a un dispositivo.

*   Propuesta de diseño con clases:
    *   Nuestra clase Dispositivo encapsulara el atributo estado. Para modificarlo, en lugar de acceder directamente, se debera llamar al metodo publico cambiar_estado(nuevo_estado). Este metodo contendra la logica de validacion (como la del modulo soporte.py) para asegurar que nuevo_estado solo pueda ser "encendido" o "apagado".
    *   De la misma forma, los datos del Usuario (como su contraseña o rol) se protegerian, y solo podrian ser modificados a traves de metodos controlados como modificar_rol(), que podria incluir logica para verificar permisos.

El encapsulamiento nos permite crear una "caja negra": el resto del programa no necesita saber como un dispositivo cambia su estado internamente, solo necesita llamar al metodo correcto. Esto protege la integridad de los datos y reduce la complejidad.

---

3. HERENCIA: CREANDO JERARQUIAS Y REUTILIZANDO CODIGO

La herencia permite que una clase (subclase) adquiera los atributos y metodos de otra (superclase), permitiendo la reutilizacion de codigo y la creacion de jerarquias logicas.

*   Analisis del codigo actual: El sistema maneja diferentes tipos de dispositivos (luz, camara, electrodomestico) usando condicionales if/elif basados en el valor de la clave 'tipo'. Si quisieramos añadir un nuevo tipo de dispositivo, como un "Termostato", tendriamos que modificar multiples archivos (automatizaciones.py, dispositivos.py) para añadir mas elif, lo cual es propenso a errores y poco escalable.

*   Propuesta de diseño con clases:
    *   Proponemos una clase base Dispositivo con las propiedades y metodos comunes a todos los aparatos.
    *   Luego, creariamos clases hijas que hereden de Dispositivo: Luz, Camara, Electrodomestico.
    *   Esta estructura nos permite:
        1. Reutilizar codigo: Todas las clases hijas compartirian el codigo comun de la clase Dispositivo.
        2. Especializar: Cada clase hija podria tener atributos o metodos propios. Por ejemplo, la clase Luz podria tener un atributo adicional intensidad_brillo, y la clase Camara un metodo grabar().
        3. Escalabilidad: Añadir un "Termostato" seria tan simple como crear una nueva clase Termostato que herede de Dispositivo, sin tocar el codigo existente.

---

4. COMPOSICION: MODELANDO RELACIONES "TIENE-UN"

La composicion es una forma de relacion entre clases donde un objeto complejo esta compuesto por otros. Modela una relacion "tiene-un". El analisis del sistema muestra una clara relacion de "uno a muchos" entre un usuario y sus dispositivos.

*   Analisis del codigo actual: Esta relacion ya existe de forma implicita. Cada entrada en el diccionario USUARIOS tiene una clave 'dispositivos' que es una lista de diccionarios de dispositivos.

*   Propuesta de diseño con clases:
    *   En nuestro diseño, la clase Usuario tendra un atributo que sera una lista de objetos de la clase Dispositivo (o sus subclases). Esto formaliza la relacion: un objeto Usuario esta compuesto, entre otras cosas, por una coleccion de objetos Dispositivo.
    *   Se considera una composicion fuerte porque el ciclo de vida de los Dispositivos depende del Usuario. Si un usuario es eliminado, sus dispositivos asociados tambien dejan de existir, tal como se describe en la logica del sistema.

Este modelo representa la relacion de una manera mucho mas limpia y directa que los diccionarios anidados.

---

5. JUSTIFICACION GENERAL: EVOLUCION DEL PARADIGMA ESTRUCTURADO

El diseño de clases propuesto es una evolucion natural del codigo existente, que sigue un paradigma estructurado. Los beneficios clave de esta transicion son:

*   Alta Cohesion: Cada clase propuesta tiene una unica responsabilidad bien definida (la clase Usuario solo gestiona usuarios, Dispositivo solo gestiona dispositivos, etc.). En el codigo actual, la cohesion es baja, ya que la logica para gestionar dispositivos esta separada de los datos de los dispositivos.
*   Bajo Acoplamiento: Las interacciones entre clases se realizan a traves de interfaces claras (metodos), reduciendo la dependencia directa de una estructura de datos global y compartida. El codigo actual tiene un alto acoplamiento con el diccionario USUARIOS de data.py; cualquier cambio en esa estructura obliga a modificar multiples archivos. Con nuestro diseño, los cambios internos en una clase no afectan a las demas, siempre que su interfaz publica se mantenga.

---

CONCLUSION

El diagrama de clases propuesto no es solo una representacion visual, sino un diseño fundamental que aplica principios clave de POO para transformar un programa funcional en una arquitectura de software mas robusta, escalable y mantenible. Se basa en la abstraccion, el encapsulamiento, la herencia y la composicion para crear un sistema mas coherente y facil de evolucionar.