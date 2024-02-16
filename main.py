import pygame
import button

pygame.init()

SCREEN_WIDTH = 1150
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Madu")

pygame_icon = pygame.image.load("./assets/images/freeze.png")
pygame.display.set_icon(pygame_icon)


#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
play_img = pygame.image.load("./assets/images/button_play.png")
play_img = pygame.transform.scale(play_img, (250,60))

level_img = pygame.image.load("./assets/images/button_level.png")
level_img = pygame.transform.scale(level_img, (250,60))

shop_img = pygame.image.load("./assets/images/button_shop.png")
shop_img = pygame.transform.scale(shop_img, (250,60))

quit_img = pygame.image.load("./assets/images/button_quit.png")
quit_img = pygame.transform.scale(quit_img, (250,60))
video_img = pygame.image.load('./assets/images/button_video.png').convert_alpha()
audio_img = pygame.image.load('./assets/images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('./assets/images/button_keys.png').convert_alpha()
back_img = pygame.image.load('./assets/images/button_back.png').convert_alpha()

#create button instances
# play_button = button.Button(300, 150, play_img, 1)
# shop_button = button.Button(300, 250, shop_img, 1)
# quit_button = button.Button(300, 350, quit_img, 1)
# video_button = button.Button(226, 75, video_img, 1)
# audio_button = button.Button(225, 200, audio_img, 1)
# keys_button = button.Button(246, 325, keys_img, 1)
# back_button = button.Button(332, 450, back_img, 1)

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))
shopBackgroundImage = pygame.image.load("./assets/images/shop_background.png")
shopBackgroundImage = pygame.transform.scale(shopBackgroundImage, (1150,600))

menuBackgroundImage = pygame.image.load("./assets/images/menu_background.png")
menuBackgroundImage = pygame.transform.scale(menuBackgroundImage, (1150,600))

battleFieldBackgroundImage = pygame.image.load("./assets/images/BattleField_background.png")
battleFieldBackgroundImage = pygame.transform.scale(battleFieldBackgroundImage, (1150,530))

levelBackgroundImage = pygame.image.load("./assets/images/level_background.png")
levelBackgroundImage = pygame.transform.scale(levelBackgroundImage, (1150,530))


levelEasyButtonImage = pygame.image.load("./assets/images/easyLevel.png")
levelEasyButtonImage = pygame.transform.scale(levelEasyButtonImage, (250,70))

levelMedButtonImage = pygame.image.load("./assets/images/medLevel.png")
levelMedButtonImage = pygame.transform.scale(levelMedButtonImage, (250,70))

levelHardButtonImage = pygame.image.load("./assets/images/hardLevel.png")
levelHardButtonImage = pygame.transform.scale(levelHardButtonImage, (250,70))




fireBallAttackButtonImage = pygame.image.load("./assets/images/FireBall.png")
fireBallAttackButtonImage = pygame.transform.scale(fireBallAttackButtonImage, (250,70))

WaterVortexAttackButtonImage = pygame.image.load("./assets/images/WaterVortex.png")
WaterVortexAttackButtonImage = pygame.transform.scale(WaterVortexAttackButtonImage, (250,70))


stoneBulletsAttackButtonImage = pygame.image.load("./assets/images/StoneBullet.png")
stoneBulletsAttackButtonImage = pygame.transform.scale(stoneBulletsAttackButtonImage, (250,70))


windyStormAttackButtonImage = pygame.image.load("./assets/images/WindyStorm.png")
windyStormAttackButtonImage = pygame.transform.scale(windyStormAttackButtonImage, (250,70))





def fireBall():
  print("fireball")
def waterVortex():
  print("waterVortex")
def stoneBullet():
  print("stonebullet")
def windyStorm():
  print("windyStorm")



# FireBallButton = button.Button(0, 530, fireBallAttackButtonImage, 1)
# WaterVortexButton = button.Button(0, 530, WaterVortexAttackButtonImage, 1)
# StoneBulletsButton = button.Button(0, 530, stoneBulletsAttackButtonImage, 1)
# WindyStormButton = button.Button(0, 530, windyStormAttackButtonImage, 1)

game_state = "menu"
game_level = 0

#game loop
run = True
while run:
  

  #check if game is paused
  # menu_state = "options"
  # create a surface object, image is drawn on it.

  # Using blit to copy content from one surface to other
  # screen.blit(image, DEFAULT_IMAGE_POSITION)

  if game_state == "menu":
    screen.blit(menuBackgroundImage, (0, 0))
    screen.blit(play_img, (300, 100))
    screen.blit(level_img, (300, 200))
    screen.blit(shop_img, (300, 300))
    screen.blit(quit_img, (300, 400))
    
    
    # check menu state
    # if menu_state == "main":
    #   #draw pause screen buttons
    #   if play_button.draw(screen):
    #     game_paused = False
    #   elif shop_button.draw(screen):
    #     menu_state = "options"
    #   elif quit_button.draw(screen):
    #     run = False
    # #check if the options menu is open
    # elif menu_state == "options":
    #   #draw the different options buttons
    #   screen.blit(shopBackgroundImage, (0, 0))
    #   if video_button.draw(screen):
    #     print("Video Settings")
    #   elif audio_button.draw(screen):
    #     print("Audio Settings")
    #   elif keys_button.draw(screen):
    #     print("Change Key Bindings")
    #   elif back_button.draw(screen):
    #     menu_state = "main"
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        x,y=pygame.mouse.get_pos()  
        print(x,y)
        if (x>300 and x<550):
          
          if( y>100 and y<160):
            game_state = "game"
          elif( y>200 and y<260):
            game_state = "level"
          elif( y>300 and y<360):
            game_state = "shop"
          elif( y>300 and y<460):
            run = False
    screenReady = False    
  elif game_state == "game":

    screen.blit(battleFieldBackgroundImage, (0, 0))
    screen.blit(fireBallAttackButtonImage, (0, 530))
    screen.blit(WaterVortexAttackButtonImage, (300, 530))
    screen.blit(stoneBulletsAttackButtonImage, (600, 530))
    screen.blit(windyStormAttackButtonImage, (900,530))
    screenReady = True
    


  #event handler
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          game_state = "menu"
      elif event.type == pygame.QUIT:
        run = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        x,y=pygame.mouse.get_pos()
        if y > 530:
          if x < 250:
            fireBall()
          elif (x > 300 and x < 550):  
            waterVortex()
          elif (x > 600 and x < 850):
            stoneBullet()
          elif (x > 900):
            windyStorm() 
        else:
          pass
  elif game_state == "level":
    screen.blit(levelBackgroundImage, (0, 0))
    screen.blit(levelEasyButtonImage, (160, 100))
    screen.blit(levelMedButtonImage, (160, 200))
    screen.blit(levelHardButtonImage, (160, 300))
    
    
    
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          game_state = "menu"
      elif event.type == pygame.QUIT:
        run = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        x,y=pygame.mouse.get_pos()
        print(x,y)
        if (x > 160 and x < 400):
          if(y > 100 and y < 160):
            game_level = 0
          elif (y > 200 and y < 260):
            game_level = 1
          elif (y > 300 and y < 360):
            game_level = 2    
    print(game_level)    
  elif game_state == "shop":
    screen.blit(shopBackgroundImage, (0, 0)) 
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          game_state = "menu"
      elif event.type == pygame.QUIT:
        run = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        x,y=pygame.mouse.get_pos()
        print(x,y)     
  pygame.display.update()

pygame.quit()