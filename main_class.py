import pygame
import random
from sys import exit
from random import randint

def display_score():

    
    current_time = pygame.time.get_ticks() - start_time
    score_surface = font.render(f"Score: {current_time}", False, light_colour)
    score_rect = score_surface.get_rect(center = (320, 320))

    screen.blit(score_surface, score_rect)
    return current_time
    
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(torso_surface, obstacle_rect)
            else:
                screen.blit(head_surface, obstacle_rect)

        obstacle_list = [i for i in obstacle_list if i.x >-100]
        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True


def player_animation():
    global player_surface, player_index, player_j_index

    #if on floor
    if player_rect.bottom <280:
        player_index +=0.1
        if player_index >= len(player_jump):
            player_index = 0
        player_surface = player_jump[int(player_index)]
    else:
        player_index +=0.24 #framerate and animation rate
        if player_index >= len(player_walk):
            player_index = 0
        player_surface = player_walk[int(player_index)]

    #if in air

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Dodge')
clock = pygame.time.Clock()
game_active = False
start_time = 0
score = 0

#colours and visuals
font = pygame.font.Font('font/intenso-serif.ttf', 20) #(font type, font size)
bold_font = pygame.font.Font('font/intenso-serif.ttf', 40)
dark_colour = pygame.Color("#4D3F3D")
light_colour = pygame.Color("#EAEDBB")

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

#Obstacles
torso_surface = pygame.image.load('graphics/snail/torso.png').convert_alpha()
head_surface = pygame.image.load('graphics/fly/head1.png')

obstacle_rect_list = []

#score_surface = font.render('Dodge', False, dark_colour) #(text, AA, colour)
#score_rect = score_surface.get_rect(center = (400,50))

#if working with pixel art, AA = False

#torso_pos_x = 600 #(600, 250) start pos



player_w1 = pygame.image.load('graphics/player/av_run1.png').convert_alpha()
player_w2 = pygame.image.load('graphics/player/av_run2.png').convert_alpha()
player_w3 = pygame.image.load('graphics/player/av_run3.png').convert_alpha()
player_w4 = pygame.image.load('graphics/player/av_run4.png').convert_alpha()
player_w5 = pygame.image.load('graphics/player/av_run5.png').convert_alpha()
player_w6 = pygame.image.load('graphics/player/av_run6.png').convert_alpha()
player_w7 = pygame.image.load('graphics/player/av_run7.png').convert_alpha()
player_w8 = pygame.image.load('graphics/player/av_run8.png').convert_alpha()

player_j1 = pygame.image.load('graphics/player/avjump1.png').convert_alpha()
player_j2 = pygame.image.load('graphics/player/avjump2.png').convert_alpha()
player_j3 = pygame.image.load('graphics/player/avjump3.png').convert_alpha()
player_j4 = pygame.image.load('graphics/player/avjump4.png').convert_alpha()
player_j5 = pygame.image.load('graphics/player/avjump5.png').convert_alpha()
player_j6 = pygame.image.load('graphics/player/avjump6.png').convert_alpha()
player_j7 = pygame.image.load('graphics/player/avjump7.png').convert_alpha()
player_j8 = pygame.image.load('graphics/player/avjump8.png').convert_alpha()
player_j9 = pygame.image.load('graphics/player/avjump9.png').convert_alpha()

player_jump = [player_j1,player_j2,player_j3,player_j4,player_j5,player_j3,player_j4,player_j6,player_j7,player_j8]
player_walk = [player_w1,player_w2,player_w3,player_w4,player_w5,player_w6,player_w7,player_w8]
player_j_index = 0
player_w_index = 0
player_index = 0
player_surface = player_walk[player_index]


player_rect = player_surface.get_rect(topleft = (80,200)) #or midbottom = (80,300)
player_gravity = 0

player_stand = pygame.image.load('graphics/player/title_screen.png').convert_alpha()
player_stand_scaled = pygame.transform.scale(player_stand, (400, 200))
player_stand_rect = player_stand.get_rect(center = (350,170))

game_name = bold_font.render('Dodge', False, light_colour)
game_name_rect = game_name.get_rect(center = (400, 50))

game_instruction = font.render('Press Space to play', False, light_colour)
game_instruction_rect = game_instruction.get_rect(center = (400, 350))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000) #trigger obs timer every 900 milisec



while True:

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                #shows position of mouse if mouse moves
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -12

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity =-12
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: #press space to restart
                game_active = True
                
                start_time = pygame.time.get_ticks()

        if event.type == obstacle_timer and game_active:
            if randint(0,2):
                obstacle_rect_list.append(torso_surface.get_rect(bottomright=(randint(900,1100),300)))
            else:
                obstacle_rect_list.append(head_surface.get_rect(bottomright=(randint(900,1100),180)))


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
        player_gravity+=0.4
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surface,player_rect) #use rect

        #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collision
        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        obstacle_rect_list.clear()
        screen.fill(dark_colour)
        screen.blit(player_stand_scaled, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        screen.blit(game_instruction, game_instruction_rect)
        player_rect.midbottom = (80,300)
        
        score_text = font.render(f"Score: {score}", False, light_colour)
        score_text_rect = score_text.get_rect(center = (400, 320))

        if score ==0:
            screen.blit(game_instruction, game_instruction_rect)
        else:
            screen.blit(score_text, score_text_rect)



    mouse_pos = pygame.mouse.get_pos()


    pygame.display.update()
    clock.tick(60)

