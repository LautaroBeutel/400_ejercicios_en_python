# 400 Ejercicios en python
#
# Ejercicio 07:
#   Hacer un programa que cuente del 1 al 100 inclusive
#   y que sean divisibles por 5

for count in range(1,101):
    if count % 2 == 0 and count % 5 == 0:
        print(count)