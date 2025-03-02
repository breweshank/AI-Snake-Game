# AI-Snake-Game
This is a **simple AI-controlled snake game** built using **Pygame**. It follows the traditional **Snake game mechanics**: a snake moves around the screen, eating food to grow while avoiding collisions with the screen edges and itself.

## Game Features:
1.**Automated Snake Movement:**

- The snake moves automatically towards the food using an AI-based movement strategy.
  
- The AI determines the shortest path to the food and updates the snake's direction accordingly.
  
2.**Food Mechanics:**
-The food appears at random locations on the grid.
-When the snake eats the food, it grows, and new food spawns.

3.**Collision Detection:**
-The game ends when the snake collides with itself or the screen borders.
-A message "bas kar!" (Hindi for "stop it!") is printed when a collision occurs.

4.**Real-time Graphics with Pygame:**
-The game window updates in real-time, showing the snake and food.
-The snake is drawn as green rectangles, and the food is a red square.
-The game runs at a speed of 10 frames per second (FPS).

## Real-time Graphics with Pygame:
-The game window updates in real-time, showing the snake and food.
-The snake is drawn as green rectangles, and the food is a red square.
-The game runs at a speed of 10 frames per second (FPS).

## How It Works:
-The Snake class handles movement, growth, and collision detection.
-The Food class randomly places food on the grid.
-The ai_move function calculates the next move based on the food's position.
-The main game loop updates the game state, moves the snake, checks for collisions, and redraws the screen.
