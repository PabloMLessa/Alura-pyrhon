import random

def escolhe_palavra():
    palavras = []
    with open('frutas.txt', 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())
    palavra = random.choice(palavras).lower()
    return palavra

def valida_chute(palavra, letras_acertadas, chute):
    indice = 0
    for letra in palavra:
        if chute == letra:
            letras_acertadas[indice] = chute
        indice += 1

def mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()    

def mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def jogar():
    print('O jogo começou')
    acertou = False
    enforcou = False
    palavra = escolhe_palavra()
    letras_acertadas = ['_' for letra in palavra]
    erros = 0
    while(not enforcou and not acertou):
        print(letras_acertadas)
        chute = input("Escolha uma letra: ").lower()
        chute.strip()
        if chute not in letras_acertadas:
            if chute in palavra:
                valida_chute(palavra, letras_acertadas, chute)
            else:
                desenha_forca(erros)
                erros += 1
        else:
            print('Letra já escolhida, escolha outra')
        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
    if acertou:
        mensagem_vencedor()
    else:
        mensagem_perdedor(palavra)
 
    


if __name__ == '__main__':
    jogar()
