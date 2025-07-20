def load_image(image_path):
    """Load an image from the specified path."""
    try:
        image = pygame.image.load(image_path)
        return image
    except pygame.error as e:
        print(f"Unable to load image: {image_path}. Error: {e}")
        return None

def reset_game():
    """Reset the game state to its initial conditions."""
    # Implement game state reset logic here
    pass