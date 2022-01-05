import os
from typing import Match

aux = 1

def sumaNumeros(x,z):
  return x+z

def restaNumeros(x,z):
  return x-z

def divideNumeros(x,z):
  return x/z

def multiplicaNumeros(x,z):
  return x*z

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def inNumeros(aux):
  if (aux != 0):
    x = int(input("Ingrese primer núnmero"))
    z = int(input("Ingrese segundo número"))
    match int(aux):
      case 1: print(sumaNumeros(x,z))
      case 2: print(restaNumeros(x,z)) 
      case 3: print(divideNumeros(x,z))
      case 4: print(multiplicaNumeros(x,z))    

while aux != 0:
  
  clearConsole()
  print("Bienvenido al menú de operaciones")
  print("seleccione una opción")
  print("1 - Suma")
  print("2 - Resta")
  print("3 - División")
  print("4 - Multiplicación")
  print("0 - Salir")
  aux = int(input("Ingrese Opción"))
  inNumeros(aux)





