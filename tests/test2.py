print('Olá,seja bem vindo ao teste de IMC! ')

nome=input('Qual é o seu nome? ')
idade=input('Quantos anos você tem {}? '.format((nome))) 
altura=float(input('Qual a sua alutra em metros? '))
peso=int(input('Quaç o seu peso em kg? '))
IMC=peso / (altura * altura)    #IMC = peso / altura x altura

print(nome,',o seu teste de IMC deu: {} '.format((IMC)))

'''
outra solução:
'''

print('teste 2:')
nome=input('Qual é o seu nome? ')
idade=input('Quantos anos você tem {}? '.format((nome))) 
altura=float(input('Qual a sua alutra em metros? '))
peso=float(input('Quaç o seu peso em kg? '))
IMC=peso / (altura * 2) 

linha1= f'{nome}, de {idade} anos de idade , com altura de {altura} metros, pesando {peso} kg, possui seu IMC calculado em aproximadamente: {IMC:.2f}'
print(linha1)
