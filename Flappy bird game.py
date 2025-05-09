import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT =800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Game variables
GRAVITY = 0.25
BIRD_JUMP = -6
PIPE_WIDTH = 60
PIPE_GAP = 150
BIRD_WIDTH = 40
BIRD_HEIGHT = 40
BIRD_X = 50
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Fonts
font = pygame.font.SysFont('Arial', 32)

# Game clock
clock = pygame.time.Clock()

# Bird class
class Bird:
    def __init__(self):
        self.x = BIRD_X
        self.y = bird_y
        self.velocity = bird_velocity

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        if self.y < 0:
            self.y = 0
        if self.y > SCREEN_HEIGHT - BIRD_HEIGHT:
            self.y = SCREEN_HEIGHT - BIRD_HEIGHT

    def jump(self):
        self.velocity = BIRD_JUMP

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT))

# Pipe class
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(150, SCREEN_HEIGHT - PIPE_GAP)
        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - self.height - PIPE_GAP)

    def move(self):
        self.x -= 3
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

    def off_screen(self):
        return self.x < -PIPE_WIDTH

    def collide(self, bird_rect):
        return self.top_rect.colliderect(bird_rect) or self.bottom_rect.colliderect(bird_rect)

# Function to draw the score
def draw_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Main game loop
def game_loop():
    bird = Bird()
    pipes = [Pipe()]
    score = 0
    running = True
    while running:
        clock.tick(60)
        screen.fill(BLUE)  # background color
        bird.move()
        bird.draw()

        # Pipe movement and spawning
        for pipe in pipes:
            pipe.move()
            pipe.draw()

            if pipe.off_screen():
                pipes.remove(pipe)
                pipes.append(Pipe())
                score += 1  # Increase score when a pipe moves off screen

            if pipe.collide(pygame.Rect(bird.x, bird.y, BIRD_WIDTH, BIRD_HEIGHT)):
                running = False  # Game over if collision occurs

        # Check for bird input (space bar for jump)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # Draw the score
        draw_score(score)

        # Update display
        pygame.display.update()

    # Game Over
    game_over_text = font.render("Game Over!", True, WHITE)
    screen.blit(game_over_text, (SCREEN_WIDTH // 3, SCREEN_HEIGHT // 3))
    pygame.display.update()
    pygame.time.wait(2000)  # wait for 2 seconds before closing
    pygame.quit()

# Run the game
game_loop()
