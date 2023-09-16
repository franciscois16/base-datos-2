# %%
mi_lista = [1,2,3,4,5]

# %%

mi_lista.append(13)
# %%
mi_lista.remove(4)

# %%

mi_lista.insert(0,0)

# %%
mi_lista.extend([20,30])
# %%

mi_nueva_lista = mi_lista + [100,2000]

# %%
mi_nueva_lista[1]

# %%
mi_tupla = (1,2,3,4,5)
# %%
mi_tupla = mi_tupla + (6,5)

# %%
6 in mi_lista

# %%
set1 = {1,5,7,10}  #esto son conjuntos
set2 = {2,5,9,13}

# %%
set1.add(13)

# %%
set1 - set2


# %%
mi_diccionario = {"nombre":"juan","edad": 30, "ciudad" : "punta arenas"}


# %%
mi_diccionario["edad"]
# %%
mi_diccionario2 = {1:1111, ("A",0): "zzz"}

# %%
mi_diccionario2[("A",0)]

# %%
mi_diccionario.get("mascotas",0)
# %%
if "mascotas" in mi_diccionario:
    print(mi_diccionario["mascotas"])
# %%
if valor := mi_diccionario.get("mascotas") is not None:
    print(valor)
# %%
mi_diccionario.keys()

# %%
mi_diccionario.items()
# %%
del mi_diccionario["ciudad"]

# %%
mascotas = ["boby", "michi", "zoe","blacky"]
for i , mascotas in enumerate(mascotas):
    print(i)
# %%
for i, (k, v) in enumerate(mi_diccionario.items()):
    print(i,k,v)


# %%
mis_numeros = [1,5,6,7,13,16]

mis_cuadrados = []
for numero in mis_numeros:
    mis_cuadrados.append(numero**2)

# %%
mis_cuadrados = {numero : numero**2 for numero in mis_numeros if numero%2 == 1}
# %%
mis_cuadrados
# %%

def suma_numeros(num1,num2=10,num3=0):
    return num1 + num2 + num3
# %%

suma_numeros(num3=15,num1=9)

# %%
def operaciones(num1,num2):
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    print(num1/num2)

# %%
operaciones(2,3)
# %%
def removechar(nombre,num,num2):
    if num2 == 0:
        return nombre[num:]
    else:
        return nombre[:-num]
    
# %%
removechar("antonios",4,0) 


# %%