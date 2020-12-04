import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0


# Create the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=600, height=600)
wn.tracer(0)


# Create the head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"


# Create the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []


# Pen for drawing the score board
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.pensize(3)
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

# Move the player up. But do not let him go down again
def go_up():
    if head.direction != "down":
        head.direction = "up"

# Move the player down. But not up again
def go_down():
    if head.direction != "up":
        head.direction = "down"

# Move the player right. But not left again
def go_right():
    if head.direction != "left":
        head.direction = "right"

# Move the player left. But not right again
def go_left():
    if head.direction != "right":
        head.direction = "left"


# Move the player by adding pixels to the coordinate, according to its direction
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# Listen for keypresses and move accordingly
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")




# Check for a collision with the food
def food_Collision():
    global score, high_score, delay

    if head.distance(food) < 20:
        # Move the food to a random position on the screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Speed up the game
        delay -= 0.001

        # Create a new body segment
        new_Segment = turtle.Turtle()
        new_Segment.speed(0)
        new_Segment.shape("square")
        new_Segment.color("gray")
        new_Segment.penup()
        segments.append(new_Segment)

        # Add to the score when food is eaten
        score += 1

        # Update the high score
        if score >= high_score:
            high_score = score

        # Redraw the scoreboard
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))



# Restart the game to the beginning again
def reset():
    head.goto(0, 0)
    head.direction = "stop"
    time.sleep(1)

    # Move the segments off the screen
    for segment in segments:
        segment.goto(1000, 1000)

    # Clear the segments array
    segments.clear()

    # Reset the score
    score = 0

    # Reset the game speed to normal again
    delay = 0.1

    # Redraw the scoreboard
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))



# Attach the new body segments to the snake head in reverse order
def attach_Segments():
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Attach the first segment to the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


# Check for border collisions
def border_Collision():
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        reset()


# Check for body collisions
def segments_Collision():
    for segment in segments:
        if segment.distance(head) < 20:
            reset()


# Main Game Function
def main():
    wn.update()

    border_Collision()

    food_Collision()

    attach_Segments()

    move()

    segments_Collision()

    time.sleep(delay)


# Main Game Loop
if __name__ == "__main__":
    while True:
        main()


