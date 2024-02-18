import pygame
from pygame.sprite import AbstractGroup
import random
from time import sleep
from pygame import mixer 


 
  
mixer.init() 
# pygame.mixer.Channel(0).play(pygame.mixer.Sound('./assets/audiofiles/game home.wav'))
# mixer.music.set_volume(0.7) 
  
# mixer.music.play() 


pygame.init()

SCREEN_WIDTH = 1150
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Madu")

pygame_icon = pygame.image.load("./assets/images/freeze.png")
pygame.display.set_icon(pygame_icon)


#define fonts
font = pygame.font.SysFont("arialblack", 24)

gameFont = pygame.font.SysFont("arialblack", 100)

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

upgrade_img = pygame.image.load("./assets/audiofiles/upgrade.png")
upgrade_img = pygame.transform.scale(upgrade_img, (250,60))

sword_img = pygame.image.load("./assets/audiofiles/sword.png")
sword_img = pygame.transform.scale(sword_img, (250,60))

armor_img = pygame.image.load("./assets/audiofiles/Armor.png")
armor_img = pygame.transform.scale(armor_img, (250,60))

quit_img = pygame.image.load("./assets/images/button_quit.png")
quit_img = pygame.transform.scale(quit_img, (250,60))
video_img = pygame.image.load('./assets/images/button_video.png').convert_alpha()
audio_img = pygame.image.load('./assets/images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('./assets/images/button_keys.png').convert_alpha()
back_img = pygame.image.load('./assets/images/button_back.png').convert_alpha()
youDied_img = pygame.image.load('./assets/images/YouDied.png')
Victory_img = pygame.image.load('./assets/images/Victory.png')

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
setupgrade = ""  
  
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
    self.is_waiting = 45
    
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
          self.rect.x = 400
          self.is_waiting = 45
        self.image = self.sprites[int(self.currentSprit)]  
      else:
        self.is_waiting -= 1 
      
  def animate(self):
    self.is_animating = True 
    print("called") 
    # self.update()
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('./assets/audiofiles/water ball exp.mp3'))
    
  
  
class OpponentWaterVortexAttack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites = []
    self.is_waiting = 45
    
    self.is_animating = False
    # OpponentWaterVortexImage1 = pygame.image.load("./assets/images/OpponentWaterVortexAttack/final/1.png")
    OpponentWaterVortexImage0 = pygame.image.load("./assets/images/invisible.png")
    self.sprites.append(OpponentWaterVortexImage0)
    OpponentWaterVortexImage1 = pygame.transform.scale(pygame.image.load("./assets/images/WaterVortex/1-removebg-preview.png"), (160,350))
    self.sprites.append(OpponentWaterVortexImage1)
    OpponentWaterVortexImage2 = pygame.transform.scale(pygame.image.load("./assets/images/WaterVortex/2-removebg-preview.png"), (160,350))
    self.sprites.append(OpponentWaterVortexImage2)
    OpponentWaterVortexImage3 = pygame.transform.scale(pygame.image.load("./assets/images/WaterVortex/3-removebg-preview.png"), (160,350))
    self.sprites.append(OpponentWaterVortexImage3)
    OpponentWaterVortexImage4 = pygame.transform.scale(pygame.image.load("./assets/images/WaterVortex/4-removebg-preview.png"), (160,350))
    self.sprites.append(OpponentWaterVortexImage4)
    OpponentWaterVortexImage5 = pygame.transform.scale(pygame.image.load("./assets/images/WaterVortex/5-removebg-preview.png"), (160,350))
    self.sprites.append(OpponentWaterVortexImage5)
    OpponentWaterVortexImage6 = pygame.transform.scale(pygame.image.load("./assets/images/WaterVortex/6-removebg-preview.png"), (160,350))
    self.sprites.append(OpponentWaterVortexImage6)
    OpponentWaterVortexImage7 = pygame.transform.scale(pygame.image.load("./assets/images/WaterVortex/7-removebg-preview.png"), (160,350))
    self.sprites.append(OpponentWaterVortexImage7)

    self.currentSprit = 0
    self.image = self.sprites[self.currentSprit]
    
    self.rect = self.image.get_rect()
    self.rect.topleft = [posX,posY]
    print(self.rect,self.rect.topleft)
    
    
    
  def update(self):
    if self.is_animating == True:
      if self.is_waiting == 0:
        self.currentSprit += 0.4
        self.rect.x -= 8

        if(int(self.currentSprit) == 0):
          self.currentSprit = 1
        if self.currentSprit >= len(self.sprites):
          self.currentSprit = 1
        if self.rect.x < 350:
          self.is_animating = False
          self.currentSprit = 0
          self.rect.x = 800
          self.is_waiting = 45
        self.image = self.sprites[int(self.currentSprit)]  
      else:
        self.is_waiting -= 1 
      
  def animate(self):
    self.is_animating = True 
    print("called") 
    # self.update()  
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('./assets/audiofiles/water ball exp.mp3'))
    
  
  
  
  
  
  
  
  
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
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('./assets/audiofiles/fireball.mp3'))
    self.is_animating = True 
  
  
  



class StoneBulletAttack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites = []
    self.is_animating = False
    self.is_waiting = 45
    # StoneBulletImage1 = pygame.image.load("./assets/images/StoneBulletAttack/final/1.png")
    StoneBulletImage0 = pygame.image.load("./assets/images/invisible.png")
    self.sprites.append(StoneBulletImage0)
    StoneBulletImage1 = pygame.transform.scale(pygame.image.load("./assets/images/rock/1.png"), (250,125))
    self.sprites.append(StoneBulletImage1)
    StoneBulletImage2 = pygame.transform.scale(pygame.image.load("./assets/images/rock/2.png"), (250,125))
    self.sprites.append(StoneBulletImage2)
    StoneBulletImage3 = pygame.transform.scale(pygame.image.load("./assets/images/rock/3.png"), (250,125))
    self.sprites.append(StoneBulletImage3)
    StoneBulletImage4 = pygame.transform.scale(pygame.image.load("./assets/images/rock/4.png"), (250,125))
    self.sprites.append(StoneBulletImage4)
    self.currentSprit = 0
    self.image = self.sprites[self.currentSprit]
    
    self.rect = self.image.get_rect()
    self.rect.topleft = [posX,posY]
    print(self.rect,self.rect.topleft)
    
    
    
  def update(self):
    if self.is_animating == True:
      if self.is_waiting == 0:
        self.currentSprit += 0.2
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
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('./assets/audiofiles/rock ball.mp3'))
    








class OpponentStoneBulletAttack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites = []
    self.is_animating = False
    self.is_waiting = 45
    # OpponentStoneBulletImage1 = pygame.image.load("./assets/images/OpponentStoneBulletAttack/final/1.png")
    OpponentStoneBulletImage0 = pygame.image.load("./assets/images/invisible.png")
    self.sprites.append(OpponentStoneBulletImage0)
    OpponentStoneBulletImage1 = pygame.transform.scale(pygame.image.load("./assets/images/rock/1.png"), (250,125))
    self.sprites.append(OpponentStoneBulletImage1)
    OpponentStoneBulletImage2 = pygame.transform.scale(pygame.image.load("./assets/images/rock/2.png"), (250,125))
    self.sprites.append(OpponentStoneBulletImage2)
    OpponentStoneBulletImage3 = pygame.transform.scale(pygame.image.load("./assets/images/rock/3.png"), (250,125))
    self.sprites.append(OpponentStoneBulletImage3)
    OpponentStoneBulletImage4 = pygame.transform.scale(pygame.image.load("./assets/images/rock/4.png"), (250,125))
    self.sprites.append(OpponentStoneBulletImage4)
    self.currentSprit = 0
    self.image = self.sprites[self.currentSprit]
    
    self.rect = self.image.get_rect()
    self.rect.topleft = [posX,posY]
    print(self.rect,self.rect.topleft)
    
    
    
  def update(self):
    if self.is_animating == True:
      if self.is_waiting == 0:
        self.currentSprit += 0.2
        self.rect.x -= 8

        if(int(self.currentSprit) == 0):
          self.currentSprit = 1
        if self.currentSprit >= len(self.sprites):
          self.currentSprit = 1
        if self.rect.x < 200:
          self.is_animating = False
          self.currentSprit = 0
          self.rect.x = 800
          self.is_waiting = 45
        self.image = self.sprites[int(self.currentSprit)]  
      else:
        self.is_waiting -= 1  
      
  def animate(self):
    self.is_animating = True 
    print("called") 
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('./assets/audiofiles/rock ball.mp3'))
    






class WindyStormAttack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites = []
    self.is_waiting = 45
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
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('./assets/audiofiles/wind 1.wav'))
      
    
    
    
class OpponentWindyStormAttack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites = []
    self.is_waiting = 45
    self.is_animating = False
    # OpponentWindyStormImage1 = pygame.image.load("./assets/images/OpponentWindyStormAttack/final/1.png")
    OpponentWindyStormImage0 = pygame.image.load("./assets/images/invisible.png")
    self.sprites.append(OpponentWindyStormImage0)
    OpponentWindyStormImage1 = pygame.transform.scale(pygame.image.load("./assets/images/OpponentWindyStorm/windy storm/1.png"),(450,250))
    self.sprites.append(OpponentWindyStormImage1)
    OpponentWindyStormImage2 = pygame.transform.scale(pygame.image.load("./assets/images/OpponentWindyStorm/windy storm/2.png"),(450,250))
    self.sprites.append(OpponentWindyStormImage2)
    OpponentWindyStormImage3 = pygame.transform.scale(pygame.image.load("./assets/images/OpponentWindyStorm/windy storm/3.png"),(450,250))
    self.sprites.append(OpponentWindyStormImage3)
    OpponentWindyStormImage4 = pygame.transform.scale(pygame.image.load("./assets/images/OpponentWindyStorm/windy storm/4.png"),(450,250))
    self.sprites.append(OpponentWindyStormImage4)
    OpponentWindyStormImage5 = pygame.transform.scale(pygame.image.load("./assets/images/OpponentWindyStorm/windy storm/5.png"),(450,250))
    self.sprites.append(OpponentWindyStormImage5)
    OpponentWindyStormImage6 = pygame.transform.scale(pygame.image.load("./assets/images/OpponentWindyStorm/windy storm/6.png"),(450,250))
    self.sprites.append(OpponentWindyStormImage6)
    OpponentWindyStormImage7 = pygame.transform.scale(pygame.image.load("./assets/images/OpponentWindyStorm/windy storm/7.png"),(450,250))
    self.sprites.append(OpponentWindyStormImage7)
    OpponentWindyStormImage8 = pygame.transform.scale(pygame.image.load("./assets/images/OpponentWindyStorm/windy storm/8.png"),(450,250))
    self.sprites.append(OpponentWindyStormImage8)
    OpponentWindyStormImage9 = pygame.transform.scale(pygame.image.load("./assets/images/OpponentWindyStorm/windy storm/9.png"),(450,250))
    self.sprites.append(OpponentWindyStormImage9)
    OpponentWindyStormImage10 = pygame.transform.scale(pygame.image.load("./assets/images/OpponentWindyStorm/windy storm/10.png"),(450,250))
    self.sprites.append(OpponentWindyStormImage10)
    OpponentWindyStormImage11 = pygame.transform.scale(pygame.image.load("./assets/images/OpponentWindyStorm/windy storm/11.png"),(450,250))
    self.sprites.append(OpponentWindyStormImage11)
    OpponentWindyStormImage12 = pygame.transform.scale(pygame.image.load("./assets/images/OpponentWindyStorm/windy storm/12.png"),(450,250))
    self.sprites.append(OpponentWindyStormImage12)
    self.currentSprit = 0
    self.image = self.sprites[self.currentSprit]

    
    self.rect = self.image.get_rect()
    self.rect.topleft = [posX,posY]
    print(self.rect,self.rect.topleft)
    
    
    
  def update(self):
    if self.is_animating == True:
      if self.is_waiting == 0:
        self.currentSprit += 0.4
        self.rect.x -= 8

        if(int(self.currentSprit) == 0):
          self.currentSprit = 1
        if self.currentSprit >= len(self.sprites):
          self.currentSprit = 1
        if self.rect.x <200:
          self.is_animating = False
          self.currentSprit = 0
          self.rect.x = 800
          self.is_waiting = 45
        self.image = self.sprites[int(self.currentSprit)]  
      else:
        self.is_waiting -= 1 
      
  def animate(self):
    self.is_animating = True 
    print("called")  
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('./assets/audiofiles/wind 1.wav'))
         
  
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
    pygame.mixer.Channel(2).play(pygame.mixer.Sound('./assets/audiofiles/fireball.mp3'))
          
  
  
  
mainCharAnimating = False    

# class MainCharMove1Attack(pygame.sprite.Sprite):
#   def __init__(self, posX,posY) :
#     super().__init__()
#     self.sprites = []
#     self.is_animating = False
#     # MainCharMove1Image1 = pygame.image.load("./assets/images/MainCharMove1Attack/final/1.png")
#     MainCharMove2Image = pygame.image.load("./assets/images/invisible.png")
#     self.sprites1.append(MainCharMove2Image)
#     MainCharMove1Image0 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/0.png"), (250,400))
#     self.sprites1.append(MainCharMove1Image0)
#     MainCharMove1Image1 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/1.png"), (250,400))
#     self.sprites1.append(MainCharMove1Image1)
#     MainCharMove1Image2 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/2.png"), (250,400))
#     self.sprites1.append(MainCharMove1Image2)
#     MainCharMove1Image3 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/3.png"), (250,400))
#     self.sprites1.append(MainCharMove1Image3)
#     MainCharMove1Image4 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/4.png"), (400,400))
#     self.sprites1.append(MainCharMove1Image4)
#     MainCharMove1Image5 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/5.png"), (350,400))
#     self.sprites1.append(MainCharMove1Image5)
#     MainCharMove1Image6 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/6.png"), (350,400))
#     self.sprites1.append(MainCharMove1Image6)
#     MainCharMove1Image7 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/7.png"), (350,400))
#     self.sprites1.append(MainCharMove1Image7)
#     self.currentSprit = 0
#     self.image = self.sprites[self.currentSprit]
    
#     self.rect = self.image.get_rect()
#     self.rect.topleft = [posX,posY]
#     print(self.rect,self.rect.topleft)
    
    
    
#   def update(self):
#     if self.is_animating == True:
#       self.currentSprit += 0.1

#       if self.currentSprit >= len(self.sprites):
#         self.currentSprit = 0
#         self.is_animating = False
        
#       self.image = self.sprites[int(self.currentSprit)]  
#     else:
#       if mainCharAnimating == True:
#         self.image = self.sprites[0]
#       self.image = self.sprites[1]   
      
#   def animate(self):
#     self.is_animating = True 
#     print("called") 
  
  
class MainCharMove2Attack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites1 = []
    self.sprites2 = []
    self.sprites3 = []
    self.sprites4 = []
    
    
    self.is_animating = False
    
    # self.sprites1.append(MainCharMove2Image)
    MainCharMove1Image0 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/0.png"), (250,400))
    self.sprites1.append(MainCharMove1Image0)
    MainCharMove1Image1 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/1.png"), (250,400))
    self.sprites1.append(MainCharMove1Image1)
    MainCharMove1Image2 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/2.png"), (250,400))
    self.sprites1.append(MainCharMove1Image2)
    MainCharMove1Image3 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/3.png"), (250,400))
    self.sprites1.append(MainCharMove1Image3)
    MainCharMove1Image4 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/4.png"), (400,400))
    self.sprites1.append(MainCharMove1Image4)
    MainCharMove1Image5 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/5.png"), (350,400))
    self.sprites1.append(MainCharMove1Image5)
    MainCharMove1Image6 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/6.png"), (350,400))
    self.sprites1.append(MainCharMove1Image6)
    MainCharMove1Image7 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move1/7.png"), (350,400))
    self.sprites1.append(MainCharMove1Image7)
    
    # MainCharMove2Image1 = pygame.image.load("./assets/images/MainCharMove2Attack/final/1.png")
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
    self.sprites2.append(MainCharMove2Image7)
    MainCharMove2Image8 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move2/8.png"), (350,400))
    self.sprites2.append(MainCharMove2Image8)
    MainCharMove2Image9 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move2/9.png"), (350,400))
    self.sprites2.append(MainCharMove2Image9)
    
    
    MainCharmove3Image0 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move3/0.png"), (250,400))
    self.sprites3.append(MainCharmove3Image0)
    MainCharmove3Image11 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move3/11.png"), (250,400))
    self.sprites3.append(MainCharmove3Image11)
    MainCharmove3Image1 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move3/1.png"), (250,400))
    self.sprites3.append(MainCharmove3Image1)
    MainCharmove3Image2 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move3/2.png"), (250,400))
    self.sprites3.append(MainCharmove3Image2)
    MainCharmove3Image3 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move3/3.png"), (250,400))
    self.sprites3.append(MainCharmove3Image3)
    MainCharmove3Image4 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move3/4.png"), (250,400))
    self.sprites3.append(MainCharmove3Image4)
    MainCharmove3Image5 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move3/5.png"), (250,400))
    self.sprites3.append(MainCharmove3Image5)
    MainCharmove3Image6 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move3/6.png"), (250,400))
    self.sprites3.append(MainCharmove3Image6)
    MainCharmove3Image7 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move3/7.png"), (250,400))
    self.sprites3.append(MainCharmove3Image7)
    MainCharmove3Image8 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move3/8.png"), (250,400))
    self.sprites3.append(MainCharmove3Image8)
    MainCharmove3Image9 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move3/9.png"), (250,400))
    self.sprites3.append(MainCharmove3Image9)
    MainCharmove3Image10 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move3/10.png"), (350,400))
    self.sprites3.append(MainCharmove3Image10)
    
    MainCharmove4Image0 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/0.png"), (250,400))
    self.sprites4.append(MainCharmove4Image0)
    MainCharmove4Image11 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/11.png"), (250,400))
    self.sprites4.append(MainCharmove4Image11)
    MainCharmove4Image1 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/1.png"), (250,400))
    self.sprites4.append(MainCharmove4Image1)
    MainCharmove4Image2 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/2.png"), (250,400))
    self.sprites4.append(MainCharmove4Image2)
    MainCharmove4Image3 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/3.png"), (350,400))
    self.sprites4.append(MainCharmove4Image3)
    MainCharmove4Image4 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/4.png"), (500,400))
    self.sprites4.append(MainCharmove4Image4)
    MainCharmove4Image5 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/5.png"), (500,400))
    self.sprites4.append(MainCharmove4Image5)
    MainCharmove4Image6 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/6.png"), (500,400))
    self.sprites4.append(MainCharmove4Image6)
    MainCharmove4Image7 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/7.png"), (500,400))
    self.sprites4.append(MainCharmove4Image7)
    MainCharmove4Image8 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/8.png"), (500,400))
    self.sprites4.append(MainCharmove4Image8)
    MainCharmove4Image9 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/9.png"), (500,400))
    self.sprites4.append(MainCharmove4Image9)
    MainCharmove4Image10 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/10.png"), (500,400))
    self.sprites4.append(MainCharmove4Image10)
    MainCharmove4Image11 = pygame.transform.scale(pygame.image.load("./assets/images/enemy1/move4/11.png"), (500,400))
    self.sprites4.append(MainCharmove4Image11)
    
    
    
    
    self.currentSprit = 0
    self.move = 0
    self.image = self.sprites1[self.currentSprit]
    
    
    
    
    
    self.rect = self.image.get_rect()
    self.rect.topleft = [posX,posY]
    self.sprites = []
    self.sprites.append(self.sprites1)
    self.sprites.append(self.sprites2)
    self.sprites.append(self.sprites3)
    self.sprites.append(self.sprites4)
    print(self.rect,self.rect.topleft)
    
    
    
  def update(self):
    if self.is_animating == True:
      self.currentSprit += 0.1

      if self.currentSprit >= len(self.sprites[self.move]):
        self.currentSprit = 0
        self.is_animating = False
        
      self.image = self.sprites[self.move][int(self.currentSprit)]  
    # else:
    #   self.image = self.sprites[1]  
        
      
  def animate(self,move):
    mainCharAnimating = True
    self.move = move
    self.is_animating = True 
    print("called")   
  
class Enemy1CharMove2Attack(pygame.sprite.Sprite):
  def __init__(self, posX,posY) :
    super().__init__()
    self.sprites1 = []
    self.sprites2 = []
    self.sprites3 = []
    self.sprites4 = []
    
    
    self.is_animating = False
    
    # self.sprites1.append(Enemy1CharMove2Image)
    Enemy1CharMove1Image0 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/1.png"), (250,400))
    self.sprites1.append(Enemy1CharMove1Image0)
    Enemy1CharMove1Image1 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/2.png"), (250,400))
    self.sprites1.append(Enemy1CharMove1Image1)
    Enemy1CharMove1Image2 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/3.png"), (250,400))
    self.sprites1.append(Enemy1CharMove1Image2)
    Enemy1CharMove1Image3 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/4.png"), (250,400))
    self.sprites1.append(Enemy1CharMove1Image3)
    Enemy1CharMove1Image4 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/5.png"), (400,400))
    self.sprites1.append(Enemy1CharMove1Image4)
    Enemy1CharMove1Image5 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/6.png"), (350,400))
    self.sprites1.append(Enemy1CharMove1Image5)
    Enemy1CharMove1Image6 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/7.png"), (350,400))
    self.sprites1.append(Enemy1CharMove1Image6)
    Enemy1CharMove1Image7 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/8.png"), (350,400))
    self.sprites1.append(Enemy1CharMove1Image7)
    Enemy1CharMove1Image8 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/9.png"), (250,400))
    self.sprites1.append(Enemy1CharMove1Image8)
    Enemy1CharMove1Image9 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/10.png"), (250,400))
    self.sprites1.append(Enemy1CharMove1Image9)
    Enemy1CharMove1Image10 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/11.png"), (250,400))
    self.sprites1.append(Enemy1CharMove1Image10)
    Enemy1CharMove1Image11 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/12.png"), (250,400))
    self.sprites1.append(Enemy1CharMove1Image11)
    Enemy1CharMove1Image12 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/13.png"), (400,400))
    self.sprites1.append(Enemy1CharMove1Image12)
    Enemy1CharMove1Image13 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/14.png"), (350,400))
    self.sprites1.append(Enemy1CharMove1Image13)
    Enemy1CharMove1Image14 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/15.png"), (350,400))
    self.sprites1.append(Enemy1CharMove1Image14)
    Enemy1CharMove1Image15 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/16.png"), (350,400))
    self.sprites1.append(Enemy1CharMove1Image15)
    Enemy1CharMove1Image16 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/17.png"), (350,400))
    self.sprites1.append(Enemy1CharMove1Image16)
    Enemy1CharMove1Image17 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/18.png"), (350,400))
    self.sprites1.append(Enemy1CharMove1Image17)
    Enemy1CharMove1Image18 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move1/19.png"), (350,400))
    self.sprites1.append(Enemy1CharMove1Image18)
    
    # Enemy1CharMove2Image1 = pygame.image.load("./assets/images/Enemy1CharMove2Attack/final/1.png")
    Enemy1CharMove2Image0 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move2/0.png"), (250,400))
    self.sprites2.append(Enemy1CharMove2Image0)
    Enemy1CharMove2Image1 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move2/1.png"), (250,400))
    self.sprites2.append(Enemy1CharMove2Image1)
    Enemy1CharMove2Image2 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move2/2.png"), (250,400))
    self.sprites2.append(Enemy1CharMove2Image2)
    Enemy1CharMove2Image3 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move2/3.png"), (250,400))
    self.sprites2.append(Enemy1CharMove2Image3)
    Enemy1CharMove2Image4 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move2/4.png"), (400,400))
    self.sprites2.append(Enemy1CharMove2Image4)
    Enemy1CharMove2Image5 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move2/5.png"), (350,400))
    self.sprites2.append(Enemy1CharMove2Image5)
    Enemy1CharMove2Image6 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move2/6.png"), (350,400))
    self.sprites2.append(Enemy1CharMove2Image6)
    Enemy1CharMove2Image7 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move2/7.png"), (350,400))
    self.sprites2.append(Enemy1CharMove2Image7)
    Enemy1CharMove2Image8 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move2/8.png"), (350,400))
    self.sprites2.append(Enemy1CharMove2Image8)
    Enemy1CharMove2Image9 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move2/9.png"), (350,400))
    self.sprites2.append(Enemy1CharMove2Image9)
    Enemy1CharMove2Image10 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move2/10.png"), (350,400))
    self.sprites2.append(Enemy1CharMove2Image10)
    
    
    Enemy1CharMove3Image = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/0.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image)
    Enemy1CharMove3Image0 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/1.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image0)
    Enemy1CharMove3Image1 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/2.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image1)
    Enemy1CharMove3Image2 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/3.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image2)
    Enemy1CharMove3Image3 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/4.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image3)
    Enemy1CharMove3Image4 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/5.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image4)
    Enemy1CharMove3Image5 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/6.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image5)
    Enemy1CharMove3Image6 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/7.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image6)
    Enemy1CharMove3Image7 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/8.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image7)
    Enemy1CharMove3Image8 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/9.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image8)
    Enemy1CharMove3Image9 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/10.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image9)
    Enemy1CharMove3Image10 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/11.png"), (350,400))
    self.sprites3.append(Enemy1CharMove3Image10)
    Enemy1CharMove3Image11 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/12.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image11)
    Enemy1CharMove3Image12 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/13.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image12)
    Enemy1CharMove3Image13 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move3/14.png"), (250,400))
    self.sprites3.append(Enemy1CharMove3Image13)

    
    Enemy1CharMove4Image0 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/0.png"), (250,400))
    self.sprites4.append(Enemy1CharMove4Image0)
    Enemy1CharMove4Image11 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/1.png"), (250,400))
    self.sprites4.append(Enemy1CharMove4Image11)
    Enemy1CharMove4Image1 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/2.png"), (250,400))
    self.sprites4.append(Enemy1CharMove4Image1)
    Enemy1CharMove4Image2 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/3.png"), (250,400))
    self.sprites4.append(Enemy1CharMove4Image2)
    Enemy1CharMove4Image3 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/4.png"), (350,400))
    self.sprites4.append(Enemy1CharMove4Image3)
    Enemy1CharMove4Image4 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/5.png"), (500,400))
    self.sprites4.append(Enemy1CharMove4Image4)
    Enemy1CharMove4Image5 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/6.png"), (500,400))
    self.sprites4.append(Enemy1CharMove4Image5)
    Enemy1CharMove4Image6 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/7.png"), (500,400))
    self.sprites4.append(Enemy1CharMove4Image6)
    Enemy1CharMove4Image7 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/8.png"), (500,400))
    self.sprites4.append(Enemy1CharMove4Image7)
    Enemy1CharMove4Image8 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/9.png"), (500,400))
    self.sprites4.append(Enemy1CharMove4Image8)
    Enemy1CharMove4Image9 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/10.png"), (500,400))
    self.sprites4.append(Enemy1CharMove4Image9)
    Enemy1CharMove4Image10 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/11.png"), (500,400))
    self.sprites4.append(Enemy1CharMove4Image10)
    Enemy1CharMove4Image11 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/12.png"), (500,400))
    self.sprites4.append(Enemy1CharMove4Image11)
    Enemy1CharMove4Image12 = pygame.transform.scale(pygame.image.load("./assets/images/chr4/move4/13.png"), (500,400))
    self.sprites4.append(Enemy1CharMove4Image12)
    
    
    
    
    self.currentSprit = 0
    self.move = 0
    self.image = self.sprites1[self.currentSprit]
    
    
    
    
    
    self.rect = self.image.get_rect()
    self.rect.topleft = [posX,posY]
    self.sprites = []
    self.sprites.append(self.sprites1)
    self.sprites.append(self.sprites2)
    self.sprites.append(self.sprites3)
    self.sprites.append(self.sprites4)
    print(self.rect,self.rect.topleft)
    
    
    
  def update(self):
    if self.is_animating == True:
      self.currentSprit += 0.1

      if self.currentSprit >= len(self.sprites[self.move]):
        self.currentSprit = 0
        self.is_animating = False
        
      self.image = self.sprites[self.move][int(self.currentSprit)]  
    # else:
    #   self.image = self.sprites[1]  
        
      
  def animate(self,move):
    mainCharAnimating = True
    self.move = move
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
waterVortexattack = WaterVortexAttack(350,100)
WaterVertex_sprites.add(waterVortexattack) 

opponentwaterVortexattack_sprites = pygame.sprite.Group()
opponentwaterVortexattack = OpponentWaterVortexAttack(800,100)
opponentwaterVortexattack_sprites.add(opponentwaterVortexattack) 

fireBall_sprites = pygame.sprite.Group()
fireBallattack = FireBallAttack(200,200)
fireBall_sprites.add(fireBallattack) 

opponentFireBall_sprites = pygame.sprite.Group()
opponentFireBallattack = OpponentFireBallAttack(800,200)
opponentFireBall_sprites.add(opponentFireBallattack) 

windyStorm_sprites = pygame.sprite.Group()
windystormattack = WindyStormAttack(200,250)
windyStorm_sprites.add(windystormattack) 

opponentwindyStorm_sprites = pygame.sprite.Group()
opponentwindystormattack = OpponentWindyStormAttack(800,200)
opponentwindyStorm_sprites.add(opponentwindystormattack) 

stonebullets_sprites = pygame.sprite.Group()
stonebulletsattack = StoneBulletAttack(200,250)
stonebullets_sprites.add(stonebulletsattack) 

opponentstonebullets_sprites = pygame.sprite.Group()
opponentstonebulletsattack = OpponentStoneBulletAttack(800,200)
opponentstonebullets_sprites.add(opponentstonebulletsattack) 


mainCharMove2_sprites = pygame.sprite.Group()
mainCharMove2attack = MainCharMove2Attack(150,100)
mainCharMove2_sprites.add(mainCharMove2attack) 

enemy1charMove2_sprites = pygame.sprite.Group()
enemy1charMove2attack = Enemy1CharMove2Attack(800,100)
enemy1charMove2_sprites.add(enemy1charMove2attack) 



class Bar ():
  def __init__(self,x,y,maxi,color1,color2):
    self.x = x
    self.y = y
    self.maxi = maxi
    self.hp = maxi
    self.color1 = color1
    self.color2 = color2
    
  def draw(self,surface):
    ratio = self.hp / self.maxi
    pygame.draw.rect(surface,self.color1,(self.x,self.y,500,15))
    pygame.draw.rect(surface,self.color2,(self.x,self.y,500*ratio,15))

game_state = "menu"
game_level = 0
magical_energy = 900
MagicalEnergyImage = pygame.transform.scale(pygame.image.load("./assets/images/magic_ball.png"), (50,50))

player_turn = True
playerHealthBar = Bar(15,5,100,(0,150,0),(0,255,0))
playerAttackBar = Bar(15,25,100,(100,100,100),(0,213,255))

Enemy1HealthBar = Bar(630,5,100,(0,150,0),(0,255,0))
Enemy1AttackBar = Bar(630,25,100,(100,100,100),(0,213,255))

backgroundaudio = pygame.mixer.Sound('./assets/audiofiles/game home.wav')
backgroundaudio.set_volume(0.4)
mymusic = pygame.mixer.Channel(0).play(backgroundaudio,-1)
run = True


Title = pygame.transform.scale(pygame.image.load("./assets/audiofiles/Battle Fantasy.png"), (500,100))


while run:

  screenReady = True

  if game_state == "menu":
    screen.blit(menuBackgroundImage, (0, 0))
    screen.blit(Title,(600,0))
    screen.blit(play_img, (200, 100))
    screen.blit(shop_img, (200, 250))
    screen.blit(quit_img, (200, 400))
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        x,y=pygame.mouse.get_pos()  
        if (x>200 and x<450):
          
          if( y>100 and y<160):
            game_state = "game"
          elif( y>250 and y<410):
            game_state = "shop"
          elif( y>300 and y<460):
            run = False
    screenReady = False    
    magical_energyadd = False
  elif game_state == "game":

    
    screen.blit(battleFieldBackgroundImage, (0, 0))
    screen.blit(MagicalEnergyImage, (525, 0))
    playerHealthBar.draw(screen)
    playerAttackBar.draw(screen)
    Enemy1AttackBar.draw(screen)
    Enemy1HealthBar.draw(screen)
    draw_text(str(magical_energy), font, TEXT_COL, 575, 5)
    
    screen.blit(fireBallAttackButtonImage, (0, 530))
    screen.blit(WaterVortexAttackButtonImage, (300, 530))
    screen.blit(stoneBulletsAttackButtonImage, (600, 530))
    screen.blit(windyStormAttackButtonImage, (900,530))
    
    WaterVertex_sprites.draw(screen)
    WaterVertex_sprites.update()
    
    opponentwaterVortexattack_sprites.draw(screen)
    opponentwaterVortexattack_sprites.update()
    
    fireBall_sprites.draw(screen)
    fireBall_sprites.update()
    
    opponentFireBall_sprites.draw(screen)
    opponentFireBall_sprites.update()
    
    windyStorm_sprites.draw(screen)
    windyStorm_sprites.update()
    
    opponentwindyStorm_sprites.draw(screen)
    opponentwindyStorm_sprites.update()
    
    stonebullets_sprites.draw(screen)
    stonebullets_sprites.update()
    
    opponentstonebullets_sprites.draw(screen)
    opponentstonebullets_sprites.update()
    
    mainCharMove2_sprites.draw(screen)
    mainCharMove2_sprites.update()
    
    enemy1charMove2_sprites.draw(screen)
    enemy1charMove2_sprites.update()
    
    pygame.display.flip()
    clock.tick(80)

    if playerHealthBar.hp >0 and Enemy1HealthBar.hp > 0:
    
    #event handler
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            game_state = "menu"
        elif event.type == pygame.QUIT:
          run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
          x,y=pygame.mouse.get_pos()
          if player_turn:
            
            if x < 250 and y>530:
               
              mainCharMove2attack.animate(0)
              fireBallattack.animate()
              
              Enemy1HealthBar.hp -= random.randint(15,25) 
              playerAttackBar.hp -= 15
              playerHealthBar.hp -= playerAttackBar.hp*0.01*random.randint(1,10)
              player_turn = False
            elif (x > 300 and x < 550):  
              player_turn = False
              mainCharMove2attack.animate(1)
              waterVortexattack.animate()
               
              Enemy1HealthBar.hp -= random.randint(15,25) 
              playerHealthBar.hp -= playerAttackBar.hp*0.01*random.randint(1,10)
              playerAttackBar.hp -= 15
              
            elif (x > 600 and x < 850):
              player_turn = False
              mainCharMove2()
              mainCharMove2attack.animate(3)
              stonebulletsattack.animate()
               
              Enemy1HealthBar.hp -= random.randint(15,25) 
              playerHealthBar.hp -= playerAttackBar.hp*0.01*random.randint(1,10)
              playerAttackBar.hp -= 15
              # stoneBullet()
            elif (x > 900):
              player_turn = False
              mainCharMove2()
              mainCharMove2attack.animate(2)
              windyStorm() 
              windystormattack.animate()
               
              Enemy1HealthBar.hp -= random.randint(15,25) 
              playerHealthBar.hp -= playerAttackBar.hp*0.01*random.randint(1,10)
              playerAttackBar.hp -= 15
            else :
              player_turn = True 
               
            playerAttackBar.hp += random.randint(5,15)
            if playerAttackBar.hp > playerAttackBar.maxi:
              playerAttackBar.hp = playerAttackBar.maxi
          elif not player_turn:
            index = random.choice([0,1,2,3])
            if index == 0:
              enemy1charMove2attack.animate(0)
              opponentFireBallattack.animate()
               
              playerHealthBar.hp -= random.randint(15,25)
              Enemy1HealthBar.hp -= Enemy1HealthBar.hp*0.01*random.randint(1,10)
              Enemy1AttackBar.hp -= 15
            elif index == 1:
              enemy1charMove2attack.animate(1)
              opponentwaterVortexattack.animate() 
               
              playerHealthBar.hp -= random.randint(15,25)
              Enemy1HealthBar.hp -= Enemy1HealthBar.hp*0.01*random.randint(1,10)
              Enemy1AttackBar.hp -= 15
            elif  index == 2:
              enemy1charMove2attack.animate(2)
              opponentwindystormattack.animate()  
               
              playerHealthBar.hp -= random.randint(15,25)
              Enemy1HealthBar.hp -= Enemy1HealthBar.hp*0.01*random.randint(1,10)
              Enemy1AttackBar.hp -= 15
            elif index == 3:
              enemy1charMove2attack.animate(3)
              opponentstonebulletsattack.animate()   
              playerHealthBar.hp -= random.randint(15,25)
               
              Enemy1HealthBar.hp -= Enemy1HealthBar.hp*0.01*random.randint(1,10)
              Enemy1AttackBar.hp -= 15
            Enemy1AttackBar.hp += random.randint(5,15)
            if Enemy1AttackBar.hp > Enemy1AttackBar.maxi:
              Enemy1AttackBar.hp = Enemy1AttackBar.maxi
            player_turn = True
    elif (playerHealthBar.hp < 0):
        
        draw_text("You Died",gameFont,TEXT_COL,300,200)
        if magical_energyadd == False:
          magical_energy += random.randint(20,35)
          magical_energyadd = True
          print(magical_energyadd,magical_energy)
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              playerAttackBar.hp = playerAttackBar.maxi
              playerHealthBar.hp = playerHealthBar.maxi
              Enemy1AttackBar.hp = Enemy1AttackBar.maxi
              Enemy1HealthBar.hp = Enemy1HealthBar.maxi
              game_state = "menu"
              
        
    elif (Enemy1HealthBar.hp < 0):
        if magical_energyadd == False:
          magical_energy += random.randint(100,130)
          magical_energyadd = True
        draw_text("Victory",gameFont,TEXT_COL,300,200)
        for event in pygame.event.get():
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              playerAttackBar.hp = playerAttackBar.maxi
              playerHealthBar.hp = playerHealthBar.maxi
              Enemy1AttackBar.hp = Enemy1AttackBar.maxi
              Enemy1HealthBar.hp = Enemy1HealthBar.maxi
              game_state = "menu"
              
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
    draw_text(str(magical_energy),font,TEXT_COL,575, 5)
    screen.blit(MagicalEnergyImage, (525, 0))
    armorUpgradeCost = int(playerHealthBar.hp*2.3)
    draw_text(str(armorUpgradeCost), font, TEXT_COL, 210,180)
    screen.blit(MagicalEnergyImage, (160, 175))
    screen.blit(armor_img, (100, 100))
    swordUpgradeCost = int(playerAttackBar.hp*2.3)
    draw_text(str(swordUpgradeCost), font, TEXT_COL, 600,200)
    screen.blit(MagicalEnergyImage, (550,195))
    screen.blit(sword_img, (500, 100))
    screen.blit(upgrade_img, (300, 300))
    draw_text(str(setupgrade), font, TEXT_COL, 375,370)
    
    
    draw_text("Player HP : "+str(playerHealthBar.maxi), font, TEXT_COL, 0,0)
    draw_text("Player Attack : "+str(playerAttackBar.maxi), font, TEXT_COL, 0,30)
    
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          game_state = "menu"
      elif event.type == pygame.QUIT:
        run = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        x,y=pygame.mouse.get_pos()
        print(x,y)   
        if y > 100 and y < 160:
          if(x>100 and x <350):
            setupgrade ="Armor"
          elif x >500 and x < 750:
            setupgrade = "Sword" 
            print("sword")
        elif y >300 and y < 360 and x > 300 and x < 550 :
          if setupgrade == "Armor":
            if(magical_energy >= armorUpgradeCost):
              playerHealthBar.maxi += 30
              playerHealthBar.hp = playerHealthBar.maxi
              magical_energy -= armorUpgradeCost
            
          elif setupgrade == "Sword":
            if(magical_energy >= swordUpgradeCost):
              playerAttackBar.maxi += 30   
              playerAttackBar.hp = playerAttackBar.maxi
              magical_energy -= swordUpgradeCost    
          else:
            pass    
  pygame.display.update()


pygame.quit()