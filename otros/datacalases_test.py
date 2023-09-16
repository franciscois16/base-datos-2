from dataclasses import dataclass
@dataclass

class Animal:
    especie: str
    edad: int
    color: str
    def hacer_sonido(self):
        return f"El animal de especie {self.especie} hace un sonido"
    
@dataclass
class gato:
    edad: int
    color:str
    especie:str = "gato"
    vidas: int = 9



animal1 = Animal(especie="perro",edad=12,color="verde")
gato1 = gato(5,"blanco")
print(animal1)
print(gato1)