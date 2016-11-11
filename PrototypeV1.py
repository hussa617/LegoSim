#Turtle graphics game
import turtle
import tkinter as Tk
import time
"""Set up screen"""
print("Welcome to F1 Race Car robot by YAHOZA\nThis current robot is a prototype and may not be used as the final version\n ..::WARNING::.. THIS GAME IS IN ALPHA V.0.1")
time.sleep(3)
print("The current robot has 2 settings for controlling the robot.")
time.sleep(1)
print("Either using the arrow keys or the 'W/A/S/D ' keys")
time.sleep(1)
wn = turtle.Screen() # this is assigning the variable name "wn" to "turtle.screen" function
wn.bgcolor("#696969") # this code changes the background of the gui to "Dim Gray" 


"""Create player race car"""
player = turtle.Turtle()
player.color("yellow")
player.shape("triangle")
player.penup()

#Set speed variable
speed=1

"""Defining functions"""
def TurnLeft():
    player.left(30)

def TurnRight():
    player.right(30)

def IncreaseSpeed():
    global speed
    speed +=1
    print("The current speed is")
    print(speed)
def decel():
    global speed
    speed -=1
    print("The current speed is")
    print(speed)

"""Option 1 of KeyBindings"""
turtle.listen()
turtle.onkey(TurnLeft, "a")
turtle.onkey(TurnRight, "d")
turtle.onkey(IncreaseSpeed, "w")
turtle.onkey(decel, "s")
while True:
    player.forward(speed)





delay = raw_input("Press Enter to finish")
