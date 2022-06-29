#DECLARANDO A TABELA
tabela= [ [0,0,0],
         [0,0,0],
         [0,0,0] ]

#CRIANDO A FUNÇÃO DO MENU, QUE VAI SER DADA SEMPRE ANTES DE COMEÇAR UM JOGO
def inicio():
    iniciar_continuar=1
    while iniciar_continuar:
        print("#JOGO DA VELHA#")
        iniciar_continuar = int(input("0. Sair \n1. Jogar \n"))
        if iniciar_continuar:
            jogar()
        else:
            print("Saindo do jogo")

#CRIANDO A FUNÇÃO DE JOGAR
def jogar():
    rodada=0

    while ganhou() == 0:
        print("\nJogador ", rodada%2 + 1)
        mostrar()
        linha  = int(input("\nLinha :"))
        coluna = int(input("Coluna:"))

        if tabela[linha-1][coluna-1] == 0:
            if(rodada%2+1)==1:
                tabela[linha-1][coluna-1]=1
            else:
                tabela[linha-1][coluna-1]=-1
        else:
            print("Esse espaço já foi preenchido!")
            rodada -=1

        if ganhou():
            print("Jogador ",rodada%2 + 1," ganhou o jogo!\n\n\n\n\n")

        rodada +=1
    
#CRIANDO A FUNÇÃO DE VERIFICAR O GANHADOR    
def ganhou():
    for i in range(3):
        soma = tabela[i][0]+tabela[i][1]+tabela[i][2]
        if soma==3 or soma ==-3:
            return 1

    for i in range(3):
        soma = tabela[0][i]+tabela[1][i]+tabela[2][i]
        if soma==3 or soma ==-3:
            return 1

    diagonal1 = tabela[0][0]+tabela[1][1]+tabela[2][2]
    diagonal2 = tabela[0][2]+tabela[1][1]+tabela[2][0]
    if diagonal1==3 or diagonal1==-3 or diagonal2==3 or diagonal2==-3:
        return 1

    return 0

#CRIANDO A FUNÇÃO QUE MOSTRA A TABELA
def mostrar():
    for i in range(3):
        for j in range(3):
            if tabela[i][j] == 0:
                print(" _ ", end=' ')
            elif tabela[i][j] == 1:
                print(" X ", end=' ')
            elif tabela[i][j] == -1:
                print(" O ", end=' ')

        print()
                

#CHAMANDO A FUNÇÃO INICIO, A QUAL VAI PUXANDO AS OUTRAS
inicio()