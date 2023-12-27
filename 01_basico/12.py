# 400 Ejercicios en python
#
# Ejercicio 10:
#   Hacer un programa que muestre el sgte
#   dibujo
#
#   * * * * *
#   * * * *
#   * * *
#   * *
#   *

n_cols = 6
n_rows = 6

for i in range(0, n_cols):
    for j in range(0, n_cols - i):
        print('* ', end='')
    print()