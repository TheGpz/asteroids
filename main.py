import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Création des groupes
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #Ajout des objets aux groupes
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    
    #Init joueur
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    
    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        pygame.Surface.fill(screen, (0,0,0))
        for thing in drawable:
            thing.draw(screen)

        updatable.update(dt)

        #Asteroid - player collision and game over
        for each in asteroid:
            if each.collision(player):
                print("Game Over!")
                sys.exit()
        #Bullet & asteroid collision & kill
            for bullet in shots:
                if each.collision(bullet):
                    each.split()
                    bullet.kill()


        pygame.display.flip()
        
        #Limite 60 FPS
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()