import turtle

def draw_fig(turtType, edges):
    name = turtle.Turtle()
    if turtType == 'square':
        name.shape("turtle")
        name.color("blue")
        while edges >= 1:
            name.forward(100)
            name.right(90)
            edges = edges - 1
    elif turtType == 'circle':
        name.shape("arrow")
        name.color("white")
        name.circle(100)
    elif turtType == 'triangle':
        name.shape("arrow")
        name.color("green")
        while edges > 1:
            name.forward(100)
            name.left(120)
            edges = edges - 1
        name.forward(100)

def main():
    window = turtle.Screen()
    window.bgcolor("red")
    draw_fig('square', 4)
    draw_fig('circle', 1)
    draw_fig('triangle', 3)
    window.exitonclick()

if __name__ == "__main__":
    main()



        
    
