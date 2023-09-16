from dataclasses import dataclass, field
from statistics import mean

@dataclass
class cliente:
    nombre:str
    email:str
    carrito: list["producto"] = []
    def __init__(self,nombre:str,email:str,carrito:list["producto"],lista_clientes: list["cliente"]=[])-> None:
        for cliente in lista_clientes:
            if cliente.email == email:
                raise Exception("este cliente ya existe")
        self.nombre=nombre
        self.email = email
        self.carrito = carrito

    def aggregar_al_carrito(self,producto:"producto"):
        self.carrito.append(producto)
        

@dataclass
class producto:
    nombre: str
    precio: int
    descriocion: str
    calificaciones : list[int] = field(default_factory=list)
    def agregar_calificaciones(self,calificacion:int)->None:
        self.calificaciones.append(calificacion)
    def media_calificaciones(self)->float:
        return mean(self.calificaciones)

@dataclass
class pedido:
    cliente: " cliente"
    producto: list["producto"]
    def calcular_total(self, descuento: "descuento" | None) -> int:
        # igual puede ser solo
        # suma = 0
        # for producto in self.producto:
        #     suma+= producto.precio
        # return suma
        total = sum(x.precio for x in self.productos)
        if descuento is not None:
            total -= total * (descuento.porcentaje/100)
        

@dataclass

class descuento:
    codigo:str
    porcentaje:int
    