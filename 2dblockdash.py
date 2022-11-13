import pygame
import sys
import random

count=0
number=10
pygame.init()#intializes the game

width=800#dimension of screen
height=600

plr_color=[90,90,255]#player features
plr_size=50
plr_pos=[width/2,height-2*plr_size]
plr_speedx=20
screen=pygame.display.set_mode((width,height))

background_colour=(0,0,0)
    
#enemy
enemy_size=50
enemy_pos=[random.randint(0,800-enemy_size),100]
enemy_color=[255,90,90]
enemy_speed=15

enemy_list=[]

game_over=False
color=enemy_color
def detect_collision(plr_pos,enemy_pos):
    p_x=plr_pos[0]
    p_y=plr_pos[1]

    e_x=enemy_pos[0]
    e_y=enemy_pos[1]

    if (e_x>=p_x and e_x<(p_x+plr_size))or (p_x>=e_x and p_x <(e_x+enemy_size)):
        if (e_y>=p_y and e_y<(p_y+plr_size)) or (p_y>=e_y and p_y<(e_y+enemy_size)):
            return True
    return False
def detect_collision123(plr_pos,i):
    p_x=plr_pos[0]
    p_y=plr_pos[1]

    e_x=i[0]
    e_y=i[1]

    if (e_x>=p_x and e_x<(p_x+plr_size))or (p_x>=e_x and p_x <(e_x+enemy_size)):
        if (e_y>=p_y and e_y<(p_y+plr_size)) or (p_y>=e_y and p_y<(e_y+enemy_size)):
            return True
    return False


while not game_over:
    for event in pygame.event.get():
        print(event)
        if count%12==0:
            number+=1
        if len(enemy_list)<number:
            var=[random.randint(0,800-enemy_size),0]
            enemy_list.append(var)
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT and plr_pos[0]!=0:
                plr_pos[0]-=plr_speedx
            if event.key==pygame.K_RIGHT and plr_pos[0]<745:
                plr_pos[0]+=plr_speedx
                if plr_pos[0]>745:
                    plr_pos[0]=745
    screen.fill(background_colour)
    if enemy_pos[1]<height and enemy_pos[1]>=0:
        enemy_pos[1]+=enemy_speed
    else:
        enemy_pos[1]=0
        enemy_pos[0]=random.randint(0,width-enemy_size)
        count+=1
    if detect_collision(plr_pos,enemy_pos):
        plr_color[0]+=5
        plr_color[1]+=5
        if plr_color[0]>240:
            game_over=False
    
    
    for i in enemy_list:
        color=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
        pygame.draw.rect(screen,color,(i[0],i[1],enemy_size,enemy_size))
        if detect_collision123(plr_pos,i):
            if plr_color[0]<75:
                game_over=True
                print(enemy_list)
                break
            else:
                plr_color[0]-=2
                plr_color[1]-=2
        if i[1]<height and i[1]>=0:
            i[1]+=enemy_speed
        else:
            enemy_list.remove(i)
         
    pygame.draw.rect(screen,plr_color,(plr_pos[0],plr_pos[1],plr_size,plr_size))
    pygame.draw.rect(screen,enemy_color,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))
    pygame.display.update()
    print(plr_pos[0])
print("score:",number*123)
