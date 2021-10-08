import random

def jogar():

    print_welcome_message()

    secret_word = get_secret_word()
    checked_letters = ["_" for character in secret_word]
    print(checked_letters)
    
    game_over = False
    win = False
    errors = 0

    while(not game_over and not win):
        kick = get_user_kick()

        if kick in secret_word:
            check_success_kick(kick, secret_word, checked_letters)
        else:
            errors += 1
            print_wrong_kick_message(errors, 7)
        
        game_over = errors == 7
        win = "_" not in checked_letters

        print(checked_letters)

    if win:
        print_winner_message()
    else:
        print_lost_message(secret_word)
    print("Fim do jogo")

def print_welcome_message():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def get_secret_word():
    with open("palavras.txt", "r") as file:
        file = open("palavras.txt", "r")
        words = [line.strip() for line in file]

    return words[random.randrange(len(words))].upper()

def get_user_kick():
    kick = input("Qual letra?")
    return kick.strip().upper()

def check_success_kick(kick, secret_word, checked_letters):
    index = 0
    for letter in secret_word:
        if kick == letter:
            checked_letters[index] = letter
        index = index + 1

def print_lost_message(secret_word):
    print("Você foi enforcado!")
    print("A palavra era {}".format(secret_word))
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


def print_winner_message():
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

def print_wrong_kick_message(errors, max_attempts):
    print("Ops, você errou! Faltam {} tentativas.".format(max_attempts - errors))
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
