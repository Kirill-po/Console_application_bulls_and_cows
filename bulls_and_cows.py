import random

def finding_a_number(mass, enemy_try, bulls, cows):   #Нахождение ненужных чисел компьютером
    for num in mass[:]:
        temp_bulls, temp_cows = fight(num, enemy_try)
        if temp_bulls != bulls or temp_cows != cows:
            mass.remove(num)
    return mass

def number_player(): #Ввод пользователем его числа
    while True:
        number = input("Enter 4 non-repeat number: ")
        if(len(number) == 4) and number.isdigit():
            number = list(map(int,number))
            if len(set(number)) == 4:
                break
            else:
                continue
        else:
            continue
    return number
def all_options(): #Генерация всех вариантов 4 неповторяющихся чисел
    mass_options = []
    for i in range(10000):
        option = str(i).zfill(4)
        if len(set(map(int, option))) == 4:
            mass_options.append(list(map(int, option)))
    return mass_options
def one_answer(answer):
    one = random.choice(answer)
    return one
def fight(enemy_number, number): #Функция сравнения чисел пользователя и компьютeра
    bulls, cows = 0, 0
    for i, num in enumerate(enemy_number):
        if num in number:
            if enemy_number[i] == number[i]:
                bulls+=1
            else:
                cows+=1
    return bulls, cows

answers = all_options()
print ("Welcome to game bulls and cows!")
print ("********Let's beginning********")
print("guess the number, the computer will try to guess it")
player = number_player()
option_computer = one_answer(answers)


while True:
    print('-' * 10, "Your move", '-' * 10)   #Попытка пользователя угадать число
    print('-' * 7, "guess the number", '-' * 6)
    player_n = number_player()
    bulls, cows = fight(player_n, option_computer)
    print("Bulls: ", bulls, "; Cows", cows)
    if bulls == 4:
        print('-' * 11, "You win!", '-' * 10)
        break

    enemy_try = one_answer(answers)   #Попытка компьютера угадать число
    print('=' * 9, "Enemy move", '=' * 9)
    print("Enemy think your number is: ", enemy_try)
    bulls, cows = fight(enemy_try, player)
    print("Bulls: ", bulls, "; Cows", cows)
    if bulls == 4:
        print('-' * 11, "Enemy win!", '-' * 10)
        print("number enemy is ", option_computer)
        break
    else:
        answers = finding_a_number(answers, enemy_try, bulls, cows)


print("for new game, restart project")
