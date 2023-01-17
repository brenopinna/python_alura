import random

def jogar():
    mensagem_abertura()
    palavra_secreta = escolher_palavra_secreta()

    letras_certas = letras_em_branco(palavra_secreta)
    print(letras_certas)

    erros = 0

    while '_' in letras_certas and erros < 7:

        chute = pede_chute()

        if chute in palavra_secreta:
            salva_chute_certo(chute, palavra_secreta, letras_certas)
        else:
            erros += 1
            desenha_forca(erros)

        print(letras_certas)
    if erros == 7:
        mensagem_derrota(palavra_secreta)
    else:
        mensagem_vitoria()

def mensagem_abertura():
    print('============================')
    print('BEM VINDO AO JOGO DA FORCA!!')
    print('============================\n')

def escolher_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()
    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def letras_em_branco(x):
    return['_' for letra in x]

def pede_chute():
    chute = input('CHUTE UMA LETRA: ').upper().strip()
    return chute

def salva_chute_certo(chute, palavra_secreta, letras_certas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_certas[index] = letra
        index += 1

def mensagem_derrota(palavra_secreta):
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

def mensagem_vitoria():
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
    print("_|___         \n")

if __name__ == '__main__':
    jogar()