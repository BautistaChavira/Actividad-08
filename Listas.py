from Particulas import Particula
import json

class Lista:
    def __init__(self):
        self.__Lista = []

    def insertar_final(self, Particulas:Particula):
        self.__Lista.append(Particulas)

    def insertar_inicio(self, Particulas:Particula):
        self.__Lista.insert(0, Particulas)
    
    def imprimir(self):
        for Particulas in self.__Lista:
            print(Particulas)

    def __str__(self):
        return "".join(str(Particulas) + '\n' for Particulas in self.__Lista)
    
    def guardar_archivo (self, ubicacion):
        try:
            with open(ubicacion, "w") as archivoLista:
                lista = [Particulas.to_dict() for Particulas in self.__Lista]
                json.dump(lista, archivoLista, indent = 11)
            return 1
        except:
            return 0
    
    def abrir_archivo(self, ubicacion):
        try:
            with open(ubicacion, "r") as archivoLista:
                listaTemporal = json.load(archivoLista)
                self.__Lista = [Particula(**Particulas) for Particulas in listaTemporal]
            return 1
        except:
            return 0
    
    def __len__(self):
        return len(self.__Lista)
          
    
    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__Lista):
                 Particula = self.__Lista[self.cont]
                 self.cont += 1
                 return Particula
        else :
                raise StopIteration