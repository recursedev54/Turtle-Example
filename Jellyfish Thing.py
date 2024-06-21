import turtle

def draw_tentacle(t, length, curl_factor):
    for _ in range(5):
        t.forward(length)
        t.right(curl_factor)

def draw_central_disc(t):
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color("pink")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.color("black")
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

def draw_side_view(t):
    t.penup()
    t.goto(-150, 50)
    t.pendown()
    t.color("purple", "yellow")
    t.begin_fill()
    t.circle(50, extent=180)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.circle(50, extent=180)
    t.left(90)
    t.forward(100)
    t.end_fill()

def main():
    window = turtle.Screen()
    window.bgcolor("white")

    # Create turtle
    jelly_turtle = turtle.Turtle()
    jelly_turtle.speed(0)
    jelly_turtle.width(2)

    # Draw Central Disc
    draw_central_disc(jelly_turtle)

    # Draw surrounding sections
    jelly_turtle.color("black")
    
    # Top left view (cross-sectional, yellow and pink)
    jelly_turtle.penup()
    jelly_turtle.goto(-200, 200)
    jelly_turtle.pendown()
    jelly_turtle.color("yellow", "pink")
    jelly_turtle.begin_fill()
    jelly_turtle.circle(30)
    jelly_turtle.end_fill()
    
    # Top center (reproductive organs, brown and beige)
    jelly_turtle.penup()
    jelly_turtle.goto(0, 200)
    jelly_turtle.pendown()
    jelly_turtle.color("brown", "beige")
    jelly_turtle.begin_fill()
    jelly_turtle.circle(20)
    jelly_turtle.end_fill()
    
    # Top right (cross-sectional, green and yellow)
    jelly_turtle.penup()
    jelly_turtle.goto(200, 200)
    jelly_turtle.pendown()
    jelly_turtle.color("green", "yellow")
    jelly_turtle.begin_fill()
    jelly_turtle.circle(30)
    jelly_turtle.end_fill()
    
    # Bottom left view
    jelly_turtle.penup()
    jelly_turtle.goto(-200, -150)
    jelly_turtle.pendown()
    jelly_turtle.color("pink", "yellow")
    jelly_turtle.begin_fill()
    jelly_turtle.circle(30)
    jelly_turtle.end_fill()
    
    # Bottom center (patterns, gold and white)
    jelly_turtle.penup()
    jelly_turtle.goto(0, -200)
    jelly_turtle.pendown()
    jelly_turtle.color("gold", "white")
    jelly_turtle.begin_fill()
    jelly_turtle.circle(20)
    jelly_turtle.end_fill()
    
    # Bottom right (side view, purple and yellow)
    draw_side_view(jelly_turtle)

    # Draw tentacles around the central disc
    jelly_turtle.penup()
    jelly_turtle.goto(0, -50)
    jelly_turtle.color("coral")
    for i in range(12):
        jelly_turtle.penup()
        jelly_turtle.setheading(i * 30)
        jelly_turtle.forward(50)
        jelly_turtle.pendown()
        draw_tentacle(jelly_turtle, 20, 45)
        jelly_turtle.penup()
        jelly_turtle.goto(0, -50)

    # Close window on click
    window.exitonclick()

if __name__ == "__main__":
    main()
