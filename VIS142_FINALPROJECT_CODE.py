import random
import pygame, sys

# Task 1: Animate the frames ✓
# Task 2: at the end of the CA sequence, 
#           insert a randomized star rain 
#           that appear from right to left ✓
#           in a certain sequence, 
#           in a certain speed, 
#           and stay on the screen,
#           covering entire screen and turn it white
# Task 3: make a loop ✓


# Setting up the screen
# WINSIZE = [1728, 1117]
WINSIZE = [1920, 1080]
width, height = WINSIZE  #dpi 72

# initialize and prepare screen
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINSIZE)
pygame.display.set_caption("Jinying Xie, Crowley & Aziraphale")


# Setting up custom objects
class Nebula(pygame.sprite.Sprite):
    def __init__(self):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("yellow.png"))
        self.sprites.append(pygame.image.load("orange.png"))
        self.sprites.append(pygame.image.load("blue.png"))
        self.sprites.append(pygame.image.load("pink.png"))
        self.sprites.append(pygame.image.load("purple.png"))
        self.sprites.append(pygame.image.load("white dot.png"))
        self.sprites.append(pygame.image.load("white dots series.png"))
        self.current_sprite = 0
        self.chosen_sprite = random.randint(0,1)
        self.chosen_sprite_1 = random.randint(2,4)
        self.chosen_sprite_2 = random.randint(5,6)
        self.image = self.sprites[int(self.chosen_sprite)]
        self.image_1 = self.sprites[int(self.chosen_sprite_1)]
        self.image_2 = self.sprites[int(self.chosen_sprite_2)]
    
        # Getting the dimensions of the image
        self.rect = self.image.get_rect()
        self.rect_1 = self.image_1.get_rect()
        self.rect_2 = self.image_2.get_rect()
        
        # up to down
        # self.speed_x = 3
        # self.speed_y = random.randint(5,25)
        # self.rect.x = random.randint(-100, width)
        # self.rect.y = random.randint(-height, -5)
        
        # right to left
        self.speed_y = 0
        self.speed_x = random.randint(-70, 0) # speed for running from right to left
        self.rect.y = random.randint(-35, 1080) # making sure it covers entire page
        self.rect.x = random.randint(1900, 1920) #the starting point of the image
        
        self.rect_1.y = random.randint(-35, 1080)
        self.rect_1.x = random.randint(1900, 1920)
        
        self.rect_2.y = random.randint(-35, 1080)
        self.rect_2.x = random.randint(1900, 1920)
    
    # def set1update(self):
    #     if current_time - start_time >= appearance_time_set1:
    #         self.rect.x = self.rect.x + self.speed_x
    #         self.rect.y = self.rect.y + self.speed_y
    # def set2update(self):
    #     if current_time - start_time >= appearance_time_set2:
    #         self.rect_1.x = self.rect_1.x + self.speed_x
    #         self.rect_1.y =self.rect_1.y + self.speed_y
    # def set3update(self):
    #     if current_time - start_time >= appearance_time_set2:
    #         self.rect_2.x = self.rect_2.x + self.speed_x
    #         self.rect_2.y =self.rect_2.y + self.speed_y
            
    def update(self):
        # right to left
        if current_time - start_time >= appearance_time_set1:
            self.rect.x = self.rect.x + self.speed_x
            self.rect.y = self.rect.y + self.speed_y
            # if current_time - start_time >= appearance_time_set2:
            #     self.rect_1.x = self.rect_1.x + self.speed_x
            #     self.rect_1.y =self.rect_1.y + self.speed_y
            #     if current_time - start_time >= appearance_time_set2:
            #         self.rect_2.x = self.rect_2.x + self.speed_x
            #         self.rect_2.y =self.rect_2.y + self.speed_y
        if current_time - start_time >= appearance_time_set2:
            self.rect_1.x = self.rect_1.x + self.speed_x
            self.rect_1.y =self.rect_1.y + self.speed_y
     
        # up to down
        # self.rect.x = self.rect.x + self.speed_x
        # self.rect.y = self.rect.y + self.speed_y
        
        # diagonal (?????)
        # self.rect.x = self.rect.y + self.speed_y
        # self.rect.y = self.rect.x + self.speed_x


class CA(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False # Starting with keyboard
        self.sprites.append(pygame.image.load("CA_1920x1080-1.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-2.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-3.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-4.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-5.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-6.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-7.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-8.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-9.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-10.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-11.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-12.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-13.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-14.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-15.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-16.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-15.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-16.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-15.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-16.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-15.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-16.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-15.png"))
        self.sprites.append(pygame.image.load("CA_1920x1080-16.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    # def animate(self):
        # self.is_animating = True  #for starting with keyboard
        
    def update(self):
        # if self.is_animating == True:
        self.current_sprite += 0.08  #adjusting frames per second (5fps)
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.is_animating = False
        self.image = self.sprites[int(self.current_sprite)]
        

            
# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
ca = CA(0,0)
moving_sprites.add(ca)

nebula_group = pygame.sprite.Group()
for i in range(500):
    nebula = Nebula()
    nebula_group.add(nebula)


# Main Loop

start_time = pygame.time.get_ticks() # frame time check
appearance_time_set1 = 3500  # 1000 milliseconds = 1 second
appearance_time_set2 = 3500
appearance_time_set3 = 4500

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Start with a button:
        # if event.type == pygame.KEYDOWN:
        #     ca.animate()

    screen.fill((0,0,0))
    
    # Drawing for CA
    moving_sprites.draw(screen)
    moving_sprites.update()
    
    # Drawing for Nebula
    current_time = pygame.time.get_ticks()
    # if current_time - start_time >= appearance_time_set1: 
    nebula_group.draw(screen)
    nebula_group.update()
    # if current_time - start_time >= appearance_time_set2: 
    #     nebula_group.draw(screen)
    #     nebula_group.update()
    # if current_time - start_time >= appearance_time_set3:
    #     nebula_group.draw(screen)
    #     nebula_group.update()
        
    
    # Print the specific second of the frame
    elapsed_time_seconds = (pygame.time.get_ticks() - start_time) / 1000.0
    print(f"Specific second of the frame: {elapsed_time_seconds:.2f} seconds")
    
    #Update the display
    pygame.display.flip()
    
    #Control frame rate
    fps = 60
    clock.tick(fps)
    


    
    # def generate_patterns():
#     blue = pygame.image.load("blue.png")
#     orange = pygame.image.load("orange.png")
#     pink = pygame.image.load("pink.png")
#     purple = pygame.image.load("purple.png")
#     whitedot = pygame.image.load("white dot.png")
#     dotseries = pygame.image.load("white dots series.png")
#     yellow = pygame.image.load("yellow.png")
    
#     pattern_set1 = [yellow, orange]
#     pattern_set2 = [blue, pink, purple]
#     pattern_set3 = [whitedot, dotseries]
    
#     rand_result1 = random.choice(pattern_set1)
#     rand_result2 = random.choice(pattern_set2)
#     rand_result3 = random.choice(pattern_set3)


 # self.sprites_1 = []
        # self.sprites_1.append(pygame.image.load("yellow.png"))
        # self.sprites_1.append(pygame.image.load("orange.png"))
        # self.sprites_2 = []
        # self.sprites_2.append(pygame.image.load("blue.png"))
        # self.sprites_2.append(pygame.image.load("pink.png"))
        # self.sprites_2.append(pygame.image.load("purple.png"))
        # self.sprites_3 = []
        # self.sprites_3.append(pygame.image.load("white dot.png"))
        # self.sprites_3.append(pygame.image.load("white dots series.png"))
        
        
