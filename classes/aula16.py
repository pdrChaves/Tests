# if /    elif   / else
# se / se nao se / se nao
print('Olá, seja bem vindo ao programa, farei algumas perguntas sobre você antes de começarmos')
nome=input(print('Qual o seu nome? '))
print(f'Seja bem vindo {nome}, ')
print('Este programa é unicamente para pessoas maiores de idade ')
idade=int(input(print(f'Quantos anos você tem {nome}? ')))

if idade >= 18:
    input(print('Você é maior de idade, gostaria de entrar no programa? '))

elif idade <= 18:
    print('Você é menor de idade e não possui permissão para acessar o programa.')
else:
    print('Você não respondeu a pergunta corretamentem, tente novamente...')
    
entrada=input(print('Você quer entrar ou sair do sistema? '))

if entrada == 'entrar':
    print(f'Seja bem vindo {nome}!')

elif entrada == 'sair':
    print(f'Ok, até breve {nome}!')
else:
    print('Perdão, mas aparentemente você não deu uma resposta específica')