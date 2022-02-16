from tkinter import CENTER
import turtle
import winsound
wn=turtle.Screen()
wn.title("Ping pong por Lucas Simoes")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
#Barra 1

barra_1= turtle.Turtle()
barra_1.speed(0)
barra_1.shape("square")
barra_1.color("white")
barra_1.shapesize(stretch_wid=5,stretch_len=1)
barra_1.penup()
barra_1.goto(-350, 0)

#Barra 2

barra_2= turtle.Turtle()
barra_2.speed(0)
barra_2.shape("square")
barra_2.color("white")
barra_2.shapesize(stretch_wid=5,stretch_len=1)
barra_2.penup()
barra_2.goto(350, 0)

#Bola

bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.07
bola.dy = 0.07

#Texto-Placar
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier",24,"normal"))

#Score
score_1=0
score_2=0

#Funçoes
def barra_1_up():
    y= barra_1.ycor()
    y+=20
    barra_1.sety(y)
def barra_1_down():
    y= barra_1.ycor()
    y-=20
    barra_1.sety(y)

def barra_2_up():
    y= barra_2.ycor()
    y+=20
    barra_2.sety(y)
def barra_2_down():
    y= barra_2.ycor()
    y-=20
    barra_2.sety(y)

# Binding do teclado
wn.listen()
wn.onkeypress(barra_1_up, "w")
wn.onkeypress(barra_1_down, "s")
wn.onkeypress(barra_2_up, "Up")
wn.onkeypress(barra_2_down, "Down")
#Main Game Loop

while True:
    wn.update()
    #Movimento da bola

    bola.setx(bola.xcor()+bola.dx)
    bola.sety(bola.ycor()+bola.dy)

    #Checking the border
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        winsound.PlaySound("bounce", winsound.SND_ALIAS)
        
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
        winsound.PlaySound("bounce", winsound.SND_ALIAS)
        
    if bola.xcor() > 390: 
        bola.goto(0, 0)
        bola.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1,score_2), align="center", font=("Courier",24,"normal"))
    
    if bola.xcor() < -390: 
        bola.goto(0, 0)
        bola.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1,score_2), align="center", font=("Courier",24,"normal"))

    
    # Colisão da bola e da barra
    if (bola.xcor()> 340 and bola.xcor() <350) and (bola.ycor() < barra_2.ycor()+ 40 and bola.ycor()> barra_2.ycor() -40):
        bola.setx(340)
        bola.dx *= -1
        winsound.PlaySound("bounce", winsound.SND_ALIAS)
    
    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < barra_1.ycor()+ 40 and bola.ycor()> barra_1.ycor() -40):
        bola.setx(-340)
        bola.dx *= -1
        winsound.PlaySound("bounce", winsound.SND_ALIAS)
