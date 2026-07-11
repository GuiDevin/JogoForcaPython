import random
import os
import time
import sys


def jogarFor():
    impreme_mensagem_abertura()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    desenha_forca(0)
    print(*letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1

        desenha_forca(erros)
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(*letras_acertadas)

    if (acertou):
        impreme_mensagem_vencedor()
    else:
        impreme_mensagem_perdedor()


def impreme_mensagem_abertura():
    print("*********************************")
    print("bem vindo ao jogo da forca!")
    print("*********************************")


def carregar_palavra_secreta():
    arquivo = open("palavras_secretas.txt", "r")
    palavras_secretas = []

    for linha in arquivo:
        linha = linha.strip()
        palavras_secretas.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras_secretas))
    palavra_secreta = palavras_secretas[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    lista = ["_" for letra in palavra]
    return lista


def pede_chute():
    chute = input("Chute uma letra? ")
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra.upper()):
            letras_acertadas[index] = letra
        index += 1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 0):
        print(" |            ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \\|    ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \\|/   ")
        print(" |       |    ")
        print(" |      / \\   ")

    print(" |            ")
    print("_|___         ")
    print()


def impreme_mensagem_vencedor():
    print("Você acertou! ")


def impreme_mensagem_perdedor():
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    frame1 = """
    GAME OVER! VOCÊ FOI ENFORCADO...

                  ______
               .d$$$$$$$$b.
             .d$$$$$$$$$$$$b.
            d$$$$$$$$$$$$$$$$b
           d$$$$$$$$$$$$$$$$$$b
          d$$$$$$$$$$$$$$$$$$$$b
          $$$$$$P"  ""P$$$$$$$$$
          $$$$P"  _  _  "P$$$$$$
          $$$P   (o)(o)   $$$$$$
          $$$     "  "     $$$$$
          $$$b   .____.   d$$$$$
          "$$$$b  \\__/  md$$$$P
            "$$$$b____md$$$$P"
              "$$$$$$$$$$P"
                m$$$$$$P"
               d$$$$$$P
"""

    frame2 = """
    GAME OVER! VOCÊ FOI ENFORCADO...

                  ______
               .d$$$$$$$$b.
             .d$$$$$$$$$$$$b.
            d$$$$$$$$$$$$$$$$b
           d$$$$$$$$$$$$$$$$$$b
          d$$$$$$$$$$$$$$$$$$$$b
          $$$$$$P"  ""P$$$$$$$$$
          $$$$P"  👁️  👁️  "P$$$$$$
          $$$P   (o)(o)   $$$$$$
          $$$      __      $$$$$
          $$$b   \\____/   d$$$$$
          "$$$$b        md$$$$P
            "$$$$b____md$$$$P"
              "$$$$$$$$$$P"
                m$$$$$$P"
               d$$$$$$P
"""

    if os.name == 'nt':
        os.system('')

    for _ in range(8):
        for frame in [frame1, frame2]:
            sys.stdout.write("\033[H")
            sys.stdout.write(frame)
            sys.stdout.flush()
            time.sleep(0.4)


if (__name__ == "__main__"):
    jogarFor()
