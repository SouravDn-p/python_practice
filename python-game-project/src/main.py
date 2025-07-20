import pygame
import sys
from game.player import Player
from game.enemies import Enemy

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    player = Player()
    enemies = []
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear the screen with black
        player.update()  # Update player state
        player.draw(screen)  # Draw player

        for enemy in enemies:
            enemy.update()  # Update enemy state
            enemy.draw(screen)  # Draw enemy

        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Maintain the frame rate

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()