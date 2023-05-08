import pygame
import random

# Initialize Pygame
pygame.init()

# Class settings to store all game settings
screen_width = 1200
screen_height = 800
screen_bg = (230,230,230)

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height), screen_bg)

# Set the game window caption
pygame.display.set_caption("Meagan's Alien Invasion")

# Load the player image
player_img = pygame.image.load("images/ship.bmp")

# Load the alien image
alien_img = pygame.image.load("alien.png")


# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x

        if self.rect.right > screen_width:
            self.rect.right = screen_width

        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)


# Define the alien class
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = alien_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speed_y

        if self.rect.top > screen_height + 10:
            self.rect.x = random.randrange(screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1, 8)


# Define the bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = x
        self.rect.bottom = y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y

        if self.rect.bottom < 0:
            self.kill()


# Initialize the game sprites
all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(8):
    alien = Alien()
    all_sprites.add(alien)
    aliens.add(alien)

# Set the game loop
running = True
clock = pygame.time.Clock()

while running:
    # Set the game FPS
