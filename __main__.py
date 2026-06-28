import pygame
from sys import exit
import random
import time


pygame.init()
display = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
# load images 
sun_shine = pygame.image.load("assets/images/sunshine.png")
potatto = pygame.image.load("assets/images/potato.png")
background = pygame.image.load("assets/images/background.png")
zombie = pygame.image.load("assets/images/zombie.png")
flower = pygame.image.load("assets/images/plant.png")
peai = pygame.image.load("assets/images/pea.png")
pea_ball = pygame.image.load("assets/images/basketball.png")
# game vaariable
game_font = pygame.font.SysFont("DejaVu Sans Mono", 25)
display = pygame.display.set_mode((background.get_width(), background.get_height()))
display_age = 0
multiplication_x = 81
multiplication_y = 92
around = [ 20, 15, -20, -15, -25, 25]
def_sunshine = 100
zombie_exist = 0
x = background.get_height() + 400
garden = [[None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None]]
# garden list
object_in_garden = []
# class
class Object():
    def __init__(self, image , x, y, hp):
        self.wait = 0
        self.planted = False
        self.age = 0
        self.hp = hp
        self.x = x
        self.y = y
        self.image = image
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            garden[int(self.y / multiplication_y - 1)][int(self.x/ multiplication_x - 3)] = None
            object_in_garden.remove(self)
    def draw(self, size):
        new = pygame.transform.scale(self.image, (size[0],size[1]))
        display.blit(new, (self.x, self.y))
    def move(self, speed):
        self.x += speed
    def attack(self):
        pass



class Plant(Object):
    def __init__(self, image, x, y, hp):
        self.pay = 25
        super().__init__(image, x, y, hp)

class Potato(Object):
    def __init__(self, image, x, y, hp):
        self.pay = 50
        super().__init__(image, x, y, hp)
        self.hp = 2*hp

class Ball(Object):
    def __init__(self, image, x, y, hp, pea, zom):
        super().__init__(image, x, y, hp)
        self.pea = pea
        self.enemy = zom
        object_in_garden.append(self)
    def attack(self):
        if  self.enemy.x - self.x <= 10 and self.enemy.x - self.x > 0 :
            self.enemy.take_damage(20)
            object_in_garden.remove(self)
            self.pea.ball = True

class Pea(Object):
    def __init__(self, image, x, y, hp):
        self.pay = 25
        super().__init__(image, x, y, hp)
        self.ball = True 
        self.hp = hp - 15
    def attack(self):
        for i in object_in_garden:
            if type(i) == Zombie:
                if i.y == self.y and self.ball == True:
                    self.last = pygame.time.get_ticks()
                    Ball(pea_ball, self.x + 30, self.y +5 , 0.1, self, i)
                    self.ball = False
class Sunshine(Object):
    def  __init__(self, image, x, y, hp):
        super().__init__(image, x, y, hp) 
        object_in_garden.append(self)         
        self.x = x + random.choice(around)
        self.y = y + random.choice(around)  
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
    def attack(self):
        global def_sunshine
        click = pygame.mouse.get_pressed()[0]
        if click == True:
            object_in_garden.remove(self)
            def_sunshine += 25

class Zombie(Object):
    def __init__(self, image, x, y, hp):
        super().__init__(image, x, y, hp)
        self.prem = True
    def move(self, speed):
        if self.prem:
            self.x += speed
        if self.x < 150:
            pygame.QUIT
            exit()
    def attack(self):
        line  = int(self.y / multiplication_y - 1)
        for i in garden[line]:
            if i != None:           
                if i.x  - self.x >= -40:
                    i.take_damage(0.5)
                    self.prem = False
                    break
            else:
                self.prem = True
    def take_damage(self, damage):
        global zombie_exist
        self.hp -= damage
        if self.hp <= 0:
            if self in object_in_garden:
                object_in_garden.remove(self)
                zombie_exist -= 1
def draw_text(text, font, color, coordinate):
    img = font.render(text, True, color)
    display.blit(img, coordinate)
button = {        # get the keyboard click by "if event.key" in while loop and form this dict understand what plant should planting
    "s" : {"class":Plant, "image":flower},
    "p" : {"class":Potato, "image":potatto},
    "b" : {"class":Pea, "image":peai}  
   
}
def rsunshine():
    global def_sunshine
    x = random.choice([200,900])
    y = random.choice([80, 900])
    sky = Sunshine(sun_shine, x, y , 1)
    object_in_garden.append(sky)
def rzombie():
    global zombie_exist
    ranit = random.randrange(1,6)  
    object_in_garden.append(Zombie(zombie, x, ranit * multiplication_y, 100))
    zombie_exist += 1
def Planting(mx, my):
    global plant_key
    global def_sunshine
    a = None
    x_multiple = int(mx / multiplication_x)
    x = multiplication_x * x_multiple
    y_multiple = int(my / multiplication_y)
    y = multiplication_y * y_multiple
    if garden[y_multiple - 1][x_multiple - 3] == None:
        try:
            if def_sunshine >= 25:
                a = button[plant_key]["class"](button[plant_key]["image"], x, y, 50)
                if a.planted == False:
                    object_in_garden.append(a)
                    garden[y_multiple - 1][x_multiple - 3] = a
                    def_sunshine -= a.pay
                    plant_key = None
            else:
                print("you'r sunshine isn't enough")
        except KeyError:
            print("press s for sunflower and p for potato and b for pea")
plant_key = None    # temporary variable for keep eaht shortcut pressed
# the game frame rate
while True:
    display.fill((50, 50, 50))
    # check what plant you select to planting
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                plant_key = "p"
            elif event.key == pygame.K_s:
                plant_key = "s"
            elif event.key == pygame.K_b:
                plant_key = "b"
        # quit app 
        if event.type == pygame.QUIT:
            pygame.QUIT
            exit()
    display.blit(background, (0,0))     
    # check you clicked planting
    mouse = pygame.mouse.get_pressed()
    if mouse == (True, False, False):
        mouse_pos = pygame.mouse.get_pos()
        if mouse_pos[0] < 252 or mouse_pos[0] > 986 or mouse_pos[1] < 76 or mouse_pos[1] > 565:
            print("clicked out of garden")  
        else:
            Planting(mouse_pos[0], mouse_pos[1])
    #text in screen
    draw_text(f"sunshine:{def_sunshine}", game_font, "black", (250,25))
    # moving ,attcking ...all object in game
    if zombie_exist == 0:
        rzombie()
    for i in object_in_garden[:]:
        if isinstance(i, Zombie):
            i.draw([110,110])
            i.move(-2)
            i.age += 0.5
            i.attack()
            if i.age % 200 == 0:
                rzombie()
        elif isinstance(i, Ball):
            i.move(3)
            i.draw([30,30])
            i.attack()
        elif isinstance(i, Sunshine):
            i.draw([45,45])
            i.age += 0.5
            pos = pygame.mouse.get_pos()
            if i.rect.collidepoint(pos):
                i.attack()
        else:
            i.age += 0.5
            i.draw([90,90])
            if i.age % 25 == 0:
                i.attack()
            if isinstance(i, Plant):
                if i.age % 150 == 0:
                    Sunshine(sun_shine, i.x, i.y, 1)
    display_age += 0.5
    if display_age % 150 == 0:
        rsunshine()
    # if zombie_exist == 7:
    #     draw_text("win", game_font, "white", (300,300))
    #     time.sleep(100)
    #     pygame.quit()
    #     exit()    

    # update every event happnend in display
    pygame.display.update()
    clock.tick(60)