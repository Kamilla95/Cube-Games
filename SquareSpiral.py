import turtle
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple']
t = turtle.Pen()
turtle.bgcolor('black')
sides = eval(input('Введите количество сторон от 2 до 6: '))
for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
    t.left(90)

