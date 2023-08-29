# %%
class Animal:
    def __init__(self, especie, edad, color):
        self.especie = especie
        self.edad = edad
        self.color = color

    def hacer_sonido(self):
        return f"El animal de especie {self.especie} hace un sonido"
    def describir(self):
        return f"Este es un {self.especie} {self.color} de {self.edad} años"
# %%

class Perro(Animal):
    def __init__(self, edad, color):
        super().__init__(especie="perro", edad=edad, color=color)
    def hacer_sonido(self):
        return "El perro ladra"
    
perro_1 = Perro(color="gris", edad=7)
perro_1.hacer_sonido() # El perro ladra
perro_1.describir() # Este es un perro gris de 7 años

# %%

class gato(Animal):
    def __init__(self, edad, color,vidas):
        super().__init__(especie="gato", edad=edad, color=color)
        self.vidas = vidas
    def hacer_sonido(self):
        return "El gato maulla"
    def describir(self):
        return f"Este es un {self.especie} {self.color} de {self.edad} años con {self.vidas} vidas"
    
gato_1 = gato(color="gris", edad=7,vidas=6)
gato_1.hacer_sonido() # El gato maulla
gato_1.describir()# Este es un gato gris de 7 años

# %%