class Pipe:
    def __init__(self, x, height):
        self.x = x
        self.height = height
        self.width = 50  # Width of the pipe
        self.gap = 150  # Gap between the top and bottom pipes

    def move(self, speed):
        self.x -= speed

    def draw(self, surface):
        # Draw the top pipe
        top_pipe_rect = pygame.Rect(self.x, 0, self.width, self.height)
        surface.blit(pipe_image, top_pipe_rect)

        # Draw the bottom pipe
        bottom_pipe_rect = pygame.Rect(self.x, self.height + self.gap, self.width, surface.get_height() - self.height - self.gap)
        surface.blit(pipe_image, bottom_pipe_rect)

    def collide(self, bird):
        # Check for collision with the bird
        bird_rect = pygame.Rect(bird.x, bird.y, bird.width, bird.height)
        top_pipe_rect = pygame.Rect(self.x, 0, self.width, self.height)
        bottom_pipe_rect = pygame.Rect(self.x, self.height + self.gap, self.width, surface.get_height() - self.height - self.gap)

        return bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect)