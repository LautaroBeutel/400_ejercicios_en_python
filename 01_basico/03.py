# 400 Ejercicios en python
#
# Ejercicio 03:
#   Hacer un programa que solicite la edad
#   y determine si es mayor de edad

def mayor_edad(edad):
    if edad >= 18: 
        return True
    else:
        return False
    
print('Ingrese su edad: ')

if mayor_edad(int(input())):
    print('Es mayor de edad')
else:
    print('Es menor de edad')