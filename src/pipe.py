import pygame
import random

class Pipe:
    def __init__(self, x, screen_height, img_file="assets/pipe.png", gap_height=150, pipe_width=60):
        self.x = x
        self.screen_height = screen_height
        self.pipe_width = pipe_width
        self.gap_height = gap_height
        self.passed = False

        # Load the pipe image
        self.image = pygame.image.load(img_file)

        # Calculate top and bottom pipe heights based on gap and screen height
        self.top_height = random.randint(50, self.screen_height - self.gap_height - 50)
        self.bottom_height = self.screen_height - self.top_height - self.gap_height

        # Scale the pipe image based on the extended pipe heights
        self.top_image = pygame.transform.scale(self.image, (self.pipe_width, self.top_height))
        self.bottom_image = pygame.transform.scale(self.image, (self.pipe_width, self.bottom_height))

        # Set up the top and bottom pipe positions using the image
        self.top_pipe = pygame.Rect(self.x, 0, self.pipe_width, self.top_height)
        self.bottom_pipe = pygame.Rect(self.x, self.top_height + self.gap_height, self.pipe_width, self.bottom_height)

    def update(self, speed):
        self.x -= speed
        self.top_pipe.x = self.x
        self.bottom_pipe.x = self.x

    def draw(self, screen):
        flipped_image = pygame.transform.flip(self.top_image, False, True)
        screen.blit(flipped_image, self.top_pipe.topleft)  # Draw flipped top pipe at the top
        screen.blit(self.bottom_image, self.bottom_pipe.topleft)  # Draw normal bottom pipe

    def get_rects(self):
        # Returns the full Rect objects for both pipes
        return self.top_pipe, self.bottom_pipe