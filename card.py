import turtle

#!please run this file seperately with the main game loop to print the symbols
#uncomment the last eight lines when testing this file

class Witch_symbol:
    def __init__(self,playerid=1):
        self.playerid = playerid

    def print_card(self):
        turtle.speed(10)
        turtle.screensize(bg="black")
        turtle.pencolor("white")
        turtle.pensize(5)
        turtle.fillcolor("white")

        self.draw(0, 5)
        turtle.exitonclick()

    def draw(self, i, width):
        if i == width:
            return
        turtle.circle(30 + 20 * i, -180)
        return self.draw(i+1, width)


class Seer_symbol:
    def __init__(self,playerid=1):
        self.playerid = playerid

    def print_card(self):
        turtle.speed(10)
        turtle.screensize(bg="black")
        turtle.pencolor("white")
        turtle.pensize(5)
        turtle.fillcolor("white")

        turtle.circle(150, 360)
        turtle.circle(150, 36)
        turtle.left(72)
        turtle.forward(285)
        turtle.left(144)
        turtle.forward(285)
        turtle.left(144)
        turtle.forward(285)
        turtle.left(144)
        turtle.forward(285)
        turtle.left(144)
        turtle.forward(285)
        turtle.exitonclick()


class Villager_symbol:
    def __init__(self,playerid=1):
        self.playerid = playerid

    def print_card(self):
        turtle.speed(10)
        turtle.screensize(bg="black")
        turtle.pencolor("white")
        turtle.pensize(5)
        turtle.fillcolor("white")

        turtle.left(225)
        turtle.forward(100)
        turtle.left(180)
        turtle.forward(200)
        turtle.left(180)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(180)
        turtle.forward(200)
        turtle.left(180)
        turtle.forward(70)
        turtle.circle(5, 360)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(30)
        turtle.circle(5, 360)
        turtle.left(135)
        turtle.forward(5)
        turtle.begin_fill()
        turtle.forward(30 * (2 ** 0.5) - 10)
        turtle.right(90)
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(30 * (2 ** 0.5) - 10)
        turtle.right(90)
        turtle.forward(10)
        turtle.end_fill()
        turtle.right(90)
        turtle.forward((30 * (2 ** 0.5) - 5) / 2)
        turtle.right(180)
        turtle.circle(50, 360)
        turtle.exitonclick()


class Werewolf_symbol:
    def __init__(self,playerid=1):
        self.playerid = playerid

    def print_card(self):
        turtle.speed(10)
        turtle.screensize(bg="black")
        turtle.pencolor("white")
        turtle.pensize(5)
        turtle.fillcolor("white")

        self.draw()

        turtle.penup()
        turtle.goto(0, -200)
        turtle.pendown()
        self.draw()

        turtle.penup()
        turtle.goto(180, -100)
        turtle.pendown()
        self.draw()

        turtle.penup()
        turtle.goto(-180, -100)
        turtle.pendown()
        self.draw()
        turtle.exitonclick()

    def draw(self):
        turtle.circle(100, 360)
        turtle.circle(100, 45)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.circle(100, 90)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.circle(100, 225)

# a = Werewolf_symbol(1)
# a.print_card()
# b = Witch_symbol(1)
# b.print_card()
# c = Villager_symbol(1)
# c.print_card()
# d = Seer_symbol(1)
# d.print_card()





