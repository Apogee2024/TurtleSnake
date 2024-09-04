from turtle import Turtle

# Constants for direction control
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SEGMENT_SIZE = 40  # Set the segment size to 20 pixels (default size of each turtle)

class Snake:
    def __init__(self):
        # List to store all the snake segments
        self.segments = []
        self.create_snake()  # Create initial snake of 3 segments
        self.head = self.segments[0]  # The first segment is the head

    def create_snake(self):
        """Creates the initial snake with 3 segments, spaced 20 pixels apart."""
        starting_positions = [(0, 0), (-SEGMENT_SIZE, 0), (-2 * SEGMENT_SIZE, 0)]  # 20 pixel spacing
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment to the snake at a given position."""
        new_segment = Turtle(shape='square')
        new_segment.shapesize(stretch_wid=2, stretch_len=2)  # Stretch each segment to 40x40 pixels
        new_segment.color('white', 'white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        """Moves the snake by updating the position of each segment."""
        # Move each segment to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # X coordinate of the segment in front
            new_y = self.segments[seg_num - 1].ycor()  # Y coordinate of the segment in front
            self.segments[seg_num].goto(new_x, new_y)  # Move to that position

        # Move the head of the snake forward by 20 pixels (segment size)
        self.head.forward(SEGMENT_SIZE)

    def up(self):
        """Changes the snake's direction to up if it's not currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes the snake's direction to down if it's not currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changes the snake's direction to left if it's not currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes the snake's direction to right if it's not currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        """Extends the snake by adding a segment to the end."""
        # Add a new segment at the position of the last segment
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """Resets the snake by clearing the current segments and creating a new snake."""
        # Move all segments off the screen before clearing the list
        for seg in self.segments:
            seg.goto(1000, 1000)  # Moves the segments off-screen
        self.segments.clear()  # Clear the current segments
        self.create_snake()  # Create a new snake with 3 segments
        self.head = self.segments[0]  # Set the new head
