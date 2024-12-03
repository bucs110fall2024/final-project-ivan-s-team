import pygame
import random

class Pipe:
    def __init__(self, x, screen_height, img_file="assets/pipe.png", gap_height=100, pipe_width=60):
        """
        Creates the pipes objects
        - x = x-coordinate of pipe
        - screen_height = height of the game screen
        - img_file = path to the pipe image
        - gap_height = the gap between top and bottom pipes
        """

        self.x = x
        self.screen_height = screen_height
        self.pipe_width = pipe_width
        self.gap_height = gap_height

        # Load and scale the pipe image
        self.image = pygame.image.load(img_file)
        self.image = pygame.transform.scale(self.image, (self.pipe_width, screen_height))

        # Randomly generate the top and bottom pipes' y-coordinate based on the gap
        self.top_height = random.randint(50, self.screen_height - self.gap_height - 50)
        self.bottom_height = self.screen_height - self.top_height - self.gap_height

        # Set up the top and bottom pipe positions using the image
        self.top_pipe = pygame.Rect(self.x, 0, self.pipe_width, self.top_height)
        self.bottom_pipe = pygame.Rect(self.x, self.top_height + self.gap_height, self.pipe_width, self.bottom_height)

    def update(self, speed):
        """
        Move the pipes leftward.
        - speed = speed of the pipe movement
        """
        self.x -= speed
        self.top_pipe.x = self.x
        self.bottom_pipe.x = self.x

    def draw(self, screen):
        """
        Draw the pipes on the screen using the pipe image.
        """
        flipped_image = pygame.transform.flip(self.image, False, True) 
        screen.blit(flipped_image, self.top_pipe.topleft)  
        screen.blit(self.image, self.bottom_pipe.topleft)  

    def get_rects(self):
        """
        Return the rectangles for collision detection.
        """
        return self.top_pipe, self.bottom_pipe