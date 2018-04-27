import turtle

wn = turtle.Screen()
wn.setup(400,500)
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()
    tess.penup() # Deslocar para a posição do sinal verde
    tess.forward(40)
    tess.left(90)
    tess.forward(50)

draw_housing()

# Inicia o semáforo na posição verde
tess.penup()
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
wn.ontimer((),2000)

def h1():
    tess.penup()
    tess.forward(70)
    tess.fillcolor("orange")

def h2():
    tess.penup()
    tess.forward(70)
    tess.fillcolor("red")

def h3():
    tess.penup()
    tess.back(140)
    tess.fillcolor("green")

def traffic_light():
    """ Funcionamento do semáforo """
    wn.ontimer(h1(),2000)
    wn.ontimer(h2(),2000)
    wn.ontimer(h3(),2000)
    traffic_light()

traffic_light()

wn.mainloop()