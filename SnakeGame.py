import pygame
import time
import random

pygame.init()
pygame.mixer.init()

white =(255,255,255)
red =(255,0,0)
black =(0,0,0)
green =(0,145,0)
purple =(139,0,139)

game_width =800
game_height = 600
gameDisplay =pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption('snakes')

snakeimg = pygame.image.load('snake2.png')
direction ="right"
appleimg =pygame.image.load('apple_2.png')
appleimg =pygame.transform.scale(appleimg,(30,30))
green_apple = pygame.image.load('GreenApple(PikminComet).png')
green_apple = pygame.transform.scale(green_apple, (30, 30))
orangeimg = pygame.image.load('orange.png')
orangeimg = pygame.transform.scale(orangeimg, (30, 30))
background = pygame.image.load(("background.png")).convert()
background_rect = background.get_rect()
background =pygame.transform.scale(background,(game_width,game_height))
Game_Overscreen = pygame.image.load(("ENding.png")).convert()
Game_Overscreen_rect = Game_Overscreen.get_rect()
Game_Overscreen = pygame.transform.scale(Game_Overscreen, (game_width, game_height))
Pause_screen = pygame.image.load(("Paused.png")).convert()
Pause_screen__rect = Pause_screen.get_rect()
Pause_screen = pygame.transform.scale(Pause_screen, (game_width, game_height))
Gameintro_screen = pygame.image.load(("Starting.png")).convert()
Gameintro_screen_rect = Gameintro_screen.get_rect()
Gameintro_screen = pygame.transform.scale(Gameintro_screen, (game_width, game_height))

clock =pygame.time.Clock()
block_size =20
fps =15

smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("comicsansms",80)

pygame.mixer.music.load("Boogie_Woogie_Bed.wav")
eating_sound = pygame.mixer.Sound("eating.wav")
hit_sound = pygame.mixer.Sound("hit.wav")
hit_soundb = pygame.mixer.Sound("hit2.wav")

def text_object(text,color,size):
    if size =="small":
        textSurface =smallfont.render(text,True,color)
    if size =="medium":
        textSurface =medfont.render(text,True,color)
    if size =="large":
        textSurface =largefont.render(text,True,color)

    return textSurface ,textSurface.get_rect()

def message_to_screen(msg,color,y_displace =0,size ="small"):
    textsurf,textRect =text_object(msg,color,size)
    textRect.center = (game_width/2),(game_height/2)+y_displace
    gameDisplay.blit(textsurf,textRect)

def Score(Score):
    text =smallfont.render("Score: "+str(Score),True,white)
    gameDisplay.blit(text,[0,0])

def Pause():
    Paused =True
    while Paused:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type ==pygame.KEYDOWN:
                if event.key ==pygame.K_c:
                    Paused =False
                elif event.key ==pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.blit(Pause_screen, Pause_screen__rect)
        pygame.display.update()
        clock.tick(15)


def snake(snakelist,block_size):

    if direction =="right":
        head =pygame.transform.rotate(snakeimg,270)
    if direction =="left":
        head =pygame.transform.rotate(snakeimg,90)
    if direction =="up":
        head =snakeimg
    if direction =="down":
        head =pygame.transform.rotate(snakeimg,180)
    
    gameDisplay.blit(head,(snakelist[-1][0],snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green,[XnY[0],XnY[1],block_size,block_size])

def game_intro():
    pygame.mixer.music.play(-1)
    intro =True
    while intro:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type ==pygame.KEYDOWN:
                if event.key ==pygame.K_c:
                    intro =False
                if event.key ==pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.blit(Gameintro_screen, Gameintro_screen_rect)
        pygame.display.update()
        clock.tick(15)


    

def gameLoop():
    pygame.mixer.music.pause()
    Sound =True
    global direction
    direction ="right"
    gameExit = False
    gameOver = False
    lead_x =game_width/2
    lead_y =game_height/2
    Applesize = 30
    Orangesize = 30
    dt =0
    timer = 5
    timer2 = 5
    Scoring =0

    lead_x_change =10
    lead_y_change= 0
    snakeList =[]
    snakeLength =1

    randOrangeX = round(random.randrange(0, game_width-Orangesize))  # /10.0)*10.0
    randOrangeY = round(random.randrange(0, game_height-Orangesize))
    randgreen_AppleX = round(random.randrange(0, game_width-Orangesize))  # /10.0)*10.0
    randgreen_AppleY = round(random.randrange(0, game_height-Orangesize))
    randAppleX = round(random.randrange(0,game_width-Applesize))#/10.0)*10.0
    randAppleY = round(random.randrange(0,game_height-Applesize))#/10.0)*10.0
    
    while not gameExit:

        while gameOver ==True:
        
            while Sound:
                pygame.mixer.Sound.play(hit_sound)
                Sound = False
            gameDisplay.blit(Game_Overscreen, Game_Overscreen_rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    gameExit =True
                    gameOver =False
                if event.type ==pygame.KEYDOWN:
                    if event.key ==pygame.K_q:
                        gameExit =True
                        gameOver =False
                    if event.key ==pygame.K_c:
                        gameLoop()



        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                gameExit =True
            if event.type ==pygame.KEYDOWN:
                if direction =="right":
                    if event.key == pygame.K_UP:
                        direction = "up"
                        lead_y_change = -block_size
                        lead_x_change = 0
                    elif event.key == pygame.K_DOWN:
                        direction = "down"
                        lead_y_change = block_size
                        lead_x_change = 0
                elif direction =="left":
                    if event.key == pygame.K_UP:
                        direction = "up"
                        lead_y_change = -block_size
                        lead_x_change = 0
                    elif event.key == pygame.K_DOWN:
                        direction = "down"
                        lead_y_change = block_size
                        lead_x_change = 0
                elif direction =="up":
                    if event.key == pygame.K_LEFT:
                        direction = "left"
                        lead_x_change = -block_size
                        lead_y_change = 0
                    elif event.key ==pygame.K_RIGHT:
                        direction = "right"
                        lead_x_change =block_size
                        lead_y_change =0
                elif direction == "down":
                    if event.key == pygame.K_LEFT:
                        direction = "left"
                        lead_x_change = -block_size
                        lead_y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        direction = "right"
                        lead_x_change = block_size
                        lead_y_change = 0
                if event.key == pygame.K_p:
                    Pause()
        if lead_y >=game_height or lead_y<0:
            gameOver =True
        elif lead_x >= game_width:
            pygame.mixer.Sound.play(hit_soundb)
            direction ="up"
            lead_x = game_width-block_size
            lead_y_change = -block_size
            lead_x_change = 0
            
        elif lead_x < 0:
            pygame.mixer.Sound.play(hit_soundb)
            direction ="down"
            lead_x = 0
            lead_y_change = block_size
            lead_x_change = 0

        lead_x +=lead_x_change
        lead_y +=lead_y_change
        
        timer -=dt
        timer2 -=dt
        gameDisplay.blit(background, background_rect)
        gameDisplay.blit(appleimg,(randAppleX,randAppleY))
        gameDisplay.blit(orangeimg, (randOrangeX, randOrangeY))
        gameDisplay.blit(green_apple, (randgreen_AppleX, randgreen_AppleY))
        if timer <= 0:
            randOrangeX = round(random.randrange( 0, game_width-Orangesize))  # /10.0)*10.0
            randOrangeY = round(random.randrange(  0, game_height-Orangesize))
            timer =10

        if timer2 <= 0:
            randgreen_AppleX = round(random.randrange(0, game_width-Orangesize))  # /10.0)*10.0
            randgreen_AppleY = round(random.randrange(0, game_height-Orangesize))
            timer2 = 10
        snakeHead =[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList)>snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment ==snakeHead:
                gameOver = True

        snake(snakeList,block_size)
        Score(Scoring)
        pygame.display.update()

        
        if (lead_x >randAppleX and lead_x <randAppleX + Applesize) or (lead_x +block_size >randAppleX and lead_x +block_size < randAppleX + Applesize):
            if (lead_y >randAppleY and lead_y <randAppleY + Applesize) or (lead_y +block_size >randAppleY and lead_y +block_size<randAppleY +Applesize):
                snakeLength +=1
                Scoring +=1
                pygame.mixer.Sound.play(eating_sound)
                randAppleX = round(random.randrange(0,game_width-Applesize))#/10.0)*10.0
                randAppleY = round(random.randrange(0,game_height-Applesize))#/10.0)*10.0   

        if (lead_x > randOrangeX and lead_x < randOrangeX + Applesize) or (lead_x + block_size > randOrangeX and lead_x + block_size < randOrangeX + Applesize):
                if (lead_y > randOrangeY and lead_y < randOrangeY + Applesize) or (lead_y + block_size > randOrangeY and lead_y + block_size < randOrangeY + Applesize):
                    pygame.mixer.Sound.play(eating_sound)
                    Scoring +=2
                    randOrangeX =game_width +50
                    randOrangeY = game_height +10

        if (lead_x > randgreen_AppleX and lead_x < randgreen_AppleX + Applesize) or (lead_x + block_size > randgreen_AppleX and lead_x + block_size < randgreen_AppleX + Applesize):
                if (lead_y > randgreen_AppleY and lead_y < randgreen_AppleY + Applesize) or (lead_y + block_size > randgreen_AppleY and lead_y + block_size < randgreen_AppleY + Applesize):
                    pygame.mixer.Sound.play(eating_sound)
                    Scoring += 5
                    randgreen_AppleX = game_width + 200
                    randgreen_AppleX = game_height + 200
                    
        clock.tick(fps)
        dt = clock.tick(fps) / 1000
    pygame.quit()
    quit()

game_intro()
gameLoop()
