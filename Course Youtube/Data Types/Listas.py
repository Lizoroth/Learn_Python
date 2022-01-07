primeraLista=["cero",9,3.14,False,5,8,"seis"]
#print(primeraLista[-3])# elemento contado desde el final de la lista
#print(primeraLista[2]) # elemento contado desde la primera posición
print(primeraLista[4:]) #porción de una lista 
primeraLista.append("siete")
print(primeraLista[:])
primeraLista.insert(2,"ocho")#inserta elemento a una lista definiendo la posicion especifica en la que se desea agregarlo
print(primeraLista[:])
primeraLista.extend(["nueve","diez","once","doce","trece","catorce"])
print(primeraLista[:])
print()
print(primeraLista.index(False))#devuelve el indice del elemento consultado por parametro

print("uno" in primeraLista)#compruebo si existe el elemento en la lista definida
primeraLista.remove(8)
print(primeraLista[:])

primeraLista.pop() # elimina el ultimo elemento de la lista
print(primeraLista[:])

segundaLista=["aaaa","eeeeeeeee"]

terceraLista = primeraLista+segundaLista
print(terceraLista[:])