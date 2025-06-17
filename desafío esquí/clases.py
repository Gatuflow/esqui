class simulador:
    def __init__(self, velocidad, posicion, curva):
        self.__velocidad=velocidad
        self.__posicion=posicion
        self.__curva=curva
    def get_velocidad(self):
        return self.__velocidad
    def set_velocidad(self,num):
        self.__velocidad = num
    def get_posicion(self):
        return self.__posicion
    def set_posicion(self,num):
        self.__posicion = num
    def get_curva(self):
        return self.__curva
    def set_curva(self, num):
        self.__curva = num
    def __str__(self):
        return f"Vas a {self.get_velocidad()} km/h, en el puesto {self.get_posicion()}, la siguiente curva tiene una dificultad de nivel {self.get_curva()}"