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

        # Tells User to press space to start
        font = pygame.font.SysFont('Arial', 32)  # Font and size
        text_surface = font.render("Press SPACE to Start", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
        game_started = False
        game_over = False

        # Game over text
        game_over_font = pygame.font.SysFont('Arial', 50)
        game_over_surface = game_over_font.render("Game Over", True, (255, 0, 0))
        game_over_rect = game_over_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        # Restart instruction text
        restart_surface = font.render("Press SPACE to Restart", True, (0, 0, 0))
        restart_rect = restart_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5))

        # Initialize background (will move before the game starts)
        background = Background(speed=3, screen_width=SCREEN_WIDTH, img_file="assets/background.jpg")

        # Initialize bird (visible at the start)
        bird = Bird(x=50, y=150, img_file="assets/bird.png")

        # Initialize pipes only after the game starts
        pipes = []

        # Initialize score
        score = Score(font_size=32, color=(0, 0, 0))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not game_started:  # Start the game
                            game_started = True
                            score.reset()  # Reset score at the start of a new game
                            pipes = [Pipe(x=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)]  # Initialize pipes
                            bird = Bird(x=50, y=150, img_file="assets/bird.png")  # Reset bird
                        elif game_over:  # Reset the game after a game over
                            game_over = False
                            game_started = True
                            score.reset()  # Reset score at the start of a new game
                            bird = Bird(x=50, y=150, img_file="assets/bird.png")  # Reset bird
                            pipes = [Pipe(x=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT)]  # Re-initialize pipes
                        bird.flap()  # Bird flaps when space is pressed

            # Update background, it moves even before the game starts
            background.update()

            if not game_over and game_started:
                # Update game objects
                bird.update()

                # Check if the bird goes off the screen (above or below)
                if bird.y < -100 or bird.y > SCREEN_HEIGHT + 100:
                    game_over = True  # End the game if the bird goes off the screen

                # Update pipes
                for pipe in pipes:
                    pipe.update(3)
                    if pipe.x + pipe.pipe_width < 0:  # Remove pipes when they go off screen
                        pipes.remove(pipe)
                        pipes.append(Pipe(x=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT))

                    # Check if the bird passed the pipe
                    if not pipe.passed and pipe.x + pipe.pipe_width < bird.x:
                        pipe.passed = True
                        score.increment()  # Add a point when the bird successfully passes a pipe

                # Check for collisions
                for pipe in pipes:
                    top_pipe, bottom_pipe = pipe.get_rects()
                    if bird.get_rect().colliderect(top_pipe) or bird.get_rect().colliderect(bottom_pipe):
                        game_over = True  # End the game on collision

            # Draw everything
            background.draw(screen)  # Draw background
            bird.draw(screen)  # Draw bird
            for pipe in pipes:  # Draw pipes
                pipe.draw(screen)
            score.draw(screen, 10, 10)  # Display score in the top-left corner

            if game_over:
                screen.blit(game_over_surface, game_over_rect)  # Draw "Game Over" text
                screen.blit(restart_surface, restart_rect)  # Draw "Press SPACE to Restart" text

            if not game_started and not game_over:
                screen.blit(text_surface, text_rect)  # Draw "Press SPACE to Start" text

            # Refresh display
            pygame.display.flip()
            clock.tick(60)  # Limit FPS to 60

        pygame.quit()