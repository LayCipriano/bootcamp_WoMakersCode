# DESAFIO 4

# Crie um programa que solicita ao usuário que insira um número inteiro positivo e, em seguida, calcula e exibe o fatorial desse número.
# (O fatorial de um número é o produto de todos os números inteiros positivos de 1 até o próprio número.)

def fatorial():
    n = int(input("Informe um número: "))
    result = n

    print("Fatorial de", n)

    while n > 1:
        n -= 1
        result *= n
        
        print(result)
        
fatorial()