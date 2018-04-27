import turtle
alex = turtle.Turtle()
wn = turtle.Screen()

fig_1 = [[(60,100),(-120,100),(-120,100),(90,100),(90,100),(90,100)],[(-90,200),(-90,100),(90,0)]]
fig_2 = [[(180,100),(-90,100),(-30,100),(-120,100),(-120,100),(135,100*2**0.5),(135,100)],[(-90,200),(-90,100),(90,0)]]
fig_3 = [[(90,100),(90,100),(90,100),(90,100),(45,50*2**0.5),(90,100*2**0.5),(90,100*2**0.5),(90,50*2**0.5)],[(45,50*(5+2**0.5)),(90,100),(-90,0)]]
fig_4 = [[(225,100*2**0.5),(135,100),(135,100*2**0.5),(-135,100),(-90,100),(135,50*2**0.5),(90,100*2**0.5),(90,100*2**0.5),(90,50*2**0.5),(135,100)],[]]
lista = [fig_1,fig_2,fig_3,fig_4]


def turtle_draw (trajetoria,t):
    """Executa a trajetoria para a turtle t"""

    for (ang,distancia) in trajetoria:
        t.left(ang)  # sentido anti-horário
        t.forward(distancia)



def draw_all (list,t):
    for fig in list:

        turtle_draw(fig[0],t)
        t.penup()
        turtle_draw(fig[1],t)
        t.pendown()

#turtle_draw (fig_2[0],alex)
alex.penup()
alex.forward(-350)
alex.pendown()
draw_all(lista,alex)
wn.mainloop()