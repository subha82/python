import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set up the turtle
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("red")
flower.speed(10)

# Function to draw a single petal
def draw_petal():
    for _ in range(2):
        flower.circle(100, 60)  # Draw a curve
        flower.left(120)         # Change direction
        flower.circle(100, 60)  # Draw another curve
        flower.left(120)         # Return to starting direction

# Function to draw the flower
def draw_flower():
    for _ in range(36):  # 36 petals (for a full flower)
        draw_petal()
        flower.left(10)  # Gradually change the direction to form the flower

# Draw the flower gradually
for i in range(36):  # Number of petals
    draw_petal()
    flower.left(10)  # Slightly rotate after drawing each petal

# Hide the turtle and show the final image
flower.hideturtle()

# Keep the window open
turtle.done()
