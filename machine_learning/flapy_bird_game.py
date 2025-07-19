import pygame
import sys
import random

# Game constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
BIRD_WIDTH = 40
BIRD_HEIGHT = 30
PIPE_WIDTH = 70
PIPE_GAP = 150
GRAVITY = 0.5
JUMP_STRENGTH = -10
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

def draw_bird(bird_rect):
    pygame.draw.ellipse(screen, (255, 255, 0), bird_rect)

def draw_pipe(pipe_rect):
    pygame.draw.rect(screen, (0, 255, 0), pipe_rect)

def main():
    bird_rect = pygame.Rect(100, SCREEN_HEIGHT // 2, BIRD_WIDTH, BIRD_HEIGHT)
    bird_movement = 0
    pipes = []
    score = 0
    running = True

    def create_pipe():
        height = random.randint(100, 400)
        top_pipe = pygame.Rect(SCREEN_WIDTH, 0, PIPE_WIDTH, height)
        bottom_pipe = pygame.Rect(SCREEN_WIDTH, height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - height - PIPE_GAP)
        return top_pipe, bottom_pipe

    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1500)
    pipes.extend(create_pipe())

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird_movement = JUMP_STRENGTH
            if event.type == SPAWNPIPE:
                pipes.extend(create_pipe())

        bird_movement += GRAVITY
        bird_rect.y += int(bird_movement)

        # Move pipes
        pipes = [pipe.move(-3, 0) for pipe in pipes if pipe.right > 0]

        # Collision detection
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                running = False

        if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
            running = False

        # Score
        for pipe in pipes:
            if pipe.right == bird_rect.left:
                score += 0.5  # Each pair counts as 1

        # Drawing
        screen.fill((135, 206, 235))
        draw_bird(bird_rect)
        for pipe in pipes:
            draw_pipe(pipe)
        score_surface = font.render(str(int(score)), True, (255, 255, 255))
        screen.blit(score_surface, (SCREEN_WIDTH // 2, 20))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()