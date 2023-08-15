import turtle

t = turtle.Pen()
turtle.bgcolor('black')
colors = ['red', 'yellow', 'blue', 'orange', 'green', 'purple', 'white', 'gray']

sides = int(turtle.numinput('Сколько сторон', 'Сколько сторон выхотите?', 4, 1, 8))
your_name = turtle.textinput('Введите свое имя', 'Как тебя зовут?')

for x in range(360):
    t.pencolor(colors[x % sides])
    t.penup()
    t.forward(x * 3 / sides + x)
    t.pendown()
    t.write(your_name, font = ('Arial', int((x + sides) / sides), 'bold'))
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
    
