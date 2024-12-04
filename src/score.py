import pygame

class Score:
    def __init__(self, font_size=32, color=(0, 0, 0)):
        """
        Initializes the score object
        """

        self.score = 0
        self.font = pygame.font.SysFont("Arial", font_size)
        self.color = color

    def increment(self):
        self.score += 1 #Increase the score by 1

    def reset(self):
        self.score = 0  #Resets the score to 0 when user restarts game

    def draw(self, screen, x, y):
        score_surface = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_surface, (x, y))