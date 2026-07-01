import pygame
from sys import exit
import random
import time

def lose():
    pygame.init()
    display = pygame.display.set_mode((400,400))
    title = pygame.font.SysFont("Airal", 40)
    name_font = pygame.font.SysFont("Airal", 35)
    clock = pygame.time.Clock()
    def draw_text(text, font, color, coordinate):
        img = font.render(text, True, color)
        display.blit(img, coordinate)
    def draw_button(text, font, color, coordinate, event, type):
        img = font.render(text, True, color)
        rect = img.get_rect()
        rect.topleft = (coordinate[0], coordinate[1])
        display.blit(img, coordinate)
        pos = pygame.mouse.get_pos()
        if type == "back":
            if rect.collidepoint(pos):
                if even.type ==pygame.MOUSEBUTTONUP:
                    game_menu()
        if type == "play again":
            if rect.collidepoint(pos):
                if even.type ==pygame.MOUSEBUTTONUP:
                    game()            
    while True:
        display.fill((0,0,0))
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
        draw_text("Zombies ate your mind", title, "red", (55,120))
        draw_button("back", name_font, "red", (170, 340), even, "back")
        draw_button("play again", name_font, "red", (130, 220), even, "play again")
        pygame.display.update()
        clock.tick(60)
startup = True
def game():
    #creat the screen and set size
    pygame.init()
    display = pygame.display.set_mode((400, 500))
    #get cock for the frame rate 
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
    score = 0
    display_age = 0                     # use for make game harder over time and spown random sunshine
    multiplication_x = 81              # use for planting
    multiplication_y = 92
    around = [ 20, 15, -20, -15, -25, 25]  #spown sunshine around sunflower
    def_sunshine = 100 
    zombie_exist = 0
    x = background.get_height() + 400
    # waves
    zombie_damage = 0.5
    zombie_HP = 100
    potato_HP = 100
    sunflower_HP = 50
    pea_HP = 50
    Ball_damage = 20
    zombie_speed = -2
    ball_speed = 3
    zombie_age = 0.5
    garden = [[None, None, None, None, None, None, None, None, None],     #is this for zombie realised flower is front of him 
            [None, None, None, None, None, None, None, None, None],      # or two flower dont plated at the same position
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None]]
    # garden list
    object_in_garden = []
    # classes
    class Object():
        def __init__(self, image , x, y):
            self.wait = 0
            self.age = 0
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
        def __init__(self, image, x, y):
            super().__init__(image, x, y)
            self.pay = 25
            self.hp = sunflower_HP
    class Potato(Object):
        def __init__(self, image, x, y):
            self.pay = 50
            super().__init__(image, x, y)
            self.hp = potato_HP

    class Ball(Object):
        def __init__(self, image, x, y, pea, zom):
            super().__init__(image, x, y)
            self.pea = pea
            self.enemy = zom
            object_in_garden.append(self)
        def attack(self):
            if  self.enemy.x - self.x <= 10 and self.enemy.x - self.x > 0 :
                self.enemy.take_damage(Ball_damage)
                object_in_garden.remove(self)
                self.pea.ball = True

    class Pea(Object):
        def __init__(self, image, x, y):
            super().__init__(image, x, y)
            self.pay = 25
            self.ball = True 
            self.hp = pea_HP
        def attack(self):
            for i in object_in_garden:
                if isinstance(i, Zombie):
                    if i.y == self.y and self.ball == True and i.x > self.x:
                        Ball(pea_ball, self.x + 30, self.y +5 , self, i)
                        self.ball = False
    class Sunshine(Object):
        def  __init__(self, image, x, y):
            super().__init__(image, x, y) 
            object_in_garden.append(self)         
            self.x = x + random.choice(around)
            self.y = y + random.choice(around)  
            self.rect = image.get_rect()
            self.rect.topleft = (x, y)
        def attack(self):
            nonlocal def_sunshine
            click = pygame.mouse.get_pressed()[0]
            if click == True:
                object_in_garden.remove(self)
                def_sunshine += 25

    class Zombie(Object):
        def __init__(self, image, x, y):
            super().__init__(image, x, y)
            self.hp = zombie_HP
            self.prem = True
        def move(self, speed):
            if self.prem:
                self.x += speed
            if self.x < 150:
                lose()
        def attack(self):
            nonlocal zombie_damage
            line  = int(self.y / multiplication_y - 1)
            for i in garden[line]:
                if i != None:           
                    if i.x  - self.x >= -40 and i.x < self.x:
                        i.take_damage(zombie_damage)
                        self.prem = False
                        break
                else:
                    self.prem = True
        def take_damage(self, damage):
            nonlocal zombie_exist,score
            self.hp -= damage
            if self.hp <= 0:
                if self in object_in_garden:
                    object_in_garden.remove(self)
                    score += 15
                    zombie_exist -= 1
    def draw_text(text, font, color, coordinate):
        img = font.render(text, True, color)
        display.blit(img, coordinate)
    button = {        # get the keyboard click by "if event.key" in while loop and form this dict understand what plant should planting
        "s" : {"class":Plant, "image":flower},
        "p" : {"class":Potato, "image":potatto},
        "b" : {"class":Pea, "image":peai}  
    
    }
    #functions
    def rsunshine():
        nonlocal def_sunshine
        x = random.choice([400,900])
        y = random.choice([80, 900])
        print(x,y)
        Sunshine(sun_shine, x, y)
    def rzombie():
        nonlocal zombie_exist
        ranit = random.randrange(1,6)  
        object_in_garden.append(Zombie(zombie, x, ranit * multiplication_y))
        zombie_exist += 1
    def Planting(mx, my):
        nonlocal plant_key,def_sunshine,score
        a = None
        x_multiple = int(mx / multiplication_x)
        x = multiplication_x * x_multiple
        y_multiple = int(my / multiplication_y)
        y = multiplication_y * y_multiple
        if garden[y_multiple - 1][x_multiple - 3] == None:
            try:
                a = button[plant_key]["class"](button[plant_key]["image"], x, y)
                if a.pay <= def_sunshine:
                    score += 10
                    object_in_garden.append(a)
                    garden[y_multiple - 1][x_multiple - 3] = a
                    def_sunshine -= a.pay
                    plant_key = None
                else:
                    print("you'r sunshine isn't enough")
                    a = None
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
                elif event.key == pygame.K_u:
                    plant_key = None
            # quit app 
            if event.type == pygame.QUIT:
                pygame.QUIT
                exit()
        display.blit(background, (0,0))     
        # check you clicked planting
        mouse = pygame.mouse.get_pressed()
        if mouse == (True, False, False):
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] < 252 or mouse_pos[0] > 986 or mouse_pos[1] < 90 or mouse_pos[1] > 565:
                print("clicked out of garden")  
            else:
                Planting(mouse_pos[0], mouse_pos[1])
        #text in screen
        draw_text(f"sunshine:{def_sunshine}", game_font, "black", (250,25))
        draw_text(f"score:{score}", game_font, "black", (850, 25))
        if plant_key != None:
            draw_text(f"plant selected:{str(button[plant_key]["class"])[31:-2]}", pygame.font.SysFont("DejaVu Sans Mono", 20), "blue", (500, 25))
        else:
            draw_text(f"plant selected:None", pygame.font.SysFont("DejaVu Sans Mono", 20), "black", (500, 25))
        # moving ,attcking ...all object in game,
        if zombie_exist == 0:
            rzombie()
        for i in object_in_garden[:]:
            if isinstance(i, Zombie):
                i.draw([110,110])
                i.move(zombie_speed)
                i.age += zombie_age
                i.attack()
                if i.age % 200 == 0:
                    rzombie()
            elif isinstance(i, Ball):
                i.move(ball_speed)
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
                        Sunshine(sun_shine, i.x, i.y)
        display_age += 0.5
        if display_age % 150 == 0:
            rsunshine()
        if display_age % 1000 == 0:
            print("new wave")
            zombie_damage += 0.5
            zombie_HP += 50
            potato_HP += 20
            sunflower_HP += 30
            pea_HP += 10
            Ball_damage += 15
            zombie_speed += -1
            ball_speed += 1
            zombie_age += 0.5
        pygame.display.update()
        clock.tick(60)
def help():
    pygame.init()
    display = pygame.display.set_mode((400,400))
    title = pygame.font.SysFont("Airal", 40)
    name_font = pygame.font.SysFont("Airal", 35)
    clock = pygame.time.Clock()
    def draw_text(text, font, color, coordinate):
        img = font.render(text, True, color)
        display.blit(img, coordinate)
    def draw_button(text, font, color, coordinate, event):
        img = font.render(text, True, color)
        rect = img.get_rect()
        rect.topleft = (coordinate[0], coordinate[1])
        display.blit(img, coordinate)
        pos = pygame.mouse.get_pos()
        if rect.collidepoint(pos):
            if even.type ==pygame.MOUSEBUTTONUP:
                game_menu()
    keyboard = """keyboard:
    s -> ready to plant sunflower
    p -> ready to plant potato
    b -> ready to plant pea
    u -> empties your hand"""
    
    while True:
        display.fill((255,255,255))
        for even in pygame.event.get():
            now = even
            if even.type == pygame.QUIT:
                pygame.quit()
        draw_text("keyboard:", name_font, "black", (40, 30))
        draw_text("s -> ready to plant sunflower", name_font, "black", (40, 60))
        draw_text("p -> ready to plant potato", name_font, "black", (40, 90))
        draw_text("b -> ready to plant pea", name_font, "black", (40, 120))
        draw_text("u -> empties your hand", name_font, "black", (40, 150))
        draw_text("u -> empties your hand", name_font, "black", (40, 150))
        draw_button("back", name_font, "black", (165, 340), now)
        pygame.display.update()
        clock.tick(60)
        
def game_menu():
    # creat screen
    pygame.init()
    display = pygame.display.set_mode((400,400))
    name_font = pygame.font.SysFont("Airal", 55)
    button_font = pygame.font.SysFont("lucidacalligraphy", 50)
    # frame rate
    clock = pygame.time.Clock()
    def draw_button(text, font, color, coordinate, event, type):
        img = font.render(text, True, color)
        rect = img.get_rect()
        rect.topleft = (coordinate[0], coordinate[1])
        display.blit(img, coordinate)
        pos = pygame.mouse.get_pos()
        if type == "start":
            if rect.collidepoint(pos):
                img = font.render(text, True, "green")
                display.blit(img, coordinate)
                if even.type == pygame.MOUSEBUTTONDOWN:
                    display.blit(img, coordinate)
                if even.type ==pygame.MOUSEBUTTONUP:
                    pygame.quit()
                    game()
        if type == "help":
            if rect.collidepoint(pos):
                img = font.render(text, True, "blue")
                display.blit(img, coordinate)
                if even.type ==pygame.MOUSEBUTTONUP:
                        help()
        if type == "exit":
            if rect.collidepoint(pos):
                img = font.render(text, True, "red")
                display.blit(img, coordinate) 
                if even.type ==pygame.MOUSEBUTTONUP:   
                        pygame.quit()
                        exit()
                         

    def draw_text(text, font, color, coordinate):
        img = font.render(text, True, color)
        display.blit(img, coordinate)
    while True:
        display.fill((255, 255, 255))
        draw_text("plant.vs.zombie", name_font, "black", (70,30))
        for even in pygame.event.get():
            now = even
            if even.type == pygame.QUIT:
                exit()
        draw_button("help", button_font, "black", (167, 220), even, "help")
        draw_button("start!", name_font, "black", (155, 150), even, "start")
        draw_button("exit", name_font, "black", (165, 290), even, "exit")
        pygame.display.update()
        clock.tick(60)
if startup:
    game_menu()
    startup = False

