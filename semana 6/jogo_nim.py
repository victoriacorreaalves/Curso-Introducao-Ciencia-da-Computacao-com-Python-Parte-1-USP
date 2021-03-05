#jogo do NIM
#usuário define número de peças totais e número máximo de peças que podem ser retiradas
#ganha aquele que retirar a última peça

def computador_escolhe_jogada(n, m):
# Analisa se consegue tirar todas as peças do tabuleiro e ganhar
# caso não, analisa se consegue tirar multiplo de m+1
# caso não, retira m
    if (n <= m):
        return n
    else:
        k = n % (m+1)
        if k > 0:
            return k
    return m

def usuario_escolhe_jogada(n, m):
# solicita quantas peças o usuário quer retirar e analisa se o valor é válido
    i = 0
    while i == 0:
        i = int(input("Quantas peças você vai tirar? "))
        if i > n or i < 1 or i > m:
            print()
            print("Oops! Jogada inválida! Tente de novo")
            print()
            i = 0
    return i

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
#quando c é True é vez do computador
    c= True

    if n % (m+1) == 0: 
        c = False
        print()
        print("Você começa!")
        print()
    else:
        print()
        print("Computador começa!")
        print()

    while n > 0:

        if c:
            jogada = computador_escolhe_jogada(n, m)
            c = False
            if(jogada == 1):
                print()
                print("O computador tirou uma peça.")
            else:
                print()
                print("O computador tirou", jogada, " peças.")
        else:
            jogada = usuario_escolhe_jogada(n, m)
            c = True
            if(jogada == 1):
                print()
                print("Você tirou uma peça.")
            else:
                print()
                print("Você tirou", jogada, "peças.")
                print()

        n = n - jogada

        if(n == 1):
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if(n > 1):
                print("Agora restam", n, "peças no tabuleiro.")
                print()
# sai do laço quando n=0
# se c é True então o usuário ganhou
    if c:
        print("Fim do jogo! Você ganhou!")
        return 1
    else:
        print("Fim do jogo! O computador ganhou!")
        return 0

def campeonato():
# Repete três vezes e soma os resultados para mostrar o placar
    usuario = 0
    computador = 0
    x = 1
    while (x<4):
        print()
        print("**** Rodada", x,"****")
        print()
        x = x + 1
        vencedor = partida()
        if vencedor == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1
    print()
    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você", usuario," x ",computador, "Computador")

#início

j = 0

while j == 0:
    print("")
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    j = int(input())
    if j == 1:
        partida()    
    else:
        if j == 2:
            print("Voce escolheu um campeonato!")
            print("")
            campeonato() 
        else:
            print("Escolha uma opção válida!")
            print("")
            j = 0
