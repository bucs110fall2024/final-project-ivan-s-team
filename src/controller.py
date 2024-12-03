import pygame
from src.bird import Bird
from src.background import Background
from src.pipe import Pipe
from src.score import Score

class Controller:
  def __init__(self):
    """
    Initializes controller object
    """
    pygame.init()

  def mainloop(self):
    """
    Mainloop for controller
    """
    SCREEN_WIDTH, SCREEN_HEIGHT = 600, 300
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird Inspo")
    clock = pygame.time.Clock()

    #Tells User to press space to start
    font = pygame.font.SysFont('Arial', 32)  # Font and size
    text_surface = font.render("Press SPACE to Start", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    game_started = False
    game_over = False

    #Game over text
    game_over_font = pygame.font.SysFont('Arial', 50)
    game_over_surface = game_over_font.render("Game Over", True, (255, 0, 0))
    game_over_rect = game_over_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Initialize Objects
    background = Background(speed=3, screen_width=SCREEN_WIDTH, img_file="assets/background.jpg")
    bird = Bird(x=50, y=150, img_file="assets/bird.png")
    pipes = [Pipe(x=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE:
                  if not game_started:
                    game_started = True
                  elif game_over:
                     game_over = False
                     bird = Bird(x=100, y=150, img_file="assets/bird.png", scale_width=50, scale_height=50)
                     pipes = [Pipe(x=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)]
                     bird.flap()
                  bird.flap()

        if not game_over:
          #update game objects
          background.update()
          bird.update()
          
          #update pipes
          for pipe in pipes:
            pipe.update(3)
            if pipe.x + pipe.pipe_width < 0:
                pipes.remove(pipe)
                pipes.append(Pipe(x=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT))

          for pipe in pipes:
            top_pipe, bottom_pipe = pipe.get_rects()
            if bird.get_rect().colliderect(top_pipe) or bird.get_rect().colliderect(bottom_pipe):
                game_over = True  # End the game on collision

        # Draw objects
        background.draw(screen)
        bird.draw(screen)
        for pipe in pipes:
           pipe.draw(screen)

        else:
          screen.blit(game_over_surface, game_over_rect)

        if not game_started and not game_over:
          screen.blit(text_surface, text_rect)

        # Refresh display
        pygame.display.flip()
        clock.tick(60)  # Limit FPS to 60

    pygame.quit()