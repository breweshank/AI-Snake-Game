import pygame
import random
import numpy as np

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
cell_size = 20

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Eshank Snake Game')

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = RIGHT

    def move(self):
        head_x, head_y = self.body[0]
        move_x, move_y = self.direction
        new_head = (head_x + move_x * cell_size, head_y + move_y * cell_size)
        
        # Add the new head and remove the tail
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def check_collision(self):
        head = self.body[0]
        return (
            head in self.body[1:] or
            head[0] < 0 or head[0] >= width or
            head[1] < 0 or head[1] >= height
        )

# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, (width // cell_size) - 1) * cell_size,
                         random.randint(0, (height // cell_size) - 1) * cell_size)

    def respawn(self):
        self.position = (random.randint(0, (width // cell_size) - 1) * cell_size,
                         random.randint(0, (height // cell_size) - 1) * cell_size)

# AI to determine the next move
def ai_move(snake, food):
    head_x, head_y = snake.body[0]
    food_x, food_y = food.position

    if head_x < food_x:
        next_direction = RIGHT
    elif head_x > food_x:
        next_direction = LEFT
    elif head_y < food_y:
        next_direction = DOWN
    elif head_y > food_y:
        next_direction = UP
    else:
        next_direction = snake.direction  # Continue in the same direction

    return next_direction

# Main function
def main():
    snake = Snake()
    food = Food()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # AI decides the next move
        snake.direction = ai_move(snake, food)
        snake.move()

        # Check if snake eats the food
        if snake.body[0] == food.position:
            snake.grow()
            food.respawn()

        # Check for collision
        if snake.check_collision():
            print("bas kar!")
            running = False

        # Draw everything
        screen.fill(black)
        for segment in snake.body:
            pygame.draw.rect(screen, green, (segment[0], segment[1], cell_size, cell_size))
        pygame.draw.rect(screen, red, (food.position[0], food.position[1], cell_size, cell_size))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()

