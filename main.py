import pygame
from pygame.sprite import AbstractGroup
import time



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

clock = pygame.time.Clock()

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
levelBackgroundImage = pygame.transform.scale(levelBackgroundImage, (1150,600))


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



class WaterVortexAttack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites = []
    self.is_animating = False
    # WaterVortexImage1 = pygame.image.load("./assets/images/waterVortexAttack/final/1.png")
    WaterVortexImage0 = pygame.image.load("./assets/images/invisible.png")
    self.sprites.append(WaterVortexImage0)
    WaterVortexImage1 = pygame.transform.scale(pygame.image.load("./assets/images/waterVortex/1-removebg-preview.png"), (160,350))
    self.sprites.append(WaterVortexImage1)
    WaterVortexImage2 = pygame.transform.scale(pygame.image.load("./assets/images/waterVortex/2-removebg-preview.png"), (160,350))
    self.sprites.append(WaterVortexImage2)
    WaterVortexImage3 = pygame.transform.scale(pygame.image.load("./assets/images/waterVortex/3-removebg-preview.png"), (160,350))
    self.sprites.append(WaterVortexImage3)
    WaterVortexImage4 = pygame.transform.scale(pygame.image.load("./assets/images/waterVortex/4-removebg-preview.png"), (160,350))
    self.sprites.append(WaterVortexImage4)
    WaterVortexImage5 = pygame.transform.scale(pygame.image.load("./assets/images/waterVortex/5-removebg-preview.png"), (160,350))
    self.sprites.append(WaterVortexImage5)
    WaterVortexImage6 = pygame.transform.scale(pygame.image.load("./assets/images/waterVortex/6-removebg-preview.png"), (160,350))
    self.sprites.append(WaterVortexImage6)
    WaterVortexImage7 = pygame.transform.scale(pygame.image.load("./assets/images/waterVortex/7-removebg-preview.png"), (160,350))
    self.sprites.append(WaterVortexImage7)

    self.currentSprit = 0
    self.image = self.sprites[self.currentSprit]
    
    self.rect = self.image.get_rect()
    self.rect.topleft = [posX,posY]
    print(self.rect,self.rect.topleft)
    
    
    
  def update(self):
    if self.is_animating == True:
      self.currentSprit += 0.4
      self.rect.x += 8
        
      if(int(self.currentSprit) == 0):
        self.currentSprit = 1
      print(self.rect.x)
      if self.currentSprit >= len(self.sprites):
        self.currentSprit = 1
      if self.rect.x > 800:
        self.is_animating = False
        self.currentSprit = 0
        self.rect.x = 100
      self.image = self.sprites[int(self.currentSprit)]  
      print(self.currentSprit)
      
  def animate(self):
    self.is_animating = True 
    print("called") 
    # self.update()
  
  
  
  
  
  
  
  
  
class FireBallAttack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites = []
    self.is_animating = False
    self.is_waiting = 45
    # FireBallImage1 = pygame.image.load("./assets/images/FireBallAttack/final/1.png")
    FireBallImage0 = pygame.image.load("./assets/images/invisible.png")
    self.sprites.append(FireBallImage0)
    FireBallImage1 = pygame.transform.scale(pygame.image.load("./assets/images/fireball/fireball/1.png"), (250,125))
    self.sprites.append(FireBallImage1)
    FireBallImage2 = pygame.transform.scale(pygame.image.load("./assets/images/fireball/fireball/2.png"), (250,125))
    self.sprites.append(FireBallImage2)
    FireBallImage3 = pygame.transform.scale(pygame.image.load("./assets/images/fireball/fireball/3.png"), (250,125))
    self.sprites.append(FireBallImage3)
    FireBallImage4 = pygame.transform.scale(pygame.image.load("./assets/images/fireball/fireball/4.png"), (250,125))
    self.sprites.append(FireBallImage4)
    FireBallImage5 = pygame.transform.scale(pygame.image.load("./assets/images/fireball/fireball/5.png"), (250,125))
    self.sprites.append(FireBallImage5)
    FireBallImage6 = pygame.transform.scale(pygame.image.load("./assets/images/fireball/fireball/6.png"), (250,125))
    self.sprites.append(FireBallImage6)
    self.currentSprit = 0
    self.image = self.sprites[self.currentSprit]
    
    self.rect = self.image.get_rect()
    self.rect.topleft = [posX,posY]
    print(self.rect,self.rect.topleft)
    
    
    
  def update(self):
    if self.is_animating == True:
      if self.is_waiting == 0:
        self.currentSprit += 0.4
        self.rect.x += 8

        if(int(self.currentSprit) == 0):
          self.currentSprit = 1
        if self.currentSprit >= len(self.sprites):
          self.currentSprit = 1
        if self.rect.x > 800:
          self.is_animating = False
          self.currentSprit = 0
          self.rect.x = 200
          self.is_waiting = 45
        self.image = self.sprites[int(self.currentSprit)]  
      else:
        self.is_waiting -= 1  
      
  def animate(self):
    self.is_animating = True 
    print("called") 
  
  
  
  








class WindyStormAttack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites = []
    self.is_animating = False
    # WindyStormImage1 = pygame.image.load("./assets/images/WindyStormAttack/final/1.png")
    WindyStormImage0 = pygame.image.load("./assets/images/invisible.png")
    self.sprites.append(WindyStormImage0)
    WindyStormImage1 = pygame.transform.scale(pygame.image.load("./assets/images/windystorm/windy storm/1.png"),(450,250))
    self.sprites.append(WindyStormImage1)
    WindyStormImage2 = pygame.transform.scale(pygame.image.load("./assets/images/windystorm/windy storm/2.png"),(450,250))
    self.sprites.append(WindyStormImage2)
    WindyStormImage3 = pygame.transform.scale(pygame.image.load("./assets/images/windystorm/windy storm/3.png"),(450,250))
    self.sprites.append(WindyStormImage3)
    WindyStormImage4 = pygame.transform.scale(pygame.image.load("./assets/images/windystorm/windy storm/4.png"),(450,250))
    self.sprites.append(WindyStormImage4)
    WindyStormImage5 = pygame.transform.scale(pygame.image.load("./assets/images/windystorm/windy storm/5.png"),(450,250))
    self.sprites.append(WindyStormImage5)
    WindyStormImage6 = pygame.transform.scale(pygame.image.load("./assets/images/windystorm/windy storm/6.png"),(450,250))
    self.sprites.append(WindyStormImage6)
    WindyStormImage7 = pygame.transform.scale(pygame.image.load("./assets/images/windystorm/windy storm/7.png"),(450,250))
    self.sprites.append(WindyStormImage7)
    WindyStormImage8 = pygame.transform.scale(pygame.image.load("./assets/images/windystorm/windy storm/8.png"),(450,250))
    self.sprites.append(WindyStormImage8)
    WindyStormImage9 = pygame.transform.scale(pygame.image.load("./assets/images/windystorm/windy storm/9.png"),(450,250))
    self.sprites.append(WindyStormImage9)
    WindyStormImage10 = pygame.transform.scale(pygame.image.load("./assets/images/windystorm/windy storm/10.png"),(450,250))
    self.sprites.append(WindyStormImage10)
    WindyStormImage11 = pygame.transform.scale(pygame.image.load("./assets/images/windystorm/windy storm/11.png"),(450,250))
    self.sprites.append(WindyStormImage11)
    WindyStormImage12 = pygame.transform.scale(pygame.image.load("./assets/images/windystorm/windy storm/12.png"),(450,250))
    self.sprites.append(WindyStormImage12)
    self.currentSprit = 0
    self.image = self.sprites[self.currentSprit]

    
    self.rect = self.image.get_rect()
    self.rect.topleft = [posX,posY]
    print(self.rect,self.rect.topleft)
    
    
    
  def update(self):
    if self.is_animating == True:
      self.currentSprit += 0.4
      self.rect.x += 8
        
      if(int(self.currentSprit) == 0):
        self.currentSprit = 1
      if self.currentSprit >= len(self.sprites):
        self.currentSprit = 1
      if self.rect.x > 800:
        self.is_animating = False
        self.currentSprit = 0
        self.rect.x = 100
      self.image = self.sprites[int(self.currentSprit)]  
      
  def animate(self):
    self.is_animating = True 
    print("called")   
  
class OpponentFireBallAttack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites = []
    self.is_animating = False
    # OpponentFireBallImage1 = pygame.image.load("./assets/images/OpponentFireBallAttack/final/1.png")
    OpponentFireBallImage0 = pygame.image.load("./assets/images/invisible.png")
    self.sprites.append(OpponentFireBallImage0)
    OpponentFireBallImage1 = pygame.transform.scale(pygame.image.load("./assets/images/Opponentfireball/fireball/0.png"), (250,125))
    self.sprites.append(OpponentFireBallImage1)
    OpponentFireBallImage2 = pygame.transform.scale(pygame.image.load("./assets/images/Opponentfireball/fireball/1.png"), (250,125))
    self.sprites.append(OpponentFireBallImage2)
    OpponentFireBallImage3 = pygame.transform.scale(pygame.image.load("./assets/images/Opponentfireball/fireball/2.png"), (250,125))
    self.sprites.append(OpponentFireBallImage3)
    OpponentFireBallImage4 = pygame.transform.scale(pygame.image.load("./assets/images/Opponentfireball/fireball/3.png"), (250,125))
    self.sprites.append(OpponentFireBallImage4)
    OpponentFireBallImage5 = pygame.transform.scale(pygame.image.load("./assets/images/Opponentfireball/fireball/4.png"), (250,125))
    self.sprites.append(OpponentFireBallImage5)
    OpponentFireBallImage6 = pygame.transform.scale(pygame.image.load("./assets/images/Opponentfireball/fireball/5.png"), (250,125))
    self.sprites.append(OpponentFireBallImage6)
    self.currentSprit = 0
    self.image = self.sprites[self.currentSprit]
    
    self.rect = self.image.get_rect()
    self.rect.topleft = [posX,posY]
    print(self.rect,self.rect.topleft)
    
    
    
  def update(self):
    if self.is_animating == True:
      self.currentSprit += 0.4
      self.rect.x -= 8
        
      if(int(self.currentSprit) == 0):
        self.currentSprit = 1
      if self.currentSprit >= len(self.sprites):
        self.currentSprit = 1
      if self.rect.x < 150:
        self.is_animating = False
        self.currentSprit = 0
        self.rect.x = 800
      self.image = self.sprites[int(self.currentSprit)]  
      print(self.currentSprit)
      
  def animate(self):
    self.is_animating = True       
  
  
  
mainCharAnimating = False    

class MainCharMove1Attack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites = []
    self.is_animating = False
    # MainCharMove1Image1 = pygame.image.load("./assets/images/MainCharMove1Attack/final/1.png")
    MainCharMove2Image = pygame.image.load("./assets/images/invisible.png")
    self.sprites.append(MainCharMove2Image)
    MainCharMove1Image0 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/0.png"), (250,400))
    self.sprites.append(MainCharMove1Image0)
    MainCharMove1Image1 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/1.png"), (250,400))
    self.sprites.append(MainCharMove1Image1)
    MainCharMove1Image2 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/2.png"), (250,400))
    self.sprites.append(MainCharMove1Image2)
    MainCharMove1Image3 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/3.png"), (250,400))
    self.sprites.append(MainCharMove1Image3)
    MainCharMove1Image4 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/4.png"), (400,400))
    self.sprites.append(MainCharMove1Image4)
    MainCharMove1Image5 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/5.png"), (350,400))
    self.sprites.append(MainCharMove1Image5)
    MainCharMove1Image6 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/6.png"), (350,400))
    self.sprites.append(MainCharMove1Image6)
    MainCharMove1Image7 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/7.png"), (350,400))
    self.sprites.append(MainCharMove1Image7)
    self.currentSprit = 0
    self.image = self.sprites[self.currentSprit]
    
    self.rect = self.image.get_rect()
    self.rect.topleft = [posX,posY]
    print(self.rect,self.rect.topleft)
    
    
    
  def update(self):
    if self.is_animating == True:
      self.currentSprit += 0.1

      if self.currentSprit >= len(self.sprites):
        self.currentSprit = 0
        self.is_animating = False
        
      self.image = self.sprites[int(self.currentSprit)]  
    else:
      if mainCharAnimating == True:
        self.image = self.sprites[0]
      self.image = self.sprites[1]   
      
  def animate(self):
    self.is_animating = True 
    print("called") 
  
  
class MainCharMove2Attack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites1 = []
    self.sprites2 = []
    self.is_animating = False
    # MainCharMove2Image1 = pygame.image.load("./assets/images/MainCharMove2Attack/final/1.png")
    MainCharMove2Image = pygame.image.load("./assets/images/invisible.png")
    self.sprites2.append(MainCharMove2Image)
    MainCharMove2Image0 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move2/0.png"), (250,400))
    self.sprites2.append(MainCharMove2Image0)
    MainCharMove2Image1 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move2/1.png"), (250,400))
    self.sprites2.append(MainCharMove2Image1)
    MainCharMove2Image2 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move2/2.png"), (250,400))
    self.sprites2.append(MainCharMove2Image2)
    MainCharMove2Image3 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move2/3.png"), (250,400))
    self.sprites2.append(MainCharMove2Image3)
    MainCharMove2Image4 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move2/4.png"), (400,400))
    self.sprites2.append(MainCharMove2Image4)
    MainCharMove2Image5 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move2/5.png"), (350,400))
    self.sprites2.append(MainCharMove2Image5)
    MainCharMove2Image6 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move2/6.png"), (350,400))
    self.sprites2.append(MainCharMove2Image6)
    MainCharMove2Image7 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move2/7.png"), (350,400))
    self.sprites.append(MainCharMove2Image7)
    MainCharMove2Image8 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move2/8.png"), (350,400))
    self.sprites2.append(MainCharMove2Image8)
    MainCharMove2Image9 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move2/9.png"), (350,400))
    self.sprites2.append(MainCharMove2Image9)
    self.currentSprit = 0
    self.image = self.sprites[self.currentSprit]
    
    self.rect = self.image.get_rect()
    self.rect.topleft = [posX,posY]
    print(self.rect,self.rect.topleft)
    
    
    
  def update(self):
    if self.is_animating == True:
      self.currentSprit += 0.1

      if self.currentSprit >= len(self.sprites):
        self.currentSprit = 0
        self.is_animating = False
        
      self.image = self.sprites[int(self.currentSprit)]  
      mainCharAnimating = False
    # else:
    #   self.image = self.sprites[1]  
        
      
  def animate(self):
    mainCharAnimating = True
    self.is_animating = True 
    print("called")   
  
  
  
  
    
      
    

















def fireBall():
  print("fireball")
def opponentfireBall():
  print("opponentfireball")
  
def waterVortex():
  print("waterVortex")
  
    
def stoneBullet():
  print("stonebullet")
def windyStorm():
  print("windyStorm")
  
def mainCharMove1():
  print("mainCharMove1")
  
def mainCharMove2():
  print("mainCharMove2")



WaterVertex_sprites = pygame.sprite.Group()
waterVortexattack = WaterVortexAttack(200,100)
WaterVertex_sprites.add(waterVortexattack) 

fireBall_sprites = pygame.sprite.Group()
fireBallattack = FireBallAttack(200,200)
fireBall_sprites.add(fireBallattack) 

opponentFireBall_sprites = pygame.sprite.Group()
opponentFireBallattack = OpponentFireBallAttack(800,200)
opponentFireBall_sprites.add(opponentFireBallattack) 

windyStorm_sprites = pygame.sprite.Group()
windystormattack = WindyStormAttack(200,250)
windyStorm_sprites.add(windystormattack) 

mainCharMove1_sprites = pygame.sprite.Group()
mainCharMove1attack = MainCharMove1Attack(150,100)
mainCharMove1_sprites.add(mainCharMove1attack) 

mainCharMove2_sprites = pygame.sprite.Group()
mainCharMove2attack = MainCharMove2Attack(150,100)
mainCharMove2_sprites.add(mainCharMove2attack) 



# FireBallButton = button.Button(0, 530, fireBallAttackButtonImage, 1)
# WaterVortexButton = button.Button(0, 530, WaterVortexAttackButtonImage, 1)
# StoneBulletsButton = button.Button(0, 530, stoneBulletsAttackButtonImage, 1)
# WindyStormButton = button.Button(0, 530, windyStormAttackButtonImage, 1)

game_state = "menu"
game_level = 0
player_turn = True


#game loop
run = True

while run:
  

  #check if game is paused
  # menu_state = "options"
  # create a surface object, image is drawn on it.

  # Using blit to copy content from one surface to other
  # screen.blit(image, DEFAULT_IMAGE_POSITION)
  screenReady = True

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
    WaterVertex_sprites.draw(screen)
    WaterVertex_sprites.update()
    
    fireBall_sprites.draw(screen)
    fireBall_sprites.update()
    
    opponentFireBall_sprites.draw(screen)
    opponentFireBall_sprites.update()
    
    windyStorm_sprites.draw(screen)
    windyStorm_sprites.update()
    
    mainCharMove1_sprites.draw(screen)
    mainCharMove1_sprites.update()
    
    mainCharMove2_sprites.draw(screen)
    mainCharMove2_sprites.update()
    
    pygame.display.flip()
    clock.tick(80)


  #event handler
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          game_state = "menu"
      elif event.type == pygame.QUIT:
        run = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        x,y=pygame.mouse.get_pos()
        if y > 530 and player_turn:
          if x < 250:
            mainCharMove1()
            mainCharMove1attack.animate()
            fireBall()
            fireBallattack.animate()
            player_turn = False
          elif (x > 300 and x < 550):  
            mainCharMove2()
            mainCharMove2attack.animate()
            waterVortex()
            waterVortexattack.animate()
            
          elif (x > 600 and x < 850):
            stoneBullet()
          elif (x > 900):
            windyStorm() 
            windystormattack.animate()
        elif not player_turn:
          opponentfireBall()
          opponentFireBallattack.animate()
          player_turn = True
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
        if (x > 160 and x < 400):
          if(y > 100 and y < 160):
            game_level = 0
          elif (y > 200 and y < 260):
            game_level = 1
          elif (y > 300 and y < 360):
            game_level = 2    
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