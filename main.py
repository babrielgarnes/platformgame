import pygame
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
Gravity = -10

screen_height = 800
screen_width = 1000

white = (0, 0, 0)
green = (21, 128, 0)
skyblue = (128, 212, 255)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TODO: Change Title")


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.rect.Rect((x, y, width, height))

    def draw(self, surface):
        pygame.draw.rect(surface, green, self.rect)


class Player:
    jumpDuration = 50  # number of frames moving upwards
    jumpFrameCount = 0  # number of frames elapsed
    jumping = False

    def __init__(self):
        self.rect = pygame.rect.Rect((64, 64, 30, 30))

    # Defines movement of the player and edges of the screen
    def movement_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:  # left
            if self.rect.left > 3:
                self.rect.move_ip(-3, 0)
        if key[pygame.K_d]:  # right
            if self.rect.right < screen_width - 3:
                self.rect.move_ip(3, 0)
        if key[pygame.K_w]:  # up
            if onground:
                self.jumping = True

    def jump(self):
        self.rect.move_ip(0, -3)
        self.jumpFrameCount += 1
        if self.jumpFrameCount == self.jumpDuration:
            self.jumping = False
            self.jumpFrameCount = 0

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 128), self.rect)


player1 = Player()
ground = Platform(0, screen_height - 100, screen_width, 100)

environment = pygame.sprite.Group()
environment.add()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    onground = pygame.Rect.colliderect(player1.rect, ground)
    if player1.jumping:  # gravity 2.0
        player1.jump()
    elif onground:
        player1.rect.bottom = ground.rect.top
    else:
        player1.rect.move_ip(0, 3)

    screen.fill(skyblue)
    ground.draw(screen)

    player1.draw(screen)
    player1.movement_keys()

    pygame.display.update()
    FramePerSec.tick(FPS)

pygame.quit()