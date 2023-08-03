            
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
for i in range(1,3):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/{i}.png'), (45, 45)))
player_x = 450
player_y = 663

direction = 0
counter = 0
flicker = False

valid_turns = [False, False, False, False] # can I go right/left/up/down now?


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
        
def check_position(centerX, centerY):
    turns = [False, False, False, False] 
    
    num1 = ((SCREENHEIGHT - 50) // 32)
    num2 = (SCREENWIDTH // 30)
    num3 = 15
    #check colliding based on XY of player + Num so not to enter the wall
    if centerX // 30 < 29:
        if direction == 0:
            if level[centerX // num1][(centerY - num3) // num2 ] < 3:
              turns[1] = True  
        if direction == 1:
        
        if direction == 2:
            
        if direction == 3:
    else:
        turns[0] = True
        turns[1] = True
        
    return turns  


#game running and functions collection

run = True

while run:
    timer.tick(fps)
    if counter < 19:
        counter += 1
        if counter > 5:
             flicker = False
    else:
        counter = 0
        flicker = True
    
    screen.fill("black")
    
    draw_board()
    draw_player()
    
    center_x = player_x + 23
    center_y = player_y + 24
    valid_turns = check_position(center_x, center_y)
    
    
   
    
    
    for event in pygame.event.get():
        #red X key
        if event.type == pygame.QUIT:
            run = False 
        #pressed keys for the directions 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = 0
            if event.key == pygame.K_LEFT:
                direction = 1
            if event.key == pygame.K_UP:
                direction = 2
            if event.key == pygame.K_DOWN:
                direction = 3
                
            
        
    pygame.display.flip()

pygame.quit()
            