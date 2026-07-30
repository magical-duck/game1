import random
import sys
import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
CELL_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

COLOR_BG = (30, 30, 30)
COLOR_SNAKE = (0, 255, 0)
COLOR_FOOD = (255, 80, 80)
COLOR_TEXT = (240, 240, 240)
COLOR_GAME_OVER = (255, 255, 0)


def draw_text(surface, text, size, color, pos):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, pos)


def place_food(snake):
    while True:
        position = (random.randrange(GRID_WIDTH), random.randrange(GRID_HEIGHT))
        if position not in snake:
            return position


def draw_grid(surface):
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(surface, (40, 40, 40), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, (40, 40, 40), (0, y), (SCREEN_WIDTH, y))


def draw_snake(surface, snake):
    for part in snake:
        rect = pygame.Rect(part[0] * CELL_SIZE, part[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, COLOR_SNAKE, rect)


def draw_food(surface, food):
    rect = pygame.Rect(food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, COLOR_FOOD, rect)


def show_game_over(surface, score):
    surface.fill(COLOR_BG)
    draw_text(surface, "Game Over", 64, COLOR_GAME_OVER, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4))
    draw_text(surface, f"Score: {score}", 48, COLOR_TEXT, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    draw_text(surface, "Press R to restart or Q to quit", 28, COLOR_TEXT, (SCREEN_WIDTH // 6, SCREEN_HEIGHT * 3 // 4))
    pygame.display.flip()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2),
             (GRID_WIDTH // 2 - 1, GRID_HEIGHT // 2),
             (GRID_WIDTH // 2 - 2, GRID_HEIGHT // 2)]
    direction = (1, 0)
    food = place_food(snake)
    score = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if game_over:
                    if event.key == pygame.K_r:
                        return main()
                    continue
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        if not game_over:
            head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
            if (
                head[0] < 0 or head[0] >= GRID_WIDTH
                or head[1] < 0 or head[1] >= GRID_HEIGHT
                or head in snake
            ):
                game_over = True
            else:
                snake.insert(0, head)
                if head == food:
                    score += 1
                    food = place_food(snake)
                else:
                    snake.pop()

        screen.fill(COLOR_BG)
        draw_grid(screen)
        draw_snake(screen, snake)
        draw_food(screen, food)
        draw_text(screen, f"Score: {score}", 28, COLOR_TEXT, (10, 10))

        if game_over:
            show_game_over(screen, score)
        else:
            pygame.display.flip()

        clock.tick(10)


if __name__ == "__main__":
    main()
