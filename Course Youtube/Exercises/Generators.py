
# A Python program to demonstrate use of 
# generator object with next() 

# A generator function

def simpleGeneratorFun(limite):
    num=1
    while num<=limite:
       yield num*2
       num+=1
   
# x is a generator object
x = simpleGeneratorFun(8)
  
# Iterating over the generator object using next
print("imprime todos los elementos almacenados en el iterador la lista completa")


print(x.__next__())
print ("aaaa")
print(x.__next__())


print("ciclo")
for i in x:
    print(i)