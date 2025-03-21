## Encapsulación

"""Una coordenada en dos dimenciones esta compuesta por 2 valores, el valor en el eje de las x y el valor en el eje de las y,esto podria ser una clase. Un cuadrado esta compuesto por cuatro coordenadas que son los cuatro vertices, esto podria ser una clase que esta compuesta por cuatro clases"""

# clase Coordenada

class Coordenada:

    # metodo constructor   
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    # metodos de lectura y escritura de cada atributo
    def getX(self):
        return self.__X 
    
    def getY(self):
        return self.__Y
    
    def getX(self, x):
        self.__X = x

    def getY(self, y):
        self.__Y = y 
    
    # metodo para mostrar la coordenada
    def mostrarCoordenada(self):
        print("(", self.__X, ",", self.__Y, ")")

# clase Cuadrado

class Cuadrado:

    # metodo constructor
    def __init__(self,v1, v2, v3, v4):
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4

    # metodo privados para mostrar los vertices
    def mostrarCoordenadasV1(self):
        print("(", self.__V1.getX(), ",", self.__V1,getY(), ")")

    def mostrarCoordenadasV1(self):
        print("(", self.__V2.getX(), ",", self.__V2,getY(), ")")

    def mostrarCoordenadasV1(self):
        print("(", self.__V3.getX(), ",", self.__V3,getY(), ")")

    def mostrarCoordenadasV1(self):
        print("(", self.__V4.getX(), ",", self.__V4,getY(), ")")

    # metodo para mostrar los vertices
    def mostrarVertices(self):
        print("El cuadrado esta compuesto por los siguientes vertices: ")
        self.__mostrarCoordenadaV1()
        self.__mostrarCoordenadaV2()
        self.__mostrarCoordenadaV3()
        self.__mostrarCoordenadaV4()


# metodo principal del modulo
def main():
    # input
    x1 = int(input("Digite el valor de x: "))
    x2 = int(input("Digite el valor de y: "))

    # processing
    c1 = Coordenada(x1,x2)
    c1.mostrarCordenada()

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)
    
    cuadrado1 = Cuadrado(v1, v2, v3, v4)
    cuadrado1.mostrarVertices()

    # Que ocurre sii el metodo getX() lo hacemos privado: __getX()?
    coordenada = Coordenada(3,4)
    print("(", coordenada:__getX(), ",", coordenada.getY(), ")")


if __name__ == "__main__":
    main()