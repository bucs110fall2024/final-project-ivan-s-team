import pygame

class Bird:
    def __init__(self, x, y, img_file="assets/bird.png"):
        """
        Initializes bird object
        - x : x-cordinate of bird
        - y : y-cordinate of bird
        - img_file : imports the bird png
        """

        self.x = x
        self.y = y
        self.startingy = y
        self.gravity = 0.5
        self.velocity = 0
        self.max_velocity = 10
        self.flap_power = -8
        self.image = pygame.image.load(img_file)
        self.image = pygame.transform.scale(self.image, (35, 35))  # Resize the image
        self.flap_triggered = False
        self.active = False

    def flap(self):
        self.velocity = self.flap_power
        self.flap_triggered = True
        self.active = True  # Start the bird's movement when it flaps

    def update(self):
        if self.active:  # Only apply gravity if the bird is active
            self.velocity += self.gravity
            if self.velocity > self.max_velocity:
                self.velocity = self.max_velocity
            self.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.image.get_width(), self.image.get_height())