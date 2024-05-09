# DESAFIO 2

# Crie um programa que solicita ao usuário que insira um número inteiro e, em seguida, verifica se o número é par ou ímpar.
# O programa deve exibir uma mensagem indicando se o número é par ou ímpar.

def parImpar():
    number = int(input("Informe um número: "))

    result = number % 2

    if result == 0:
        print(f"O número {number} é um número PAR!")
    else:
        print(f"O número {number} é um número ÍMPAR")
        
parImpar()