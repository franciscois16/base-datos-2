from typing import Optional
def buscar_elemento(lista: list[int], elemento: int)  -> Optional[int]:
    if elemento in lista:
        return lista.index(elemento)
    return None

n = buscar_elemento(["2","3"],4)
print(n)