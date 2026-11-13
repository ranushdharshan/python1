
import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Font
font = pygame.font.SysFont("Arial", 25)

# Snake
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)

# Food
food = (
    random.randrange(0, WIDTH, CELL_SIZE),
    random.randrange(0, HEIGHT, CELL_SIZE)
)

score = 0
game_over = False

# Main game loop
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)

            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)

            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)

            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

            if game_over and event.key == pygame.K_SPACE:
                snake = [(100, 100), (80, 100), (60, 100)]
                direction = (CELL_SIZE, 0)
                food = (
                    random.randrange(0, WIDTH, CELL_SIZE),
                    random.randrange(0, HEIGHT, CELL_SIZE)
                )
                score = 0
                game_over = False

    if not game_over:

        # Move snake
        head = (
            snake[0][0] + direction[0],
            snake[0][1] + direction[1]
        )

        snake.insert(0, head)

        # Eat food
        if head == food:
            score += 1
            food = (
                random.randrange(0, WIDTH, CELL_SIZE),
                random.randrange(0, HEIGHT, CELL_SIZE)
            )
        else:
            snake.pop()

        # Check collision
        if (
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in snake[1:]
        ):
            game_over = True

    # Draw screen
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(
            screen, GREEN,
            (segment[0], segment[1], CELL_SIZE, CELL_SIZE)
        )

    # Draw food
    pygame.draw.rect(
        screen, RED,
        (food[0], food[1], CELL_SIZE, CELL_SIZE)
    )

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Game over screen
    if game_over:
        text = font.render("GAME OVER!", True, RED)
        restart = font.render("Press SPACE to Restart", True, WHITE)

        screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2 - 30))
        screen.blit(restart, (WIDTH // 2 - 130, HEIGHT // 2 + 10))

    pygame.display.update()
    clock.tick(10)
