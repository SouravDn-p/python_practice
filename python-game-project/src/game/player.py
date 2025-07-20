class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)  # Example dimensions for the player
        self.gravity = 0.5
        self.jump_strength = -10
        self.velocity_y = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def jump(self):
        self.velocity_y = self.jump_strength

    def update(self):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 128, 255), self.rect)  # Example color for the player