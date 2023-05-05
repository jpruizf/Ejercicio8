#Defino clase conjunto

class Conjunto:
    __elementos: list
    def __init__(self,elementos: list):
        self.__elementos = elementos
    def cargar(self):
        self.__elementos = []
        for elemento  in self.__elementos:
            if elemento not in self.__elementos:
                self.__elementos.append(elemento)
    
    def __ad__(self,otro):
        elementos = self.__elementos.copy()
        for elemento in otro.__elementos:
            elementos.append(elemento)
        return Conjunto(elementos)
    def __sub__(self,otro):
        elementos = []
        for elemento in self.__elementos:
            if elemento not in otro.__elementos:
                elementos.append(elemento)
        return Conjunto(elementos)
    
    def __eq__(self,otro):
        if len(self.__elementos) != len(otro.__elementos):
            Val =  False
        else:
            Val = True
        return Val
    
    def __str__(self):
        return "{" + " , " .join(str(elemento) for elemento in self.__elementos) + "}"