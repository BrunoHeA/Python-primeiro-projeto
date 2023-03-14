def jogar():

    import random

    print('--------------------------------')
    print('Bem vindo ao jogo de adivinhação')
    print('--------------------------------')

    numero = random.randrange(1, 101)
    pontos = 1000

    print('Selecione a Dificuldade!')
    print('(1)Facil (2)Medio (3)Dificil')
    dif = int(input(''))

    if dif == 1:
        t_tentativas = 20
    elif dif == 2:
        t_tentativas = 10
    else:
        t_tentativas = 5

    tentativas = 1

    while tentativas <= t_tentativas:
        print('Tentativa {} de {}'.format(tentativas, t_tentativas))
        print('Digite um numero entre 1 e 100!')
        chute = int(input(''))
        if chute > 100 or chute < 1:
            print('SOMENTE NUMEROS ENTRE 0 E 100 AMIGÃO')
            tentativas += 1
            continue
        if chute == numero:
            print('Você acertou! parabens c:')
            break
        else:
            pontos -= abs(chute - numero)
            if chute > numero:
                print('Você errou! chutou muito alto amigão')
                tentativas += 1
            elif chute < numero:
                print('Você errou! chutou muito baixo amigão')
                tentativas += 1

    print('Você conseguiu {} pontos, parabens c:'.format(pontos))
    print('-----------')
    print('Fim de jogo')
    print('-----------')

if (__name__) == '__main__':
    jogar()