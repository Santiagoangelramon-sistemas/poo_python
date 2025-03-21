# poo_python

El paradigma de POU esta basado en una abstraccion del mundo real que nos va a permitir desarollar programas de forma cercana a como vemos el mundo, pensando  en objetos que tenemos delante y en acciones que podemos hacer ellos.

## Clase

-Una clase de mierda es un tipo de dato cuyas variables se llaman objetos o instancias
-la clase es la definicion de concepto real y los sujetos o instancias son el propio objeto del mundo real 
-estan compuestas por: Atributos y Metodos.

### Atributos
-Informacion que almacena la clase 

### Metodos
-Operaciones que se pueden realizar en clase

## Definicion de una clase en python

```python
class NombreClase:
    def__init__(self, variable1, variable2):
self.Atributo1 = valor1
self.Atributo2 = valor2

    def nombreMetodo(self):
    bloquecodigo
```

### Componentes

``````class``````: Palabra reservada en python para definir una clase.

```NombreClase```: nombre de la clase que quieres crear.

```def```: palabra reservada en python que se utiliza para definir tanto el constructor de la clase (metodo que se ejecuta la primera vez que usas una clase) como los diferentes metodods ue tiene.

```__init__```: palabra reservada en python para definir el metodo constructor de la clase. es lo primero que se ejecuta cuando crear un objeto de una clase.

```(self, variableX)```: parametro del constructor de la clase. El parametro self es obligatorio despues puedes tener tantos parametros como quieras.  La forma de añadir parametros en las mismas funciones.

```self.AtributosX```: forma de utilizacion y acceso a los atributos de la clase.

```nombreMetodo```: instrucciones que ejecutara el metodo.

```(self)```: parametros del metodo. El parametro self es obligatorio y despues puedes tener tantos parametros como quieras.

```bloqueCodigo```: instrucciones que ejecutara el metodo.

- Cuando defines una clase debes tener en cuenta los siguientes puntos:
    - Puedes definir tantos atributos como necesites.
    - Puedes definir tantos metodos como necesites.
    - Puedes definir tantos parametros en el constructor y en los metodos como necesites

## Comṕosicion
- Consiste en la creacion de nueva clases apartir de clases ya existentes que actuan compociciones nuevos de la nueva
-las clases exixtentes seran atributos de la nueva clase
-en (POO) la composicion significaque entre las 2 clases existe una relacion tipo "ya tienes.."
- Ejemplo:
    -una cordenada en 2 dimenciones esta compuesta por 2 valores, el valor en el eje de las y, esto podria ser una clase. Un cuadrado esta compuesto por 4 cordenadas que son los 4 vertices, esto podria ser una clase que esta compuesta por 4 clases del objeto ordenada.
    
## Herencia
- Permite la reutilización de código.
- Consiste en la definición de una clase utilizando como base una clase ya existente.
- La nueva clase derivada tendrá todas las caracteristicas de la clase base y ampliará el concepto de esta, es decir, tendrá todos los atributos y métodos de la clase base.
- Significa que entre dos clases existe una relación del tipo "es un".
- La herencia en Python se especifica de la siguiente manera: ```class NombreClase(ClaseBase):```
- Ejemplo:
    - Pensemos en una persona como una clase, la persona tendría una serie de atributos como pueden ser el nombre, los apellidos, la edad, etc.  Esas características de una persona serían compartidas por todas aquellas clases hijas como pueden ser alumno y profesor.  Es decir, alumno y profesor heredarían las propiedades de la clase persona y tendrían sus propias propiedades, diferentes entre ellas, como por ejemplo el curso en el que está el alumno y el horario de tutorias del profesor.

    - Clase base: Persona
        - Atributos:
            - Nombre
            - Apellidos
            - Edad

    - Clase derivada: Alumno
        - Atributos:
            - Curso
            - Asignaturas
    
    - Clase derivada: Profesor
        - Atributos:
            - Antigüedad
            - Tutorias
            - Teléfono

## Actividad:
- Consulte un ejemplo práctico del uso de herencia múltiple en Python

### Bibliografía
Moreno, A. y Córcoles, S.  (2020).  Python práctica.  Herramientas, conceptos y técnicas.  Ediciones de la U.