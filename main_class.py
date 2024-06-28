import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Odd One Out')
clock = pygame.time.Clock()

#colours and visuals
font = pygame.font.Font('intenso-serif.ttf', 40) #(font type, font size)
dark_colour = pygame.Color("#4D3F3D")
light_colour = pygame.Color("#EAEDBB")

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

torso_surface = pygame.image.load('graphics/snail/torso.png').convert_alpha()
torso_rect = torso_surface.get_rect(bottomright=(600,300))

score_surface = font.render('Dodge', False, dark_colour) #(text, AA, colour)
score_rect = score_surface.get_rect(center = (400,50))
#if working with pixel art, AA = False
positions_list = [i for i in range(900,1400)]
#torso_pos_x = 600 #(600, 250) start pos



player_surface = pygame.image.load('graphics/player/av_run1.png').convert_alpha()
player_rect = player_surface.get_rect(topleft = (80,200)) #or midbottom = (80,300)
player_gravity = 0



while True:




    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
              #shows position of mouse if mouse moves
            if player_rect.collidepoint(event.pos):
                player_gravity = -20

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('p')



    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,280))
    
    pygame.draw.rect(screen, light_colour, score_rect)
    pygame.draw.rect(screen, dark_colour, score_rect, 2)

    screen.blit(torso_surface,(torso_rect))
    torso_rect.x -=4
    if torso_rect.x <=0:
        torso_rect.x = random.choice(positions_list)

    screen.blit(score_surface, score_rect)


    player_gravity+=1
    player_rect.y += player_gravity
    screen.blit(player_surface,player_rect) #use rect



    mouse_pos = pygame.mouse.get_pos()


    pygame.display.update()
    clock.tick(60)

