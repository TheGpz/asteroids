import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #Création des groupes
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    #Ajout joueur aux groupes
    Player.containers = (updatable, drawable)
    #Init joueur
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    
    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        pygame.Surface.fill(screen, (0,0,0))
        for thing in drawable:
            thing.draw(screen)
        updatable.update(dt)
        pygame.display.flip()
        
        #Limite 60 FPS
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()