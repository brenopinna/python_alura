from random import randint
def jogar():
    print('===================================')
    print('BEM VINDO AO JOGO DA ADIVINHAÇÃO!!!')
    print('===================================\n')
    segredo = randint(1, 100)
    tentativas = 0
    pontos = 1000
    nivel = int(input('SELECIONE A DIFICULDADE:\n[1] Fácil\n[2] Médio\n[3] Difícil\nSUA OPÇÃO: '))
    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    elif nivel == 3:
        tentativas = 5
    for rodada in range(1, tentativas + 1):
        print(f'\nTentativa {rodada} de {tentativas}')
        chute = int(input('CHUTE UM VALOR DE 1 A 100: '))
        if chute < 1 or chute > 100:
            print('APENAS VALORES DE 1 A 100!!!')
            continue
        if chute == segredo:
            print(f'\033[32m\nACERTOU! Meu número é {chute}!\nVocê fez {pontos} ponto(s)!')
            print('FIM DE JOGO!\033[m')
            break
        else:
            if segredo > chute:
                print(f'\033[33mMeu número é maior que {chute}!\033[m')
            elif segredo < chute:
                print(f'\033[33mMeu número é menor que {chute}!\033[m')
            pontos = pontos - (abs(chute - segredo))
        if rodada == tentativas:
            print(f'\n'
                  f'\033[31mSUAS TENTATIVAS ACABARAM!\033[m\nVocê fez {pontos} ponto(s)!')
if __name__ == '__main__':
    jogar()