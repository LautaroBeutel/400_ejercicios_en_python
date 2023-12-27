# 400 Ejercicios en python
#
# Ejercicio 10:
#   Hacer un programa que imprima el siguiente dibujo
#
#   * * * * * * * * * *
#   *                 *
#   *                 *
#   *                 *
#   * * * * * * * * * *

n_cols = 10
n_rows = 6

for i in range(0, n_rows):
    for j in range(0, n_cols):
        if i == 0 or i == n_rows - 1:
            print('*', end='')
        else:
            if j == 0 or j == n_cols -1:
                print('*', end='')
            else:
                print(' ', end='')
    print()