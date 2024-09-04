
# Snake Game - Turtle Graphics

This is a classic Snake game built using Python's `turtle` graphics.  It is designed with a grid for a better player experience. It's a great examples for the advantages of OOP.

## Features
- **Snake Movement**: Control the snake using `W`, `A`, `S`, and `D` keys for up, left, down, and right movements.
- **Food Collection**: The snake can eat food to grow longer and increase the score.
- **Wall Collision Detection**: If the snake hits the wall, the game resets.
- **Tail Collision Detection**: If the snake collides with its own tail, the game resets.
- **Scoreboard**: A running tally of the score is displayed, which resets after each collision.
  
## Game Components
This game is divided into three Python classes, each in its own file:
1. **Snake**: Handles the creation and movement of the snake.
2. **Food**: Represents the food that appears randomly on the screen.
3. **Scoreboard**: Keeps track of the player's score and handles game reset logic.

## Installation and Setup
1. Ensure you have Python installed on your system.
2. Clone the repository:
   \`\`\`bash
   git clone <repository-url>
   \`\`\`
3. Install the necessary dependencies if required (e.g., turtle graphics is included in standard Python installations).

4. Run the game:
   \`\`\`bash
   python main.py
   \`\`\`

## How to Play
- The objective is to control the snake and collect food that appears on the screen.
- Each time the snake eats food, it grows longer, and your score increases.
- Avoid running into the walls or your own tail to keep playing.
- How many pieces can you eat without dying?


## Customization
The game grid is currently set to 680x680 pixels with snake segments that are 40px each. You can adjust the screen size and snake segment size in the `main.py` file as per your preference:
\`\`\`python
screen.setup(width=680, height=680)
# Snake segments are 40x40 pixels each
\`\`\`




## License
This project is licensed under the MIT License.