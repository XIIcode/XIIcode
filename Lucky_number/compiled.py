import random as rnd
import os
import winsound as ws
banner = '''
  _     _    _  _____ _  ____     __  _   _ _    _ __  __ ____  ______ _____  
 | |   | |  | |/ ____| |/ /\ \   / / | \ | | |  | |  \/  |  _ \|  ____|  __ \ 
 | |   | |  | | |    | ' /  \ \_/ /  |  \| | |  | | \  / | |_) | |__  | |__) |
 | |   | |  | | |    |  <    \   /   | . ` | |  | | |\/| |  _ <|  __| |  _  / 
 | |___| |__| | |____| . \    | |    | |\  | |__| | |  | | |_) | |____| | \ \ 
 |______\____/ \_____|_|\_\   |_|    |_| \_|\____/|_|  |_|____/|______|_|  \_\
'''
def loosegame():
    sound1 = "mixkit-crowd-disappointment-long-boo-463.wav"
    ws.PlaySound(sound1 , ws.SND_FILENAME)
def wongame():
    sound1 = "success-1-6297.wav"
    sound2 = "DVFAP2L-goofy-character-its-time-for-a-celebration.wav"
    sound3 = "level-win-6416.wav"
    ws.PlaySound(sound1 , ws.SND_FILENAME)
    ws.PlaySound(sound2 , ws.SND_FILENAME)
    ws.PlaySound(sound3 , ws.SND_FILENAME)
def exittinggame():
    sound = "mixkit-retro-arcade-game-over-470.wav"
    ws.PlaySound(sound , ws.SND_FILENAME)
def Duringplaying():
    sound = "ASHUTOSH-Jaipur.wav"
    ws.PlaySound(sound , ws.SND_FILENAME)
def lasttrial():
    sound = "alex-productions-epic-cinematic-trailer-elite.wav"
    ws.PlaySound(sound , ws.SND_FILENAME)
def welcomeMessage():
    sound = "example_1.wav"
    ws.PlaySound(sound , ws.SND_FILENAME)
def getBanner():
    os.system("cls")
    print(banner)
def get_input():
    user_range = str(input("Choose  a range of numbers e.g 0-75 and max=100 : "))
    while '-' not in user_range:
        print("Use '-' between the ranges")
        user_range = str(input("Choose  a range of numbers e.g 0-75 and max=100 : "))
    splitted_range = user_range.split('-')
    while not splitted_range[0].isnumeric() or not splitted_range[1].isnumeric():
        print("Forbidden Entry do not use letters or strings.Try again")
        user_range = str(input("Choose  a range of numbers e.g 0-75 and max=100 : "))
        while '-' not in user_range:
           print("Use '-' between the ranges") 
           user_range = str(input("Choose  a range of numbers e.g 0-75 and max=100 : "))
        splitted_range = user_range.split('-')
    while int(splitted_range[0]) > int(splitted_range[1]) or int(splitted_range[1]) > 100:
        print("Error Check your Range of Numbers.")
        user_range = str(input("Choose  a range of numbers e.g 0-75 and max=100 : "))
        while '-' not in user_range:
            user_range = str(input("Choose  a range of numbers e.g 0-75 and max=100 : "))
        splitted_range = user_range.split('-')
    return user_range
def playagain(winner_choice,start_range,end_range):
    value = False
    user_guess = int(input("Guess the lucky number : "))
    while (user_guess < start_range or user_guess > end_range):
        print("Choose appropriate number")
        user_guess = int(input("Guess the lucky number : "))
    if (user_guess == winner_choice):
        print("You have won the game")
        wongame()
        value = True
    else:
        print("you have lost")
    return value
def newGame():
    #Reuse the previous Functions
    value_range = get_input()
    x = value_range
    splitted_string = x.split('-')
    a , b = int(splitted_string[0]), int(splitted_string[1])
    random_result = rnd.randint(a,b)
    user_guess = int(input("Guess the lucky number : "))
    while (user_guess < a or user_guess > b):
        print("Choose appropriate number")
        user_guess = int(input("Guess the lucky number : "))
    if (random_result == user_guess):
        print("You have won the game")
        wongame()
        cont_quit_new_won = str(input("Do you want to continue playing or quit the game(y/n)?"))
        while cont_quit_new_won.lower() not in ('y','n'):
            print("Use the letters defined above")
            cont_quit_new_won = str(input("Do you want to continue playing or quit the game(y/n)?"))
        if cont_quit_new_won.lower() == 'y':
            newGame()
        elif cont_quit_new_won.lower() == 'n':
            exittinggame()
            exit()
    else:
        print("you have lost")
        loosegame()
        choice = str(input('Do you want to play again (y)/(n) :'))
        while choice.lower() not in ('y', 'n'):
            print("Use letters defined above")
            choice = str(input('Do you want to play again (y)/(n)'))
        if choice.lower() == 'y':
            print("You have three trials remaining")
            for x in range(3):
                user_result = playagain(random_result,a,b)
                if user_result:
                    cont_quit = str(input("Do you want to continue playing or quit the game(y/n)?"))
                    while cont_quit.lower() not in ('y', 'n'):
                        print("Use the letters defined above")
                        cont_quit = str(input("Do you want to continue playing or quit the game(y/n)?"))
                    if cont_quit.lower() == 'y':
                        newGame()
                    elif cont_quit.lower() == 'n':
                        exittinggame()
                        exit()
        elif choice.lower() == 'n':               
            new_quit = str(input("Do you want to play a new game? (y/n)"))
            while new_quit.lower() not in ('y','n'):
                print("Use letters defined below")
                new_quit = str(input("Do you want to play new game? (y/n)"))
            if new_quit.lower() == 'y':
                newGame()
            elif new_quit.lower() == 'n':
                exittinggame()
                exit()    
# Start of the execution of the program.
getBanner()
welcomeMessage()
value_range = get_input()
x = value_range
splitted_string = x.split('-')
a , b = int(splitted_string[0]), int(splitted_string[1])
random_result = rnd.randint(a,b)
user_guess = int(input("Guess the lucky number : "))
while (user_guess < a or user_guess > b):
    print("Choose appropriate number")
    user_guess = int(input("Guess the lucky number : "))
if (random_result == user_guess):
    print("You have won the game")
    wongame()
    cont_quit_won = str(input("Do you want to continue playing or quit the game(y/n)?"))
    while cont_quit_won.lower() not in ('y','n'):
        print("Use letters defined above")
        cont_quit_won = str(input("Do you want to continue playing or quit the game(y/n)?"))
    if cont_quit_won.lower() == 'y':
        newGame()
    elif cont_quit_won.lower() == 'n':
        exittinggame()
        exit()
else:
    print("you have lost")
    loosegame()
    choice = str(input('Do you want to play again (y)/(n) : '))
    while choice.lower() not in ('y', 'n'):
        print("Use letters defined above")
        choice = str(input('Do you want to play again (y)/(n) : '))
    if choice.lower() == 'y':
        print("You have three trials remaining")
        for x in range(3):
            user_result = playagain(random_result,a,b)
            if user_result:
                cont_quit = str(input("Do you want to continue playing or quit the game(y/n)?"))
                while cont_quit.lower() not in ('y', 'n'):
                    print("Use letters defined below")
                    cont_quit = str(input("Do you want to continue playing or quit the game(y/n)?"))
                if cont_quit.lower() == 'y':
                    newGame()
                elif cont_quit.lower() == 'n':
                    exit()
            elif x==1 and user_result == False:
                print("1 trial remaining")
                lasttrial()
            elif x == 2 and user_result == False:
                play_again_new_Game=str(input("Do you want to play a new game? (y/n)?"))
                while play_again_new_Game.lower() not in ('y', 'n'):
                    print("Use letters defined below")
                    play_again_new_Game=str(input("Do you want to play a new game? (y/n)?"))
                if play_again_new_Game.lower() == 'y':
                    newGame()
                elif play_again_new_Game.lower() == 'n':
                    exit()
    elif choice.lower() == 'n':               
        new_quit = str(input("Do you want to play a new game? (y/n)"))
        while new_quit.lower() not in('y','n'):
          print("Use letters defined below")
          new_quit = str(input("Do you want to play new game? (y/n)"))
        if new_quit.lower() == 'y':
          newGame()
        elif new_quit.lower() == 'n':
            exittinggame()
            exit()
        