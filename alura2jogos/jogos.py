import forca
import adivinhacao

print('=================')
print('Escolha seu jogo!')
print('=================\n')
jogo = int(input('Qual o jogo?\n[1] Adivinhação\n[2] Forca\nSUA OPÇÃO: '))
if jogo == 1:
    adivinhacao.jogar()
elif jogo == 2:
    forca.jogar()
