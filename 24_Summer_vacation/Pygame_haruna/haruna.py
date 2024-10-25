import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1800, 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Heart Shooter with Moving Targets")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Bubble settings
BUBBLE_RADIUS = 20
MAX_BUBBLES = 100

# Target settings
TARGET_WIDTH = 80
TARGET_HEIGHT = 80
NUM_TARGETS = 12  # Total number of targets

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Define the Bubble class
class Bubble:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (BUBBLE_RADIUS * 2, BUBBLE_RADIUS * 2))  # Resize image
        self.radius = BUBBLE_RADIUS
        self.dx = 10 * math.cos(math.radians(90))
        self.dy = -10 * math.sin(math.radians(90))

    def draw(self, screen):
        # Draw the image
        screen.blit(self.image, (self.x - self.radius, self.y - self.radius))

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off the walls
        if self.x - self.radius <= 0 or self.x + self.radius >= WIDTH:
            self.dx = -self.dx
        if self.y - self.radius <= 0:
            self.dy = -self.dy

# Define the Launcher class
class Launcher:
    def __init__(self, x, y, bubble_image):
        self.x = x
        self.y = y
        self.angle = 90  # Start aiming straight up
        self.bubble_image = bubble_image
        self.bubble = self.new_bubble()

    def new_bubble(self):
        return Bubble(self.x, self.y, self.bubble_image)

    def draw(self, screen):
        self.bubble.draw(screen)
        # Draw the triangular shooter
        point1 = (self.x + 30 * math.cos(math.radians(self.angle)), self.y - 30 * math.sin(math.radians(self.angle)))
        point2 = (self.x + 15 * math.cos(math.radians(self.angle + 135)), self.y - 15 * math.sin(math.radians(self.angle + 135)))
        point3 = (self.x + 15 * math.cos(math.radians(self.angle - 135)), self.y - 15 * math.sin(math.radians(self.angle - 135)))
        pygame.draw.polygon(screen, BLACK, [point1, point2, point3])

    def move_left(self):
        self.angle += 5
        if self.angle > 160:  # Restricting angle to left maximum of 160 degrees
            self.angle = 160

    def move_right(self):
        self.angle -= 5
        if self.angle < 20:  # Restricting angle to right maximum of 20 degrees
            self.angle = 20

    def shoot(self):
        bubble = self.bubble
        bubble.dx = 10 * math.cos(math.radians(self.angle))
        bubble.dy = -10 * math.sin(math.radians(self.angle))
        self.bubble = self.new_bubble()
        return bubble

# Initialize targets
targets = []
target_colors = []
target_speeds = []
for _ in range(NUM_TARGETS):
    target_x = random.randint(0, WIDTH - TARGET_WIDTH)
    target_y = random.randint(100, HEIGHT // 2)  # Random Y position in the upper half of the screen
    targets.append(pygame.Rect(target_x, target_y, TARGET_WIDTH, TARGET_HEIGHT))
    target_colors.append(random_color())  # Assign a random color to each target
    target_speeds.append(random.choice([-3, 3]))  # Random speed and direction for each target

# Load bubble image
bubble_image = pygame.image.load("heart.png")

# Initialize launcher
launcher = Launcher(WIDTH // 2, HEIGHT - 50, bubble_image)

# Game loop
running = True
bubbles = []
remaining_bubbles = MAX_BUBBLES
clock = pygame.time.Clock()
spacebar_pressed = False

# Font setup
font = pygame.font.SysFont(None, 36)

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not spacebar_pressed and remaining_bubbles > 0:
                new_bubble = launcher.shoot()
                bubbles.append(new_bubble)
                spacebar_pressed = True
                remaining_bubbles -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                spacebar_pressed = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        launcher.move_left()
    if keys[pygame.K_RIGHT]:
        launcher.move_right()
    
    # Update bubbles
    for bubble in bubbles[:]:
        bubble.update()
        bubble.draw(screen)
        if bubble.y > HEIGHT:
            bubbles.remove(bubble)
    
    # Update targets
    for i, target in enumerate(targets):
        target.x += target_speeds[i]
        
        # Check for collision with the left wall
        if target.left <= 0:
            target.x = 0  # Adjust position to prevent sticking
            target_speeds[i] = -target_speeds[i]  # Reverse direction
            
        # Check for collision with the right wall
        if target.right >= WIDTH:
            target.x = WIDTH - TARGET_WIDTH  # Adjust position to prevent sticking
            target_speeds[i] = -target_speeds[i]  # Reverse direction
            
        pygame.draw.rect(screen, target_colors[i], target)  # Draw the target with its assigned color

    # Check for collisions
    for bubble in bubbles[:]:
        for target in targets[:]:
            if target.collidepoint(bubble.x, bubble.y):
                target_index = targets.index(target)
                targets.remove(target)
                target_colors.pop(target_index)  # Remove the corresponding color
                target_speeds.pop(target_index)  # Remove the corresponding speed
                bubbles.remove(bubble)
                break

    # Draw launcher
    launcher.draw(screen)

    # Draw remaining bubbles and targets
    remaining_targets_text = font.render(f"Remaining Targets: {len(targets)}", True, BLACK)
    screen.blit(remaining_targets_text, (10, 10))
    
    remaining_bubbles_text = font.render(f"Remaining Bubbles: {remaining_bubbles}", True, BLACK)
    screen.blit(remaining_bubbles_text, (10, 50))

    # Check for game over
    if len(targets) == 0:
        game_over_text = font.render("Game Over! All targets cleared.", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

