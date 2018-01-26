import pygame
import time
import random

pygame.init()

white = (255,255,255)
gdyellow = (255,255,233)
black = (0,0,0)
red = (255,0,0)
green = (0,115,0)
display_width = 800
display_height = 600
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Zootopia")



clock = pygame.time.Clock()


FPS = 100

smallfont = pygame.font.SysFont("comicsansms",25)
largefont = pygame.font.SysFont("comicsansms",50)


def text_objects(text,color):
    textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen (msg, color, y_displace=0):
    textSurf, textRect = text_objects(msg,color)
    textRect.center = (display_width / 2), (display_height /2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def message_to_screen2 (msg,color):
    screen_text = smallfont.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2-238,display_height/2+120])

def message_to_screen3 (msg,color):
    screen_text = smallfont.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2-150,display_height/2+160])
    
def level_to_screen (msg,color):
    screen_text = smallfont.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width-120,display_height-50])

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        gameDisplay.fill(gdyellow)
        message_to_screen("Welcome to Zootopia!",green)
        message_to_screen2("Use UP,DOWN,LEFT,RIGHT to catch Nick.",red)
        message_to_screen3("Press C to play or Q to quit.",black)
        logo = pygame.image.load("logo.png")
        gameDisplay.blit(logo,(200,120))
        pygame.display.update()


def gameLoop():
    rab1 = pygame.image.load("1.png")
    rab2 = pygame.image.load("2.png")
    rab = rab1
    fox1 = pygame.image.load("fox1.png")
    fox2 = pygame.image.load("fox2.png")
    fox3 = pygame.image.load("fox3.png")
    fox4 = pygame.image.load("fox4.png")
    fox5 = pygame.image.load("fox5.png")
    list = [fox1,fox2,fox3,fox4,fox5]
    fox = fox1
    donut = pygame.image.load("donut.png")
    donnut = pygame.image.load("donut.png")
    gameExit = False
    gameOver = False
    levelup = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    block_size = 2
    speed = 2
    times = 0


    randFoxX = random.randrange(0,display_width-150)
    randFoxY = random.randrange(0,display_height-150)
    randDonX =random.randrange(-100,-50) 
    randDonY = random.randrange(0,display_height/2+150)
    randDonnX =random.randrange(700,1100) 
    randDonnY = random.randrange(0,display_height/2+150)
        
    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(gdyellow)
            message_to_screen("Game over, you got %s. " %(times),red, -50)
            message_to_screen("Press C to play again or Q to quit",black, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameOver = False
                        gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True            
            if event.type == pygame.KEYDOWN:
                if rab == rab1:
                    rab = rab2
                else:
                    rab = rab1

                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_SPACE:
                    lead_x_change = 0
                    lead_y_change = 0

        if lead_x >= display_width-55 or lead_x <= 0 or lead_y >= display_height-110 or lead_y <= 0:
                    gameOver = True
        if abs(lead_x-randDonX) < 65 and abs(lead_y-randDonY) < 70:
                    gameOver = True
        if abs(lead_x-randDonnX) < 65 and abs(lead_y-randDonnY) < 70:
                    gameOver = True



        lead_x += lead_x_change
        lead_y += lead_y_change
        randDonX += speed
        randDonY += randDonX/90
        randDonnX -= speed
        randDonnY += randDonX/90
        gameDisplay.fill(gdyellow)
        gameDisplay.blit(rab,(lead_x,lead_y))
        gameDisplay.blit(fox,(randFoxX,randFoxY))
        gameDisplay.blit(donut,(randDonX,randDonY))
        gameDisplay.blit(donnut,(randDonnX,randDonnY))
        level_to_screen("you got %s" %(times),red)

        if randDonX > display_width+500 or randDonY > display_height+500:
                    randDonX = random.randrange(-80,-10)
                    randDonY = random.randrange(0,display_height/2+150)
                    randDonnX =random.randrange(900,1100) 
                    randDonnY = random.randrange(0,display_height/2+150)


        
        pygame.display.update()

        if abs(lead_x - randFoxX) < 55 and lead_y - randFoxY < 80 and randFoxY - lead_y < 110:
                    randFoxX = random.randrange(0,display_width-150)
                    randFoxY = random.randrange(0,display_height-150)
                    while abs(randFoxX-lead_x)<100 and abs(randFoxY - lead_y)<100:
                        randFoxX = random.randrange(0,display_width-150)
                        randFoxY = random.randrange(0,display_height-150)
                    
                    fox = random.choice(list)
                    block_size += 0.2
                    speed += 0.1
                    times += 1
                    


        clock.tick(FPS)


    pygame.quit()
    quit()
    
game_intro()
gameLoop()
