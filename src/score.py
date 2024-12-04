import pygame

class Score:
    def __init__(self, font_size=32, color=(0, 0, 0)):
        self.score = 0
        self.font = pygame.font.SysFont("Arial", font_size)
        self.color = color

    def increment(self):
        """Increase the score by 1."""
        self.score += 1

    def reset(self):
        """Reset the score to 0."""
        self.score = 0

    def draw(self, screen, x, y):
        """Draw the score on the screen."""
        score_surface = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_surface, (x, y))