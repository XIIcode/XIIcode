import random as rnd
def get_input():
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
        value = True
    else:
        print("you have lost")
    return value
print("Note use of letters and strings will crash the program.")
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
else:
    print("you have lost")
    choice = str(input('Do you want to play agin (y)/(n) :'))
    while choice.isnumeric():
        print("Use letters")
        choice = str(input('Do you want to play agin (y)/(n)'))
    if choice.lower() == 'y':
        print("You have three trials remaining")
        for x in range(3):
            user_result = playagain(random_result,a,b)
            if user_result:
                break
    elif choice.lower() == 'n':               
        exit()
        