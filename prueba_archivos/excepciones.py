num_texto = "7"
#num_texto = "siete"
num2 = 0
try:
    mi_numero = int(num_texto)
    mi_numero= mi_numero/num2
except (ValueError,ZeroDivisionError) as e:
    print(f"algo paso. {repr(e)}")
else:
    print("else")
    raise Exception("me gustan los errores")
finally:
    print("termino todo esto")
# except ZeroDivisionError:
#     print ( "eroor num 2 no puede ser 0")
# except ValueError:
#     print ("")
print("final del programa")