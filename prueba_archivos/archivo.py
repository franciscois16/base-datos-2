with open("mi_archivo.txt","w") as f: #con with no es necesario usar close solo con open si
    f.write("hola mundo!\n")
    f.writelines([f"hola mundo {n+1}\n" for n in range (10)])
#f.close()