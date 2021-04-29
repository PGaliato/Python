tentativas = 5
jogador = input('Jogador: ')

print ('Ola, tente adivinhar o numero correto')
print ('Você tem  5 tentativas')

print ('Gerando um número de 0 á 10...\nGood Luck')

numero = (7)


while(tentativas > 0):
    chute = int(input('Chute: '))
    tentativas -= 1

    if tentativas >= 0:
        if (chute == numero):
            print ('Meus parabéns você adivinhou o numero que eu pensei!')
            break
        elif(chute < numero):
            print ('Você errou,tente um numero mais alto')
            print ('Ainda restam', tentativas)
        elif(chute > numero):
            print ('Você errou, tente um numero mais baixo')
            print ('Ainda resta',  tentativas)
    else:
        print ('Infelizmente, não foi dessa vez, Voce esgotou suas chances, mais sorte na proxima!') 
        print ('O número certo era: ',numero)
