# 400 Ejercicios en python
#
# Ejercicio 09:
#   Hacer un programa que muestre el dibujo:
#
#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *

for i in range(0, 6):
    for j in range(0, 11):
        print('*', end='')
    print()