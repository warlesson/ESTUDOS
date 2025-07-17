# Função para tirar as virgulas e dar Enter em cada part number
with open("test2.avl", "r") as arquivo:
     file = arquivo.read().replace(",", "\n") # Tirar a , e dar enter

     with open("test2.avl", "w") as arquivo: # criar tudo sem o \n
        arquivo.write(file)

### Função para deixar em um vetor, apagar os \n e apagar as que estão duplicadas.
#def apagar():
with open("test2.avl", "r+") as arquivo:
        file = arquivo.readlines() # listando todos os part number em um vetor
        print(file)
        file = [line.rstrip('\n') for line in file]  # retirando o \n
        meuSet = list(set(file)) # Transformando para lista []
        print(meuSet)
        
        with open ("test2.avl", 'w' ) as arquivo: # adicionando os part no AVL
            for valor in meuSet:
                arquivo.write(valor + '\n')




#apagar()