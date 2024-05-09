import re

# DESAFIO 3

# Crie um programa que verifica se uma palavra fornecida pelo usuário é um palíndromo ou não.
# (Um palíndromo é uma palavra que é lida da mesma forma tanto da esquerda para a direita quanto da direita para a esquerda.)


def palindromo():
    regex = r'\d+'
    word = str(input("Informe uma palavra: "))    
    word = re.sub(regex, '', word).upper()

    if word == word[::-1]:
        print("O conteúdo informado é um palíndromo!")
        palindromo()
    else:
        print("O conteúdo informado não é um palíndromo!")
        palindromo()
        
palindromo()