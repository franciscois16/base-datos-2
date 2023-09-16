from clases import cliente,producto,pedido

clientes=[

cliente(nombre="catalina",email="catalina@example.com",lista_clientes =[]),
cliente(nombre="miguel",email="miguel@example.com",lista_cliente =[]),
]

productos =[
    producto(nombre="lapiz",precio=1900,descriocion="lapiz verde"),
    producto(nombre="regla",precio=2990,descriocion="regla 30 cm"),
    producto(nombre="mouse",precio=29900,descriocion="mouse RGB"),

]

cl1 = cliente(nombre="miguel",email="miguel12@example.com",lista_clientes = clientes)

def buscar_productos(lista_productos:list["producto"],busqueda:str)-> producto | None:
    print("hola")