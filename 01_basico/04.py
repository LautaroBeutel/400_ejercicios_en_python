# 400 Ejercicios en python
#
# Ejercicio 04:
#   Hacer un programa que solicite un color por teclado e imprima
#   los siguientes mensajes dada ciertas situaciones
#       Verde ->        'Puede pasar'
#       Amarillo ->     'Precaucion'
#       Rojo ->         'No pasar'
#       Cualquiera ->   'Color invalido'

def imprimir_msg(color):
    if color.lower() == 'verde':
        print('Puede pasar')
    elif color.lower() == 'amarillo':
        print('Precaucion')
    elif color.lower() == 'rojo':
        print('No pasar')
    else:
        print('Color invalido')

print('ingrese un color:')
imprimir_msg(input())