numero = 45
pontos = 500
tentativas = 5
rodada = 1
while rodada <= tentativas:
    print(f'Rodada {rodada} de {tentativas}')
    chute = int(input('Digite seu palpite: '))

    if chute == numero:
        print('Acertou☺!!!')
        pontos += 100
        rodada = 6
    else:
        if chute < numero:
            print('Errou☺, chute menor que o numero')
            pontos -= 100
            rodada += 1
            
        elif chute > numero:
            print('Errou☺, chute maior que o numero')
            pontos -= 100
            rodada += 1
print('Fim de jogo ☻')
print(f'Seus pontos: {pontos}')