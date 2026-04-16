import turtle
import random

# ===== Screen Setup =====
screen = turtle.Screen()
screen.title("Random Walk Simulation")
screen.bgcolor("black")
screen.setup(800, 600)

# ===== Walker Setup =====
walker = turtle.Turtle()
walker.shape("circle")
walker.color("white")
walker.pensize(3)
walker.speed(2000)

# ===== Start Position =====
x, y = 0, 0
walker.penup()
walker.goto(x, y)
walker.pendown()

# Random directions
directions = [(0, 10), (0, -10), (10, 0), (-10, 0)]

# Path colors
colors = ["red", "blue", "green", "yellow", "orange", "purple"]

# ===== Random Walk =====
for step in range(200):
    dx, dy = random.choice(directions)
    x += dx
    y += dy

    walker.pencolor(random.choice(colors))
    walker.goto(x, y)

# ===== End Marker =====
walker.penup()
walker.goto(x, y)
walker.dot(12, "red")

# ===== Result Text =====
distance = (x**2 + y**2) ** 0.5

info = turtle.Turtle()
info.hideturtle()
info.color("white")
info.penup()
info.goto(-350, 250)
info.write(
    f"Final Position: ({x}, {y}) | Distance: {distance:.2f}",
    font=("Arial", 14, "bold")
)

print("Simulation Complete!")
print("Final Position:", (x, y))
print("Distance from origin:", round(distance, 2))

screen.exitonclick()