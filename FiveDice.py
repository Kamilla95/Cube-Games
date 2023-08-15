import random

keep_going = True
while keep_going:
    dice = [0, 0, 0, 0, 0]
    for i in range(5):
        dice[i] = random.randint(1, 6)
    print('Вам выпало: ', dice)

    if dice[0] == dice[4]:
        print('Яцзы!')
    elif (dice[0] == dice[3]) or (dice[1] == dice[4]):
        print('Четыре одинаковых!')
    elif (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
        print('Три одинаковые')

    keep_going = (input('Нажмите ENTER для продолжения или любую клавишу, чтобы выйти') == '')
