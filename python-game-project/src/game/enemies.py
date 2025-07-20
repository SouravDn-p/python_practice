class Enemy:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 5

    def spawn(self):
        # Logic to spawn the enemy at a specific location
        pass

    def move(self):
        self.rect.x -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)