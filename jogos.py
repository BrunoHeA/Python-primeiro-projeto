def escolhe_jogo():

    import forca
    import adivinhacao

    print('-------------------')
    print('-Choose your game!-')
    print('-------------------')

    print('(1)Forca (2)Adivinhação')
    jogo = int(input('Escolha seu jogo: '))

    if jogo == 1:
        print('Jogando Forca')
        forca.jogar()
    elif jogo == 2:
        print('Jogando adivinhação')
        adivinhacao.jogar()

if (__name__ == '__main__'):
    escolhe_jogo()