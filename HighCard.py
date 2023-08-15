suits = ['пики', 'бубны', 'черви', 'крести']
faces = ['двойка', 'тройка', 'четверка', 'пятерка',
         'шестерка', 'семерка', 'восьмёрка', 'девятка', 'десятка',
         'валет', 'дама', 'король', 'туз']

import random
keep_going = True

while keep_going:
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print('У меня ', my_face, ' ', my_suit)
    print('У вас ', your_face, ' ', your_suit)
    if faces.index(my_face) > faces.index(your_face):
        print('Я победил!')
    elif faces.index(my_face) < faces.index(your_face):
        print('Вы победили!')
    else:
        print('У нас ничья!')
    answer = input('Нажмите ENTER, чтобы продолжить или любую клавишу, чтобы выйти: ')
    keep_going = (answer == '')
