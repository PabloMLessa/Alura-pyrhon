import random 


def jogar():
    rodada = 1
    numero = random.randint(1,100)
    print('O jogo começou')
    print('Escolha números entre 1 e 100')
    print('Dificuldades: \n[1] = Fácil\n[2] = Médio\n[3] = Difícil')
    dificuldade = input('Digite a dificuldade: ')
    if dificuldade == '1':
        tentativas = 10
        pontos = 200
    elif dificuldade == '2':
        tentativas = 5
        pontos = 100
    elif dificuldade == '3':
        tentativas = 3
        pontos = 60
    while rodada <= tentativas:
        print(f'Rodada {rodada} de {tentativas}')
        chute = int(input('Digite seu palpite: '))
        if chute == numero:
            print('Acertou☺!!!')
            break
        else:
            if chute < numero:
                print('Errou☺, chute menor que o numero')
                pontos -= 20
            elif chute > numero:
                print('Errou☺, chute maior que o numero')
                pontos -= 20
        rodada += 1
    print('Fim de jogo ☻')
    print(f'Seus pontos: {pontos}')


if __name__ == '__main__':
    jogar()