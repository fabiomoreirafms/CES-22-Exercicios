import turtle
def draw_a_star (t):
    # Draw a star of 100 units side
    for i in range(5):
        t.forward (100)
        t.right(144)
wn = turtle.Screen()
star = turtle.Turtle()
draw_a_star(star)
wn.mainloop()