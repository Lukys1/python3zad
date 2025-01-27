import turtle
import random

window = turtle.Screen()
t = turtle.Turtle()
t.pensize(7)
t.shape('turtle')

i = 0

one = ""
two = ""
three = ""
four = ""
five = ""
six = ""

one = random.choice(['red','blue', 'yellow', 'green', 'purple', 'orange'])
two = random.choice(['red','blue', 'yellow', 'green', 'purple', 'orange'])
three = random.choice(['red','blue', 'yellow', 'green', 'purple', 'orange'])
four = random.choice(['red','blue', 'yellow', 'green', 'purple', 'orange'])
five = random.choice(['red','blue', 'yellow', 'green', 'purple', 'orange'])


while(i < 5):
    if(one == two or one == three or one == four or one == five):
        one = random.choice(['red','blue', 'yellow', 'green', 'purple', 'orange'])
        break
    i=i+1

while(two == one or two == three or two == four or two == five):
    two = random.choice(['red','blue', 'yellow', 'green', 'purple', 'orange'])
while(three == one or three == two or three == four or three == five):
    three = random.choice(['red','blue', 'yellow', 'green', 'purple', 'orange'])
while(four == one or four == two or four == five or four == three):
    four = random.choice(['red','blue', 'yellow', 'green', 'purple', 'orange'])
while(five == one or five == two or five == four or five == three):
    five = random.choice(['red','blue', 'yellow', 'green', 'purple', 'orange'])

spr = random.choice(['red','blue', 'yellow', 'green', 'purple', 'orange'])

t.penup()
def cir(kolor, x):
    t.goto(x, 200)
    t.pendown()
    t.color(kolor)
    t.begin_fill()
    t.circle(25)
    t.penup()
    t.end_fill()



cir(one, -200)
cir(two, -100)
cir(three, 0)
cir(four, 100)
cir(five, 200)


t.goto(0, 0)
t.pendown()
t.color(spr)
t.begin_fill()
t.circle(25)
t.penup()
t.end_fill()

if(spr == one or spr == two or spr == three or spr == four or spr == five):
    t.color('green')
    t.goto(-200, -100)
    t.write(f"Wygrałeś! Wylosowana kula ma kolor {spr}.", font=("Arial", 15, "bold"))
else:
    t.color('red')
    t.goto(-200, -100)
    t.write(f"Spróbuj jeszcze raz. Wylosowana kula ma kolor {spr}.", font=("Arial", 15, "bold"))

window.listen()
window.mainloop()