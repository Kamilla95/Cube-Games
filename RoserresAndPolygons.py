import turtle
t = turtle.Pen()

sides = int(turtle.numinput('Количество сторон',
                        'Сколько сторон будет у фигуры?', 4))

for m in range(5, 75):
    t.left(360/sides + 5)
    t.width(m // 25 + 1)
    t.penup()
    t.forward(m * 4)
    t.pendown()
    if (m % 2 == 0):
        for n in range(sides):
            t.circle(n/3)
            t.right(360/sides)
    else:
        for k in range(sides):
            t.forward(k)
            t.right(360/sides)
