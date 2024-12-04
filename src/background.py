import pygame

class Background:
    def __init__(self, speed, screen_width, img_file ="assets/background.jpg"):
        """
        Initializes the background img
        - speed : the speed of the moving background
        - screen_wdith : how big the screen is
        - img_file : imports background image
        """

        self.image = pygame.image.load(img_file)
        self.screen_width = screen_width
        self.speed = speed

        self.rect1 = self.image.get_rect(topleft=(0,0))
        self.rect2 = self.image.get_rect(topleft=(self.screen_width, 0))

    def update(self):
        self.rect1.x -= self.speed
        self.rect2.x -= self.speed

        if self.rect1.right <= 0:
            self.rect1.x = self.rect2.right
        if self.rect2.right <= 0:
            self.rect2.x = self.rect1.right

    def draw(self, screen):
        screen.blit(self.image, self.rect1.topleft)
        screen.blit(self.image, self.rect2.topleft)