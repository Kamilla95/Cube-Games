import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor('black')

circles = int(turtle.numinput('Количество спиралей',
                    'Сколько будет спиралей (2 - 6)?', 4, 2, 6))
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']

for m in range(100):
    t.circle(m)
    position = t.position()
    heading = t.heading()
    for n in range(int(m / 2)):
        t.pendown()
        t.pencolor(colors[n % circles])
        t.circle(2 * n)
        t.right(360 / circles - 2)
        t.penup
    t.setx(position[0])
    t.sety(position[1])
    t.setheading(heading)
    t.left(360 / circles + 2)
