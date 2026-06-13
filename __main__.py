import pygame
from sys import exit
import random
import time


pygame.init()
display = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
# load images 
potatto = pygame.image.load("assets/images/potato.png")
background = pygame.image.load("assets/images/background.png")
zombie = pygame.image.load("assets/images/zombie.png")
flower = pygame.image.load("assets/images/plant.png")
peai = pygame.image.load("assets/images/pea.png")
pea_ball = pygame.image.load("assets/images/basketball.png")
# game vaariable
display = pygame.display.set_mode((background.get_width(), background.get_height()))
multiplication_x = 81
multiplication_y = 92
corners  = [[252, 986],[76, 575]]
spown_time = 10
x = background.get_height() + 400
garden = [[None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None],
         [None, None, None, None, None, None, None, None, None]]
balls = {}
# garden list
object_in_garden = {
    "plant" : [],
    "zombie" : []
}
# class
class Plant():
    def __init__(self, image, x, y):
        self.hp = 50
        self.x = x
        self.y = y
        self.image = image
    def draw(self):
        try:
            new = pygame.transform.scale(self.image, (90,90))
            display.blit(new, (self.x, self.y))
        except:
            pass
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            garden[int(self.y / multiplication_y - 1)][int(self.x/ multiplication_x - 3)] = None
            for i in object_in_garden["plant"]:
                if i.x == self.x and i.y  == self.y:
                    object_in_garden["plant"].remove(i)
class Potato(Plant):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

class Pea(Plant):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
    def attack(self, x, y):
            self.xball = x
            self.yball = y
            balls.update({self : {"image":pea_ball, "line":int(y/multiplication_y)}})
    def draw_ball(self):
        new_pea_ball = pygame.transform.scale(pea_ball ,(25,25))  
        display.blit(new_pea_ball, (self.xball + 25, self.yball + 10))
    
class Button():
    def __init__(self, color, text):       
            self.text = pygame.font.init(text, True, "white")
            self.rect = self.text.get_rect(topleft = (10, 10))
            self.color = color
            self.clicked = False
    def draw(self, w, h):
        display.blit(self.text, self.rect)
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
             if pygame.mouse.get_pressed()[0] and self.clicked == False:
                print("clicked")

class Zombie():
    def __init__(self, image, x , y):
        self.hp = 50
        self.x = x
        self.y = y
        self.image = image
    def draw(self):
        new = pygame.transform.scale(self.image, (120, 120))
        display.blit(new, (self.x, self.y))
    def attack(self, obj):
        obj.take_damage(1)
    def take_damage(self):
        self.hp -= 20
        if self.hp < 0: 
            object_in_garden["zombie"].pop(self)
button = {        # get the keyboard click by "if event.key" in while loop and form this dict understand what plant should planting
    "s" : {"class":Plant, "image":flower},
    "p" : {"class":Potato, "image":potatto},
    "b" : {"class":Pea, "image":peai}    
}
def rzombie():
    ranit = random.randrange(1,6)  
    z = Zombie(zombie, x, ranit * multiplication_y)
    object_in_garden["zombie"].append({"obj":z,"line":int(z.y/multiplication_y), "move":True})
def Planting(mx, my):
    a = None
    x_multiple = int(mx / multiplication_x)
    x = multiplication_x * x_multiple
    y_multiple = int(my / multiplication_y)
    y = multiplication_y * y_multiple
    if garden[y_multiple - 1][x_multiple - 3] == None:
        try:
            a = button[plant_key]["class"](button[plant_key]["image"], x, y)
            object_in_garden["plant"].append(a)
            garden[y_multiple - 1][x_multiple - 3] = a
        except KeyError:
            print("press s for sunflower and p for potato")
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
    # randomize the zombie line and dont let zombie spown too many

    if len(object_in_garden["zombie"]) == 0:
        rzombie()
    if len(object_in_garden["zombie"]) != 0:
        for i in object_in_garden["zombie"]:
            i["obj"].draw()
            if i["move"] == True:
                i["obj"].x -= 1
            if len(object_in_garden["plant"]) != 0:
                for j in object_in_garden["plant"]:
                    j.draw()
                    if i["obj"].y == j.y:
                        if i["obj"].x - balls[j].x == 10:
                            i["obj"].take_damage()
                        if j not in balls:
                            try:
                                j.attack(j.x, j.y)
                            except AttributeError:
                                pass
                        if i["obj"].x - j.x < 10:
                            i ["move"] = False
                            i["obj"].attack(j)
                        else:
                            i["move"] = True      
            else:
                i["move"] = True
                pass

    # update every event happnend in display
    pygame.display.update()
    clock.tick(60)