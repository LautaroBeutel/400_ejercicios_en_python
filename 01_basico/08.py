# 400 Ejercicios en python
#
# Ejercicio 08:
#   Hacer un prorama que imprima una tabla de multiplicar del 2 al 9. 
#   Cada uno debe mostrar sus valores multiplicados

for a in range(2, 10):
    print(f'Tabla del {a}:')
    for b in range(2, 10):
        print(f'{a}*{b} = {b*a}')