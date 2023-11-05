import pygame
import random
import itertools

SPREAD_COMPRESSOR = 100

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

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.start_point = pygame.Vector2(pygame.mouse.get_pos())
                self.spawning = True

                print(self.start_point)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.spawning = False
                end_point = pygame.mouse.get_pos()
                power = (self.start_point - end_point) / 15
                pobjects.objects.append(
                    Asteroid(
                        self.start_point[0], self.start_point[1], power[0], power[1]
                    )
                )

                pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    planet.mass += 5
                    print(planet.mass)
                if event.key == pygame.K_s:
                    planet.mass -= 5
                    print(planet.mass)
                if event.key == pygame.K_r:
                    g.run = False
                    pobjects.objects = []

    def update(self):
        font_size = 40
        font = pygame.font.SysFont("Arial", font_size)

        num_asteroids = font.render(
            f"Number of asteroids: {len(pobjects.objects)}", True, "white"
        )
        num_asteroids_rect = num_asteroids.get_rect(center=(self.width / 2, 50))
        pygame.Surface.blit(self.window, num_asteroids, num_asteroids_rect)

        fps = font.render(f"FPS: {int(self.clock.get_fps())}", True, "white")
        fps_rect = fps.get_rect(center=(150, 50))
        pygame.Surface.blit(self.window, fps, fps_rect)
        pygame.display.update()

    def render(self):
        if self.spawning is True:
            pygame.draw.circle(g.window, "blue", self.start_point, 10, 0)
            pygame.draw.line(
                g.window, "blue", self.start_point, pygame.mouse.get_pos(), 2
            )


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
    def __init__(self, color="grey", mass=100):
        self.mass = mass
        self.velocity = 0
        self.color = color
        self.x = clamp(
            g.width / generateRandomPosition(),
            mass,
            g.width - mass,
        )
        self.y = clamp(
            g.height / generateRandomPosition(),
            mass,
            g.height - mass,
        )
        self.pos = pygame.Vector2(self.x, self.y)

    def update(self):
        self.pos = pygame.Vector2(self.x, self.y)

    def render(self):
        pygame.draw.circle(g.window, self.color, self.pos, self.mass / 2, 0)
        font_size = 40
        font = pygame.font.SysFont("Arial", font_size)
        text = font.render(str(self.mass), True, "white")
        text_rect = text.get_rect(center=(self.pos[0], self.pos[1]))
        pygame.Surface.blit(g.window, text, text_rect)


class Asteroid:
    def __init__(self, x, y, q=0, w=0, mass=10):
        self.mass = mass
        self.pos = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(q, w)
        self.acceleration = pygame.Vector2(0, 0)

    def update(self):
        gravity = planet.pos - self.pos
        distance = gravity.magnitude()

        if distance > 50:
            distance = 50
        elif distance < 25:
            distance = 25
        grav_m = (graviton * self.mass * planet.mass) / (distance * distance)
        gravity = gravity.normalize()
        gravity = gravity * grav_m

        self.acceleration += gravity / self.mass
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration = self.acceleration * 0

    def render(self):
        pygame.draw.circle(g.window, "grey", self.pos, self.mass, 0)
        pygame.draw.line(g.window, "green", self.pos, self.pos + self.velocity * 5, 2)


def generateRandomPosition():
    return round(random.uniform(1, 4), 2)


def generateRandomMass():
    return random.randrange(75, 200, 25)


def generateRandomColor():
    return (random.randrange(256), random.randrange(256), random.randrange(256))


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)


def setPlanets(num_planets):
    output_planets = []
    for i in range(num_planets):
        output_planets.append(
            Planet(
                color=generateRandomColor(),
                mass=generateRandomMass(),
            )
        )
    return output_planets


def arePlanetsTooClose(planets, spread_distance):
    for planet_a, planet_b in itertools.combinations(planets, 2):
        average_mass = (planet_a.mass + planet_b.mass) / 2
        if planet_a.pos.distance_to(planet_b.pos) < spread_distance + average_mass:
            return True


g = Game()
num_planets = 6
planets = setPlanets(num_planets)
pobjects = Objects()
graviton = 2

spread_distance = SPREAD_COMPRESSOR * (num_planets / max(1, num_planets - 1))

while g.run:
    g.input()
    g.window.fill("black")
    g.render()

    while arePlanetsTooClose(planets, spread_distance):
        planets = setPlanets(num_planets)

    for planet in planets:
        planet.update()
        planet.render()

        pobjects.update()
        pobjects.render()

    g.update()
    g.clock.tick(60)
    if g.run is False:
        planets = setPlanets(num_planets)
        g.run = True
