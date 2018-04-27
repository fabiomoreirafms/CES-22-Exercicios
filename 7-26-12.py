import turtle
alex = turtle.Turtle()
wn = turtle.Screen()
lista = [(90,100),(-30,100),(-120,100),(-75,100*2**0.5),(135,100),
         (135,100*2**0.5),(-135,100),(-90,100)]

def turtle_draw (trajetoria,t):
    """Executa a trajetoria para a turtle t"""
    for (ang,distancia) in trajetoria:
        t.left(ang)  # sentido anti-horário
        t.forward(distancia)
    wn.mainloop()


turtle_draw (lista,alex)