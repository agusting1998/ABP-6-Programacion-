=========================================================
  JUSTIFICACION DEL DISEÑO ORIENTADO A OBJETOS (POO)
         PARA EL SISTEMA POO-SMARTHOME
=========================================================

Justificación del Diagrama y Conceptos Aplicados
A continuación, se justifica cómo el diagrama de clases representa cada uno de los conceptos de la Programación Orientada a Objetos presentes en el proyecto.
Clases y Objetos:
Justificación: El diagrama muestra las clases Usuario, GestorUsuarios, Dispositivo y LuzInteligente como las plantillas o "blueprints" del sistema. Cada uno de estos rectángulos define los atributos y métodos que tendrán los objetos que se creen a partir de ellas en tiempo de ejecución.


Encapsulamiento:
Justificación: El encapsulamiento se representa mediante los modificadores de visibilidad (+ para público, - para privado). En la clase Usuario, el atributo contrasena está marcado como privado (-contrasena: str), lo que significa que no debería ser accesible directamente desde fuera de la clase, protegiendo así el estado interno del objeto. Lo mismo ocurre en GestorUsuarios con el atributo -usuarios.


Abstracción:
Justificación: La clase Dispositivo es una abstracción de un dispositivo inteligente genérico. Define las características y comportamientos comunes a todos los dispositivos (un nombre, un id, un estado y la capacidad de cambiarlo), ocultando los detalles complejos de cómo podría funcionar cada tipo de dispositivo específico.


Herencia:
Justificación: Aunque en la tabla se marcó como pendiente, el diseño sí implementa la herencia. La relación se muestra con la flecha de generalización (<|--) que va de LuzInteligente a Dispositivo. Esto significa que LuzInteligente es un Dispositivo que hereda todos sus atributos y métodos, y además añade los suyos propios (brillo).


Polimorfismo:
Justificación: El polimorfismo es una consecuencia directa de la herencia mostrada en el diagrama. Ambas clases, Dispositivo y LuzInteligente, tienen un método con la misma firma: +cambiar_estado(...). Gracias a la herencia, se puede tratar un objeto LuzInteligente como si fuera un Dispositivo genérico. Al invocar el método cambiar_estado(), el programa ejecutará la versión correcta del método (la de LuzInteligente si el objeto es de ese tipo), permitiendo que objetos de diferentes clases respondan al mismo mensaje de formas distintas.


Justificación Específica de las Relaciones

Asociación (entre Usuario y Dispositivo):
Justificación: Un Usuario gestiona dispositivos, pero estos no son parte del usuario. Un dispositivo es un objeto independiente que puede existir por sí mismo. Por eso se usa una asociación, indicando que un usuario está vinculado a (gestiona >) cero o más dispositivos.


Agregación (entre GestorUsuarios y Usuario):
Justificación: El GestorUsuarios contiene una colección de Usuarios, pero estos no dependen del gestor para existir. Es una relación "todo-partes" (gestiona) donde las partes (Usuario) son independientes del todo.
