import sys
import os
import time
import random

from CardClass import *

'''
Please run the code in the shell. Consider that it was created on OS Linux and the directory may need to be
changed on your computer.
'''

# Card Values
cards = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Paus", "Ouros", "Copas", "Espadas"]
# Separating by Suits.
splittingSuits = []

victories = 0
defeats = 0
points = open("points.txt", "r")

for i in range(13):
    splittingSuits.append(Cards(cards[i], cards[13]))
    splittingSuits.append(Cards(cards[i], cards[14]))
    splittingSuits.append(Cards(cards[i], cards[15]))
    splittingSuits.append(Cards(cards[i], cards[16]))


def Game(vt, dr):
    position = random.randint(0, 13)
    value_random = [splittingSuits[position].get_value(), splittingSuits[position].get_suit()]
    lifes = 15
    attempt = False
    os.system('clear') or None
    while not attempt:
        chosen_value = input("\n\n\n\n\n\t\tInsira um valor: ")
        chosen_suit = input("\n\n\t\tInsira um naipe: ")

        if chosen_value == value_random[0] and chosen_suit == value_random[1]:
            os.system('clear') or None
            print("\n\n\n\n\n\t\tParabéns Você Acertou!!!")
            input("\n\t   <<Pressione enter para continuar>>")
            vt += 1
            attempt = True
        else:
            if lifes == 1:
                os.system('clear') or None
                print("\n\n\n\n\n\n\n\n\n\t\t\t   Que pena você Perdeu.")
                input("\n\n\t\t\t<<Pressione enter para continuar>>")
                dr += 1
                break

            os.system('clear') or None
            print("\n\n\n\tO valor " + chosen_value + " é diferente do valor que foi escolhido.\n")
            if chosen_suit != value_random[1]:
                print("\tO naipe tambem é diferente\n")
            lifes -= 1
            print("\tagora lhe resta apenas " + str(lifes) + " vidas.")
    write_points(points, vt, dr)


def write_points(arqu, v, d):
    list_points = str(arqu.readlines())  # <-- Por algum motivo aqui as vezes vem vazio e buga, não encontrei por que.
    os.remove("/home/r1/PycharmProjects/pythonProject/testes/points.txt")
    file = open("points.txt", "w")
    concat1 = v + int(list_points[2])
    concat2 = d + int(list_points[4])
    file.write(str(concat1) + ";" + str(concat2) + ";" + "Developed by RITKILL")
    file.close()
    introduction()


def read_points():
    os.system('clear') or None
    print("\t\t\tGame Score\n\n")
    arqu = open("points.txt", "r")
    score = str(arqu.readlines())
    print("Vitorias: " + str(score[2]))
    print("Derrotas: " + str(score[4]))
    input("\n\t\t\t<<Pressione Enter para retornar ao menu>>")
    introduction()


def reset_points():
    os.system('clear') or None
    confirm = input("\n\n\n\n\n\n\n\n\tTem certeza que deseja resetar o placar[s/n]?: ")
    if confirm == 's' or confirm == 'S':
        os.remove("/home/r1/PycharmProjects/pythonProject/testes/points.txt")
        file = open("points.txt", "w")
        file.write("0;0;Developed by RITKILL")
        file.close()
        introduction()
    else:
        introduction()


def introduction():
    os.system('clear') or None
    print("\n\n\t\t\t\t Welcome to Game \n\t\t\t      ***Random Card!!!!***")
    print("\n\tDeveloped by R1TKILL.\t\t\tVersion: 1.0.0")
    print("\n\t 1 - Play \n\t 2 - Records \n\t 3 - Reset \n\t 4 - Exit\n")
    initChoice = int(input("Escolha: "))

    if initChoice == 1:
        os.system('clear') or None
        Game(victories, defeats)
    elif initChoice == 2:
        os.system('clear') or None
        read_points()
    elif initChoice == 3:
        os.system('clear') or None
        reset_points()
    elif initChoice == 4:
        os.system('clear') or None
        points.close()
        print("\n\n\n\n\t\tSaindo do Jogo em 3...")
        time.sleep(1)
        os.system('clear') or None
        print("\n\n\n\n\t\tSaindo do Jogo em 2...")
        time.sleep(1)
        os.system('clear') or None
        print("\n\n\n\n\t\tSaindo do Jogo em 1...")
        time.sleep(1)
        os.system('clear') or None
        sys.exit()
    else:
        os.system('clear') or None
        introduction()


introduction()
