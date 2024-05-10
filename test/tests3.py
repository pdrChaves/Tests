'''
Operadores de comparação: (relacionais)
>       maior
>=      maior/igual
<       menor
<=      menor/igual
==      igual
!=      diferente
'''

num_1=int(input(print('Digite um número:')))
num_2=int(input(print('Digite outro número:')))

maior= num_1 > num_2
menor= num_1 < num_2
menor_igual= num_1 <= num_2
maior_igual= num_1 >= num_2
igual= num_1 == num_2
diferente= num_1 != num_2

print(f'número 1 é maior?: {maior}')
print(f'número 1 é menor?: {menor}')
print(f'número 1 e 2 são iguais?: {igual}')
print(f'são diferentes?: {diferente}')
print(f'número 1 é menor ou igual ao número 2?: {menor_igual}')
print(f'número 1 é maior ou igual ao número 2?: {maior_igual}')

if num_1 > num_2:
    print(f'maior: {maior}')
elif num_1 >= num_2:
    print(f'maior ou igual: {maior_igual}')
elif num_1 < num_2:
    print(f'menor: {menor}')
elif num_1 <= num_2:
    print(f'menor ou igual:{menor_igual}')
elif num_1 == num_2:
    print(f'igual: {igual}')
elif num_1 != num_2:
    print(f'diferentes: {diferente}')
