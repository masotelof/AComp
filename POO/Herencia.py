# esto importa toda la libreria
# import math

# esto importa solo una parte de la libreria
from math import pi

class Figura_2D:
    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro
        # tenemos un atributo "privado"
        self.__privado = 10
    def cal_area(self):
        pass
    def cal_perimetro(self):
        pass

class Figura_3D:
    def __init__(self):
        self.volumen = 0
    def cal_volumen(self):
        pass

class Cuadrado(Figura_2D, Figura_3D):
    def __init__(self, lado): 
        # Manda llamar a los constructores de las clases Padres para inicializar los atributos correspondientes
        Figura_2D.__init__(self, 0, 0)
        Figura_3D.__init__(self)

        self.lado = lado

    def cal_area(self):
        self.area = self.lado**2
    def cal_perimetro(self):
        self.perimetro = 4*self.lado
    def cal_volumen(self):
        self.volumen = self.lado**3

    def __str__(self):
        return f'Cuadrado\n Area:{self.area}\n Perimetro:{self.perimetro}\n Volumen:{self.volumen}'
    

class Circulo(Figura_2D):
    def __init__(self, radio):
        Figura_2D.__init__(self, 0, 0)
        self.radio = radio

    def cal_area(self):
        self.area = pi * self.radio ** 2
    def cal_perimetro(self):
        self.perimetro = pi * 2 * self.radio

    def __str__(self):
        return f'Circulo\n Area:{self.area}\n Perimetro:{self.perimetro}'

if __name__ == "__main__":
    '''
    fig = Figura()
    # para acceder al atributo privado usamos _NombreClase y despues el nombre del atributo
    print(fig._Figura__privado)
    print(f'Area {fig.area} Perimetro {fig.perimetro}')
    '''

    circulo = Circulo(6)
    circulo.cal_area()
    circulo.cal_perimetro()

    cuadrado = Cuadrado(8)
    cuadrado.cal_area()
    cuadrado.cal_perimetro()
    #cuadrado.cal_volumen()

    print(circulo)
    print(cuadrado)
    print("-"*30)
    lista = []
    lista.append(Circulo(6))
    lista.append(Cuadrado(8))
    lista.append(Cuadrado(10))
    lista.append(10)

    for fig in lista:
        if isinstance(fig, Figura_2D):
            if isinstance(fig, Figura_3D):
                fig.cal_volumen()

            fig.cal_area()
            fig.cal_perimetro()
            print(fig)
        else:
            print("No es una Figura")
         
