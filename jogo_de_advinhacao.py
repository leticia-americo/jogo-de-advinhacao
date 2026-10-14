import random

novamente = "s"

recorde = 9999

while novamente == "s":

    numero = random.randint(1, 100)

    palpite = 0
    tentativa = 0

    while palpite != numero:
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativa += 1

        if palpite < 1 or palpite > 100:
            print("Número inválido! Digite apenas números entre 1 e 100, por favor.")
        elif numero == palpite:
            print(f"Parabéns, você ganhou em {tentativa} tentativa(s)!!")
        elif numero > palpite:
            print("O número secreto é MAIOR")
        else:
            print("O número secreto é MENOR")

    if tentativa < recorde:
        recorde = tentativa
        print(f"Seu novo record é {recorde} tentativa(s)!!")
    else:
        print(f"Seu recorde continua sendo {recorde} tentativa(s)")

    novamente = input("Gostaria de jogar novamente? (s/n): ")

print("Obrigada por jogar!!")
