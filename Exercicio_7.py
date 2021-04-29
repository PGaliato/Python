felicidade = 1
nome = input('Digite seu nome:')
if(felicidade > 0):
    felicidade = int(input('Grau de Felicidade:'))

    if(felicidade <= 10):
        print ('Voce é muito Feliz',nome)
        print ('alegria contagiante')
        
    elif(felicidade >= 11) and (felicidade <= 19):
        print('Voce é muito Indeciso',nome)
        print('Faca algo que te deixe animado')
         
    elif(felicidade >= 20):
        print ('Voce esta infeliz hoje',nome)
        print ('Procure a ajuda de alguem')



             
