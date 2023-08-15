import turtle
t = turtle.Pen()

number = int(turtle.numinput('Количество сторон или окружностей',
                        'Сколько сторон или окружностей будет у фигуры?', 6))

shape = turtle.textinput('Какую фигуру вы хотите?',
                         'Введите "м" для многоугольника или "р" для розетки:')

for x in range(number):
    if shape == 'р':
        t.circle(100)
    else:
        t.forward(150)
    t.left(360/number)
