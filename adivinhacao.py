def jogar():

    import random

    print('-------------------')
    print('Welcome to the game')
    print('-------------------')

    numero = random.randrange(1, 101)
    t_tentativas = 0
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('(1)Fácil (2)Médio (3)Difícil')
    dif = int(input('Digite um numero: '))

    if dif == 1:
        t_tentativas = 20
    elif dif == 2:
        t_tentativas = 10
    else:
        t_tentativas = 5

    for tentativas in range(1, t_tentativas + 1):
        print('Tentativa {} de {}'.format(tentativas, t_tentativas))
        chute_str = input('Digite um numero entre 1 e 100: ')

        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print('Somente numeros entre 1 e 100!')
            continue

        if (chute == numero):
            print('Você acertou!')
            break
        else:
            if (chute > numero):
                print('Você errou! Chutou muito alto')
            elif (chute < numero):
                print('Você errou! Chutou muito baixo')
            pontos -= abs(numero - chute)

    print('Você conseguiu fazer {} pontos'.format(pontos))
    print('------------')
    print('Fim de jogo!')
    print('------------')

if (__name__ == '__main__'):
    jogar()