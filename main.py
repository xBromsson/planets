import pygame
import random

test = "testing git"

class Game:
    def __init__(self):
        pygame.init()
        self.width = 1600
        self.height = 900
        self.window = pygame.display.set_mode((self.width, self.height))
        self.caption = pygame.display.set_caption("planets")
        self.clock = pygame.time.Clock()
        self.run = True
        self.mouse = pygame.mouse.get_pos()
        self.start_point = pygame.Vector2()
        self.spawning = False

    def input(self):
        self.keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                self.mouse = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==  1:
                self.start_point = pygame.Vector2(pygame.mouse.get_pos())
                self.spawning = True
                    
                print(self.start_point)
                
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.spawning = False
                end_point = pygame.mouse.get_pos()
                power = (self.start_point - end_point)/15
                pobjects.objects.append(Asteroid(self.start_point[0], self.start_point[1], power[0], power[1]))
                
                pass


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    earth.mass += 5
                    print(earth.mass) 
                if event.key == pygame.K_s:
                    earth.mass -= 5
                    print(earth.mass) 
      
    def update(self):
        pygame.display.update()

    def render(self):
        if self.spawning == True:
            pygame.draw.circle(g.window, "blue", self.start_point, 12, 0)
            pygame.draw.line(g.window, "blue", self.start_point, pygame.mouse.get_pos(), 2)


class Objects:
    def __init__(self):
        self.objects = []

    def update(self):
        if self.objects:
            for obj in self.objects:
                obj.update()

    def render(self):
        if self.objects:
            for obj in self.objects:
                obj.render()


class Planet:
    def __init__(self, x, y):
        self.pos = pygame.Vector2(x, y)
        self.mass = 50
        self.velocity = 0

    def update(self):
        self.pos = pygame.Vector2(g.width/2, g.height/2)

    def render(self):
        pygame.draw.circle(g.window, "grey", self.pos, self.mass, 0)

class Asteroid:
    def __init__(self, x, y, q=0, w=0):
        self.mass = 12
        self.pos = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(q ,w)
        self.acceleration = pygame.Vector2(0, 0)

    def update(self):

        gravity = earth.pos-self.pos
        distance = gravity.magnitude()

        if distance > 50:
            distance = 50
        elif distance < 25:
            distance = 25
        grav_m = (graviton * self.mass * earth.mass) / (distance * distance)
        gravity = gravity.normalize()
        gravity = gravity * grav_m


        self.acceleration += gravity/self.mass
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration = self.acceleration*0
           
    def render(self):
        pygame.draw.circle(g.window, "grey", self.pos, self.mass, 0)
        pygame.draw.line(g.window, "green", self.pos, self.pos+self.velocity*5, 2)


g = Game()
earth = Planet(g.width/2, g.height/2)
pobjects = Objects()
graviton = 5

while g.run:

    g.input()
    g.window.fill('black')
    g.render()

    earth.update()
    earth.render()

    pobjects.update()
    pobjects.render()

    g.update()
    g.clock.tick(60)