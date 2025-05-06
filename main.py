# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from player import Player
from asteroid import Asteroid
from  constants import *
from asteroidfield import AsteroidField
from bullet import Bullet

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()

    bullets = pygame.sprite.Group()
    Bullet.containers = (bullets, updatable, drawable)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.isColliding(player):
                print("Game over!")
                sys.exit()
            for bullet in bullets:
                if asteroid.isColliding(bullet):
                    asteroid.split()
                    bullet.kill()

        pygame.Surface.fill(screen, (0,0,0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60fps
        dt = clock.tick(60)/1000

if  __name__ == "__main__":
    main()