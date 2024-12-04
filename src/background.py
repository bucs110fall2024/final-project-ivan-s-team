import pygame

class Background:
    def __init__(self, speed, screen_width, img_file ="assets/background.jpg"):
        """
        Creates the moving background
        - speed - the speed of the moving background
        - screen_wdith - how big the screen is
        - img_file - background image
        """

        self.image = pygame.image.load(img_file)
        self.screen_width = screen_width
        self.speed = speed

        self.rect1 = self.image.get_rect(topleft=(0,0))
        self.rect2 = self.image.get_rect(topleft=(self.screen_width, 0))

    def update(self):
        """
        Updates the screens movement
        """
        self.rect1.x -= self.speed
        self.rect2.x -= self.speed

        if self.rect1.right <= 0:
            self.rect1.x = self.rect2.right
        if self.rect2.right <= 0:
            self.rect2.x = self.rect1.right

    def draw(self, screen):
        """
        Draw the background on the screen.
        """
        screen.blit(self.image, self.rect1.topleft)
        screen.blit(self.image, self.rect2.topleft)