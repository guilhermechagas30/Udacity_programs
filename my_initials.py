import turtle

def draw_example():
    window = turtle.Screen()
    window.bgcolor("black")

    #brad
    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.color("black")
    brad.speed(2)

    brad.right(180)
    brad.forward(100)
    brad.color("white")
    brad.forward(200)
    
    brad.left(90)
    brad.forward(200)
    brad.left(90)
    brad.forward(200)
    brad.left(90)
    brad.forward(100)
    brad.color("black")
    brad.right(90)
    brad.forward(30)
    brad.color("white")
    brad.right(90)
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.left(90)
    brad.forward(100)
    brad.right(90)
    brad.color("black")
    brad.forward(30)
    brad.color("white")
    brad.right(90)
    brad.forward(100)

    brad.right(180)
    brad.forward(100)
    brad.color("black")
    brad.forward(30)
    brad.color("white")
    brad.right(90)
    brad.circle(10)

    brad.color("black")
    brad.forward(50)
    
    window.exitonclick()


draw_example()
