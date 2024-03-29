import pygame

# initialize Pygame
pygame.init()
screen_width,screen_height=800,600
# create a window
window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite pixel by @Datevid")

clock = pygame.time.Clock()

# define the color of the background (black)
bg_color = (0, 0, 0)

# define the color of the pixel (red, green, blue)
spriteColor = (255, 125, 125)

# create object x y width height
spriteObj=pygame.Rect(0,0,30,30)
spriteObj.center=(screen_width/2,screen_height/2)

spriteSpeedX,spriteSpeedY=5,5

# Load the image of nave espacial or spaceship
shipSurface = pygame.image.load("player.png")
shipSurface=pygame.transform.scale(shipSurface,(50,50))
shipObj=shipSurface.get_rect()

#obstacule
obstaculeObj=pygame.Rect(400,200,100,100)

# Flag to track whether the left or right key is being pressed
left_key_pressed = False
right_key_pressed = False
top_key_pressed=False
bottom_key_pressed=False
# wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # chek for keypress events for spaceship
        elif event.type == pygame.KEYDOWN:
            # Handle key down events
            if event.key == pygame.K_LEFT:
                # Set the left key flag to True
                left_key_pressed = True
            elif event.key == pygame.K_RIGHT:
                # Set the right key flag to True
                right_key_pressed = True
            elif event.key == pygame.K_UP:
                top_key_pressed = True
            elif event.key == pygame.K_DOWN:
                bottom_key_pressed=True
        elif event.type == pygame.KEYUP:
            # Handle key up events
            if event.key == pygame.K_LEFT:
                # Set the left key flag to False
                left_key_pressed = False
            elif event.key == pygame.K_RIGHT:
                # Set the right key flag to False
                right_key_pressed = False
            elif event.key == pygame.K_UP:
                top_key_pressed = False
            elif event.key == pygame.K_DOWN:
                bottom_key_pressed=False

            
    # Move the sprite if a key is being pressed
    if left_key_pressed:
        shipObj.x -= 10
    elif right_key_pressed:
        shipObj.x += 10
    elif top_key_pressed:
        shipObj.y -= 10
    elif bottom_key_pressed:
        shipObj.y += 10

    spriteObj.x+=spriteSpeedX
    spriteObj.y+=spriteSpeedY
    if spriteObj.bottom-200 >=screen_height or spriteObj.top+200 <= 0:
        spriteSpeedY*=-1
    if spriteObj.right-200 >= screen_width or spriteObj.left+200 <=0:
        spriteSpeedX*=-1

    # fill the window with the background color
    window.fill(bg_color)

    pygame.draw.ellipse(window,spriteColor,spriteObj)
    # blit (copy) the surface onto the window
    #window.blit(spriteSurface, spriteObj)

    #draw obstacule
    pygame.draw.rect(window,(255,255,0),obstaculeObj,4)
    
    #draw the image to the screen:
    #window.blit(shipSurface,(100,100),shipObj)
    window.blit(shipSurface,shipObj)

    if shipObj.colliderect(obstaculeObj):
        pygame.draw.rect(window,(255,125,125),shipObj,4)

    if shipObj.colliderect(spriteObj):
        pygame.draw.rect(window,(255,125,125),shipObj,4)

    # update the window
    pygame.display.update()

    clock.tick(60)
