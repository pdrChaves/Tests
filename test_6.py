primeiro_valor = input('Insira um valor: ')
segundo_valor = input('Insira um segundo valor: ')

if primeiro_valor > segundo_valor:
    print(
        f'O primeiro valor = {primeiro_valor}'
        f' é maior que o segundo valor = {segundo_valor}.'
    )
elif primeiro_valor == segundo_valor:
    print(
        f'O primeiro valor = {primeiro_valor}' 
        f' e segundo valor = {segundo_valor} são iguais.'
    )
elif primeiro_valor < segundo_valor:
    print(
        f'O segundo valor = {segundo_valor}' 
        f' é maior que o primeiro valor = {primeiro_valor}.'
    )

