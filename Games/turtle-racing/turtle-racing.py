import turtle
import time
import random

## creating the size of the screen for our race
WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "yellow", "purple", "black", "orange", "pink", "brown", "cyan"]

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of the turtles for the race (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Enter a valid number")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Enter a number between 2-10")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 10)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacing_turtles = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i+1) * spacing_turtles, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

## creating the screen for our race
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
