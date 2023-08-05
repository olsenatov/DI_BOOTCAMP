            
import pygame
from board import board
import math

#basic settings for the game - variables
pygame.init()

SCREENHEIGHT = 950
SCREENWIDTH = 900

screen = pygame.display.set_mode([SCREENWIDTH, SCREENHEIGHT])

timer = pygame.time.Clock()
fps = 60

font = pygame.font.Font('assets/RobotoMono-Medium.ttf', 20)

level = board
color = 'green'

PI = math.pi

player_images = []
for i in range(1,5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45)))
player_x = 450
player_y = 663

direction = 0
counter = 0
flicker = False

valid_turns = [False, False, False, False] # can I go right/left/up/down now?
direction_command = 0
player_speed = 2

score = 0


def check_collisions(score_p):
    num1 = SCREENHEIGHT - 50 // 32
    num2 = SCREENWIDTH // 30
    if 0 < player_x < 870:
        if level[center_y // num1 ][center_x // num2] == 1:
               level[center_y // num1 ][center_x // num2] == 0
               score_p += 10 
    return score_p
        
    
#draw_board
def draw_board():
    num1 = ((SCREENHEIGHT - 50) // 32)
    num2 = (SCREENWIDTH // 30)
    
    for i in range(len(level)):
        for j in range(len(level[i])):
            # 0 = empty black rectangle
            
            if level[i][j] == 1: # dot
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4)
            
            if level[i][j] == 2 and not flicker: # big dot 
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)  
            
            if level[i][j] == 3: # vertical line 
                 pygame.draw.line(screen, color, (j * num2 +(0.5 * num2), i * num1), (j * num2 +(0.5 * num2), i * num1 + num1), 3)            
            
            if level[i][j] == 4: # horizontal line
                pygame.draw.line(screen, color, (j * num2, i * num1 +(0.5 * num1)), (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
                 
            if level[i][j] == 5: # top right corner line
               pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], 0, PI / 2, 3)
                  
            if level[i][j] == 6: # top right corner line
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
                
            if level[i][j] == 7: # bottom left corner line
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.5 * num1)), num2, num1], PI, 3*PI / 2, 3)
                               
            if level[i][j] == 8: # bottom right corner line
                 pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.5)), (i * num1 - (0.5 * num1)), num2, num1], 3*PI / 2, 2*PI, 3)
                
            if level[i][j] == 9: # gate
                pygame.draw.line(screen, 'white', (j * num2, i * num1 +(0.5 * num1)), (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
                  
def draw_player():
    if direction == 0: #right
        screen.blit(player_images[counter // 5], (player_x, player_y))
    elif direction == 1: #left
        screen.blit(pygame.transform.flip(player_images[counter // 5], True, False ), (player_x, player_y))
    elif direction == 2: #up
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y))
    elif direction == 3: #down
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))
        
def check_position(centerx, centery):
    turns = [False, False, False, False]
    num1 = (SCREENHEIGHT - 50) // 32
    num2 = (SCREENWIDTH // 30)
    num3 = 15
    # check collisions based on center x and center y of player +/ buffer number
    if centerx // 30 < 29:
        if direction == 0:
            if level[centery // num1][(centerx - num3) // num2] < 3:
                turns[1] = True
        if direction == 1:
            if level[centery // num1][(centerx + num3) // num2] < 3:
                turns[0] = True
        if direction == 2:
            if level[(centery + num3) // num1][centerx // num2] < 3:
                turns[3] = True
        if direction == 3:
            if level[(centery - num3) // num1][centerx // num2] < 3:
                turns[2] = True

        if direction == 2 or direction == 3:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num3) // num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num3) // num1][centerx // num2] < 3:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level[centery // num1][(centerx - num2) // num2] < 3:
                    turns[1] = True
                if level[centery // num1][(centerx + num2) // num2] < 3:
                    turns[0] = True
        if direction == 0 or direction == 1:
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num1) // num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num1) // num1][centerx // num2] < 3:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level[centery // num1][(centerx - num3) // num2] < 3:
                    turns[1] = True
                if level[centery // num1][(centerx + num3) // num2] < 3:
                    turns[0] = True
    else:
        turns[0] = True
        turns[1] = True

    return turns

def move_player(play_x, play_y):
    
    # right, left, up, down
    if direction == 0 and valid_turns[0]:
        play_x += player_speed
    elif direction == 1 and valid_turns[1]:
        play_x -= player_speed
    if direction == 2 and valid_turns[2]:
        play_y -= player_speed
    elif direction == 3 and valid_turns[3]:
        play_y += player_speed
    return play_x, play_y

    
    


#game running and functions collection

run = True

while run:
    timer.tick(fps)
    if counter < 19:
        counter += 1
        if counter > 3:
             flicker = False
    else:
        counter = 0
        flicker = True
    
    screen.fill("black")
    
    draw_board()
    center_x = player_x + 23
    center_y = player_y + 24
    draw_player()
    
    
    valid_turns = check_position(center_x, center_y)
    
    player_x, player_y = move_player(player_x, player_y)
        
    score = check_collisions(score)
    
    for event in pygame.event.get():
        #red X key
        if event.type == pygame.QUIT:
            run = False 
        #pressed keys for the directions 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3
           #if i was trying to go this way originally and no longer need = override with direction_command     
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = direction
        
        
    if direction_command == 0 and valid_turns[0]:
        direction = 0
    elif direction_command == 1 and valid_turns[1]:
        direction = 1
    elif direction_command == 2 and valid_turns[2]:
        direction = 2
    elif direction_command == 3 and valid_turns[3]:
                direction = 3
                
    if player_x > 900:
            player_x = -47
    elif player_x < -50:
            player_x = 897
            
            
        
    pygame.display.flip()

pygame.quit()
#  __________________________________________________________________
 
 