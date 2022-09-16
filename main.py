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

    def input(self):
        self.keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEMOTION:
                self.mouse = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==  1:
                print("True")
                pobjects.objects.append(Asteroid(self.mouse[0], self.mouse[1]))

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pobjects.objects.append(Asteroid2(self.mouse[0], self.mouse[1]))
                 
    def update(self):
        pygame.display.update()


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
        self.mass = 1
        self.velocity = 0

    def update(self):
        self.pos = pygame.Vector2(g.width/2, g.height/2)

    def render(self):
        pygame.draw.circle(g.window, "grey", self.pos, 25, 0)


class Asteroid:
    def __init__(self, x, y):
        self.mass = 5
        self.pos = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0 ,0)
        self.acceleration = pygame.Vector2(0, 0)
        

    def update(self):
        
        #gravity = (earth.pos-self.pos).normalize()/100*self.mass
        #self.acceleration += gravity/self.mass

        gravity = earth.pos-self.pos
        distance = gravity.magnitude()
        if distance > 25:
            distance = 25
        elif distance < 5:
            distance = 5
        grav_m = (graviton * self.mass * earth.mass) / (distance * distance)
        gravity.normalize()
        gravity = gravity * grav_m
        
        self.acceleration += gravity/self.mass
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration = self.acceleration*0
           
    def render(self):
        pygame.draw.circle(g.window, "grey", self.pos, self.mass, 0)
        pygame.draw.line(g.window, "green", self.pos, self.pos+self.velocity, 2)


class Asteroid2:
    def __init__(self, x, y):
        self.mass = 10
        self.pos = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0 ,0)
        self.acceleration = pygame.Vector2(0, 0)
        

    def update(self):

        #gravity = (earth.pos-self.pos).normalize()/100*self.mass
        gravity = earth.pos-self.pos
        distance = gravity.magnitude()
        if distance > 25:
            distance = 25
        elif distance < 5:
            distance = 5
        grav_m = (graviton * self.mass * earth.mass) / (distance * distance)
        gravity.normalize()
        gravity = gravity * grav_m

        self.acceleration += gravity/self.mass
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration = self.acceleration*0
           
    def render(self):
        pygame.draw.circle(g.window, "grey", self.pos, self.mass, 0)
        pygame.draw.line(g.window, "green", self.pos, self.pos+self.velocity, 2)

g = Game()
earth = Planet(g.width/2, g.height/2)
pobjects = Objects()
graviton = 1

while g.run:

    g.input()
    g.window.fill('black')

    earth.update()
    earth.render()

    pobjects.update()
    pobjects.render()

    g.update()
    g.clock.tick(60)