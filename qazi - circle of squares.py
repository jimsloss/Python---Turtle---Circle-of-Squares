import turtle

draw = turtle.Turtle()
draw.speed(0)


def square(length, angle):
    for side in range(4):
        draw.forward(length)
        draw.right(angle)
        
for i in range(100):
    square(100,90)
    draw.right(11)

draw.color('red')
for i in range(100):
    square(30,90)
    draw.fillcolor('purple')
    draw.right(7)

draw.color('blue')
for i in range(100):
    square(150,90)
    draw.right(23)
    

    
