#Turtle graphics game
import turtle
import tkinter as Tk
import time
"""Set up screen"""
print("Welcome to F1 Race Car robot by YAHOZA\nThis current robot is a prototype and may not be used as the final version\n ..::WARNING::.. THIS GAME IS IN ALPHA V.0.2")
print("The current robot has 1 settings for controlling the robot.")
print("Please tap  'W/A/S/D ' keys to control the robot")

wn = turtle.Screen() # this is assigning the variable name "wn" to "turtle.screen" function
wn.bgcolor("#696969") # this code changes the background of the gui to "Dim Gray"

"""New turtle to draw the border"""

borderpen= turtle.Turtle()
borderpen.penup()
borderpen.setposition(-400,-400)  #(x,y)
borderpen.pendown()
borderpen.pensize(3)
for side in range (4):
    borderpen.forward(800)
    borderpen.left(90)
borderpen.hideturtle()

"""Create player race car"""
player = turtle.Turtle()
player.color("yellow")
player.shape("triangle")
player.shapesize(0.5,0.5)
player.penup()
player.speed(0)


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

"""Using "WASD" KeyBindings control"""
turtle.listen()
turtle.onkey(TurnLeft, "a")
turtle.onkey(TurnRight, "d")
turtle.onkey(IncreaseSpeed, "w")
turtle.onkey(decel, "s")



while True:
    player.forward(speed)
    #Force race car to return back to race track
    if player.xcor() > 400 or player.xcor() < -400:
        player.right(180)
    if player.ycor()> 400 or player.ycor() < -400:
        player.right(180)
    #Force player to decrease back to speed 1 when exceed or hit speed 20
    if speed >=10:
        speed -= 9
        print("WOAH WOAH, hold your horses, your engine is not gonna last")
        print("The current speed is")
        print(speed)
    
delay = raw_input("Press Enter to finish")
