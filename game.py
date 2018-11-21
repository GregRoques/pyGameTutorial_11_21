# 1. Include Pygame
import pygame
from Hero import Hero
from badGuy import BadGuy

# 2. Initialize Pygame
pygame.init()

# 3. Make a screen with a size. The size MUST be a tuple
screen_size = (512, 480)
pygame_screen = pygame.display.set_mode(screen_size)

theHero= Hero()
theBadGuy = BadGuy()

#set the title of the window that opens...
pygame.display.set_caption("Hawkeye")

# ======VARIABLE FOR OUR GAME=========

background_image = pygame.image.load("background.png")
hero_image = pygame.image.load("hero.png")
goblin_image = pygame.image.load("goblin.png")
monster_image = pygame.image.load("monster.png")
arrow_image = pygame.image.load("arrow.png")


# ======MAIN GAME LOOP=========

game_on = True

# the loop will run as long as our bool is true
while game_on:
    # we are in the game loop from here on out!
    # 5. Listen for events and quite if the user clicks the x

    #=============EVENT CHECKER===================
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # The user clicked the red dot!
            game_on = False
        elif event.type == pygame.KEYDOWN:
            # The user pressed a key
            print (event.key)    
            if event.key == 275:
                theHero.shouldMove("right")
            elif event.key == 276:
                theHero.shouldMove("left")
            if event.key == 274:
                theHero.shouldMove("up")        
            elif event.key == 273:
                theHero.shouldMove("down")     

        elif event.type == pygame.KEYUP:
            # The user pressed a key
            print (event.key)    
            if event.key == 275:
                theHero.shouldMove("right",False)
            elif event.key == 276:
                theHero.shouldMove("left",False)
            if event.key == 274:
                theHero.shouldMove("up",False)        
            elif event.key == 273:
                theHero.shouldMove("down",False)           

    #=============DRAW STUFF=================== 
    
    # We use blit to draw on the screen. blit - block image transfer
    # blit is a method, and takes 2 args:
    #   1. What to draw
    #   2. Where to draw it           
    
    # in the docs... SURFACE = our "pygame_screen"
    pygame_screen.blit(background_image,[0,0])
    theHero.draw_me()
    theBadGuy.update_me(theHero)
    pygame_screen.blit(hero_image,[theHero.x, theHero.y])
    pygame_screen.blit(monster_image,[theBadGuy.x, theBadGuy.y])
    pygame.display.flip()
    
