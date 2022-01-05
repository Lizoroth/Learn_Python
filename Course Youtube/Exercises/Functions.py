def sumaDosNumeros(a,b):
    c = a+b
    return c

#print (sumaDosNumeros(5,20))


def numerosPrimos(nro):    
    for x in range(nro,0,):# range(start,stop,step)
        if nro%x == 1 :
          print(x)
        else :    print("no")
    

numerosPrimos(2)
