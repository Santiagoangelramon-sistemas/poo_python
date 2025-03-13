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