import turtle


def draw_a_star (t,w):
    # Draw a star of 100 units side
    w.bgcolor("lightgreen")
    t.color("hotpink")
    t.pensize(2)
    t.penup() # ajuste na janela
    t.back(150) # ajuste na janela
    t.pendown() # ajuste na janela
    for i in range(5):
        for j in range(5):
            t.forward (100)
            t.right(144)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()


wn = turtle.Screen()
star = turtle.Turtle()
draw_a_star(star,wn)
wn.mainloop()