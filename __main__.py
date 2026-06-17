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
class Object():
    def __init__(self, image , x, y, hp):
        self.hp = hp
        self.x = x
        self.y = y
        self.image = image
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            garden[int(self.y / multiplication_y - 1)][int(self.x/ multiplication_x - 3)] = None
            for i in object_in_garden["plant"]:
                if i.x == self.x and i.y  == self.y:
                    object_in_garden["plant"].remove(i)
    def draw(self, size):
        new = pygame.transform.scale(self.image, (size[0],size[1]))
        display.blit(new, (self.x, self.y))
    def move(self, speed):
        self.x += speed


class Plant(Object):
    def __init__(self, image, x, y, hp):
        super().__init__(image, x, y, hp)

class Potato(Object):
    def __init__(self, image, x, y, hp):
        super().__init__(image, x, y, hp)

class Ball(Object):
    def __init__(self, image, x, y, hp, pea):
        super().__init__(image, x, y, hp)
        self.pea = pea
        balls.update({self.pea : {"image":pea_ball, "line":int(y/multiplication_y), "ball":self}})

class Pea(Object):
    def __init__(self, image, x, y, hp):
        super().__init__(image, x, y, hp)
    def attack(self):
        Ball(pea_ball ,self.x , self.y, 0.1, self)      
    
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

class Zombie(Object):
    def __init__(self, image, x, y, hp):
        super().__init__(image, x, y, hp)
    def attack(self, obj):
        obj.take_damage(1)

button = {        # get the keyboard click by "if event.key" in while loop and form this dict understand what plant should planting
    "s" : {"class":Plant, "image":flower},
    "p" : {"class":Potato, "image":potatto},
    "b" : {"class":Pea, "image":peai}    
}
def rzombie():
    ranit = random.randrange(1,6)  
    z = Zombie(zombie, x, ranit * multiplication_y, 50)
    object_in_garden["zombie"].append({"obj":z,"line":int(z.y/multiplication_y), "move":True})
def Planting(mx, my):
    a = None
    x_multiple = int(mx / multiplication_x)
    x = multiplication_x * x_multiple
    y_multiple = int(my / multiplication_y)
    y = multiplication_y * y_multiple
    if garden[y_multiple - 1][x_multiple - 3] == None:
        try:
            a = button[plant_key]["class"](button[plant_key]["image"], x, y, 100)
            object_in_garden["plant"].append(a)
            garden[y_multiple - 1][x_multiple - 3] = a
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
    # randomize the zombie line and dont let zombie spown too many

    if len(object_in_garden["zombie"]) == 0:
        rzombie()
    if len(object_in_garden["zombie"]) != 0:
        for i in object_in_garden["zombie"]:
            i["obj"].draw([110,110])
            if i["move"] == True:
                i["obj"].move(-1)
            if len(object_in_garden["plant"]) != 0:
                for j in object_in_garden["plant"]:
                    j.draw([90,90])
                    if i["obj"].y == j.y:
                        if j not in balls and type(j) == Pea:
                            j.attack()
                        if type(j) == Pea:
                            balls[j]["ball"].move(2)
                            balls[j]["ball"].draw([30,30])
                            if balls[j]["ball"].x < i["obj"].x + 15  and balls[j]["ball"].x > i["obj"].x - 15 :
                                i["obj"].take_damage(20)
                                print(i["obj"].hp)
                                balls.pop(j)
                        # print(i["obj"].x , j.x)
                        if i["obj"].x - j.x < 10 and i["obj"].y == j.y:
                            i ["move"] = False
                            i["obj"].attack(j)
                        else:
                            i["move"] = True      
                    else:
                        i["move"] = True
            else:
                i["move"] = True
                pass

    # update every event happnend in display
    pygame.display.update()
    clock.tick(60)