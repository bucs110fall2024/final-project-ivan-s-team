import pygame
class Bird:
    def __init__(self, x, y, img_file ="assets/bird.png"):
        """
        Create the Bird object
        - x = x-coordinate of bird
        - y = y-coordinate of bird
        - img_file : str - path to Bird's image
        """

        self.x = x
        self.y = y
        self.startingy = y
        self.gravity = 0.5
        self.velocity = 0
        self.max_velocity = 10
        self.flap_power = -10
        self.image = pygame.image.load(img_file)
        self.image = pygame.transform.scale(self.image, (35, 35))  # Resize the image
        self.flap_triggered = False

    def flap(self):
        """
        Makes the bird flap upwards
        """
        self.velocity = self.flap_power  # Reset the velocity to flap upwards
        self.flap_triggered = True  # Ensure gravity starts


    def update(self):
        """
        Updates the bird's current position
        """
        if self.flap_triggered:
            self.velocity += self.gravity
            if self.velocity > self.max_velocity:
                self.velocity = self.max_velocity

        self.y += self.velocity

    def draw(self, screen):
        """
        Draws the bird on screen
        """
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        """
        Get the bird's rectangular area for collision detection
        """
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())