import pygame

from core.constants import FPS, WINDOW_SIZE
from core.grid import Grid
from core.snake import Snake

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("pySnek")
clock = pygame.time.Clock()

grid = Grid()
grid.create_background()
snake = Snake((5, 5))
snake.create_textures()
grid.add_snake(snake)

alive = False

# game loop
running = True
while running:
    # keep loop at right speed
    clock.tick(FPS)

    # process input events
    for event in pygame.event.get():

        # check for closing window
        if event.type == pygame.QUIT:
            running = False

        # snake control
        elif event.type == pygame.KEYDOWN:
            # move up
            if event.key == pygame.K_UP:
                snake.up()
            elif event.key == pygame.K_RIGHT:
                snake.right()
            elif event.key == pygame.K_DOWN:
                snake.down()
            elif event.key == pygame.K_LEFT:
                snake.left()
            elif event.key == pygame.K_KP_ENTER:
                alive = not alive

    if alive:
        # update
        snake.move()
        grid.feed_snake()
        running = not grid.rip_snake()
        grid.generate_items()

    # render
    grid.draw(screen)
    snake.draw(screen)

    # after drawing everything, display prepared image
    pygame.display.flip()


pygame.quit()


def main():
    return 0


if __name__ == "__main__":
    main()
