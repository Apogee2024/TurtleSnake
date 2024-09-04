from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        # Initialize the turtle as a food object
        self.shape('circle')  # Set shape to a circle
        self.penup()  # Prevent the turtle from drawing lines when moving

        # The default turtle size is 20x20, so this creates a 20x20 circle (half-size)
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.color('purple')  # Set the color of the food
        self.speed("fastest")  # Make movement as fast as possible

        # Position the food in a random location on the grid
        self.refresh()

    def refresh(self):
        # Generate random coordinates for food within the bounds of the screen (-280, 280)
        random_x_cor = random.randint(-280, 280)
        random_y_cor = random.randint(-280, 280)

        # Adjust to the nearest multiple of 20 to align the food with a grid
        grid_size = 40
        adjusted_x_cor = round(random_x_cor / grid_size) * grid_size
        adjusted_y_cor = round(random_y_cor / grid_size) * grid_size

        # Move the food to the new random position
        self.goto(adjusted_x_cor, adjusted_y_cor)
