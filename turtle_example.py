import turtle

def draw_example():
    window = turtle.Screen()
    window.bgcolor("black")

    #brad
    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.color("white")
    brad.speed(20)

    for y in range (0,72):
        brad.right(5)
        for x in range (0,4):
            brad.forward(100)
            brad.right(90)

    #angie
    #angie = turtle.Turtle()
    #angie.shape("turtle")
    #angie.color("pink")
    #angie.speed(4)

    #angie.circle(100)

    #phil
    #phil = turtle.Turtle()
    #phil.shape("turtle")
    #phil.color("yellow")
    #phil.speed(10)

    #for y in range(0,3):
    #    phil.forward(300)
    #    phil.right(120)
    
    window.exitonclick()

draw_example()
