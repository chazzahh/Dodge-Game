import pygame
import random
from sys import exit
from random import randint

def display_score():

    
    current_time = pygame.time.get_ticks() - start_time
    score_surface = font.render(f"Score: {current_time}", False, dark_colour)
    score_rect = score_surface.get_rect(center = (400, 50))
    #pygame.draw.rect(screen, light_colour, score_rect)
    #pygame.draw.rect(screen, dark_colour, score_rect, 2)
    screen.blit(score_surface, score_rect)
    return current_time
    
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            screen.blit(torso_surface, obstacle_rect)
        return obstacle_list
    else:
        return []



pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Dodge')
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0

#colours and visuals
font = pygame.font.Font('font/intenso-serif.ttf', 20) #(font type, font size)
dark_colour = pygame.Color("#4D3F3D")
light_colour = pygame.Color("#EAEDBB")

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#Obstacles
torso_surface = pygame.image.load('graphics/snail/torso.png').convert_alpha()
torso_rect = torso_surface.get_rect(bottomright=(600,300))

obstacle_rect_list = []

#score_surface = font.render('Dodge', False, dark_colour) #(text, AA, colour)
#score_rect = score_surface.get_rect(center = (400,50))

#if working with pixel art, AA = False
positions_list = [i for i in range(900,1400)]
#torso_pos_x = 600 #(600, 250) start pos



player_surface = pygame.image.load('graphics/player/av_run1.png').convert_alpha()
player_rect = player_surface.get_rect(topleft = (80,200)) #or midbottom = (80,300)
player_gravity = 0

player_stand = pygame.image.load('graphics/player/av_stand.png').convert_alpha()
player_stand_scaled = pygame.transform.scale(player_stand, (100, 200))
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = font.render('Dodge', False, light_colour)
game_name_rect = game_name.get_rect(center = (400, 80))

game_instruction = font.render('Press Space to play', False, light_colour)
game_instruction_rect = game_instruction.get_rect(center = (400, 380))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500) #trigger obs timer every 900 milisec



while True:




    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #shows position of mouse if mouse moves
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -18

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity =-18
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #press space to restart
                game_active = True
                torso_rect.x = random.choice(positions_list)
                start_time = pygame.time.get_ticks()

        if event.type == obstacle_timer and game_active:
            obstacle_rect_list.append(torso_surface.get_rect(bottomright=(randint(900,1100),300)))


    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,280))
        

        #screen.blit(score_surface, score_rect)

        score = display_score()

        #torso
        #torso_rect.x -=4
        #if torso_rect.x <=0:
            #torso_rect.x = random.choice(positions_list)
            
        #screen.blit(torso_surface,(torso_rect))

        #player
        player_gravity+=0.5
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface,player_rect) #use rect





        #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)





        #collision
        if torso_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill(dark_colour)
        screen.blit(player_stand_scaled, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        screen.blit(game_instruction, game_instruction_rect)
        
        score_text = font.render(f"Score: {score}", False, light_colour)
        score_text_rect = score_text.get_rect(center = (400, 330))

        if score ==0:
            screen.blit(game_instruction, game_instruction_rect)
        else:
            screen.blit(score_text, score_text_rect)



    mouse_pos = pygame.mouse.get_pos()


    pygame.display.update()
    clock.tick(60)

