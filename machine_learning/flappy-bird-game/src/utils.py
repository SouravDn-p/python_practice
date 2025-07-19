def load_image(file_path):
    """Load an image from the specified file path."""
    import pygame
    image = pygame.image.load(file_path)
    return image

def check_collision(rect1, rect2):
    """Check if two rectangles collide."""
    return rect1.colliderect(rect2)

def display_score(screen, score, font, position):
    """Display the score on the screen."""
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_surface, position)