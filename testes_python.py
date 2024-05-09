
def mediaNotas():
    nota1 = float(input("Digite 0 1º número entre 0 e 10: "))

    if nota1 <= 10:
        nota2 = float(input("Digite o 2º número entre 0 e 10: "))
        
        if nota2 <= 10:
            nota3 = float(input("Digite o 3º número entre 0 e 10: "))
            
            if nota3 <= 10:
                media = (nota1 + nota2 + nota3) / 3
                media = round(media)
                
                if media > 6:      
                    print(f"Sua média foi de {media}")
                    print(f"Considerando a média geral como 6, você está APROVADO. Parabéns")
                else:
                    print(f"Sua média foi de {media}")
                    print(f"Considerando a média geral como 6, você está REPROVADO.")
        
            else:
                print("Valor incorreto! Digite uma nota entre 0 e 10!")
                mediaNotas()
        else:
            print("Valor incorreto! Digite uma nota entre 0 e 10!")
            mediaNotas()
    else:
        print("Valor incorreto! Digite uma nota entre 0 e 10!")
        mediaNotas()

mediaNotas()
