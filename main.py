import json, pygame, time
from os import execve
from random import choice, randint, uniform

width, height = json.load(open("./properties.json"))["window"]["width"], json.load(open("./properties.json"))["window"]["height"]




class firework:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.vector = [uniform(-4, 4), uniform(-6, -2)]
        self.color = choice(json.load(open("./properties.json"))["colors"])
        self.flytime = randint(110, 190)
        self.tail = []

    def draw(self, WIN):
        self.flytime -= 1
        if self.flytime < -40:
            return True
        if self.flytime > 0:
            before = self.pos
            self.pos[0] += self.vector[0] + randint(1,2)
            self.pos[1] += self.vector[1]
            self.tail.append([before, [self.pos[0], self.pos[1]], 40])
        for tail in self.tail:
            tail[2] -= 1
            if tail[2] < 0:
                continue
            pygame.draw.line(WIN, self.color, start_pos=tail[0], end_pos=tail[1], width=tail[2]//5)
        if self.flytime > 0:
            pygame.draw.circle(WIN, self.color, self.pos, radius=8, width=0)

class Paricles:
    def __init__(self, x, y, color):
        self.tail = []
        self.color = color
        self.pos = [x, y]
        self.vector = [uniform(-5, 5), uniform(-5, 10)]
        self.flytime = randint(50, 300)
    
    def draw(self, WIN):
        if self.vector[0] < 0:
            self.vector[0] += 1/50
        elif self.vector[0] > 0:
            self.vector[0] -= 1/50
        self.vector[1] += 1/50



        self.flytime -= 1
        if self.flytime < -40:
            return True
        if self.flytime > 0:
            before = self.pos
            self.pos[0] += self.vector[0]
            self.pos[1] += self.vector[1]
            self.tail.append([before, [self.pos[0], self.pos[1]], 20])
        for tail in self.tail:
            tail[2] -= 1
            if tail[2] < 0:
                continue
            pygame.draw.line(WIN, self.color, start_pos=tail[0], end_pos=tail[1], width=tail[2]//5)
        if self.flytime > 0:
            pygame.draw.circle(WIN, self.color, self.pos, radius=3, width=0)


fireworks = [firework(width//2, height)]
partices = []
WIN = pygame.display.set_mode()
while True:
    time.sleep(1/json.load(open("./properties.json"))["window"]["fps"])
    if randint(1, 500) == 5:
        fireworks.append(firework(width//2+randint(-100, 100), height))
    WIN.fill((0, 0, 0))
    for f in fireworks:
        if f.draw(WIN):
            for _ in range(0, randint(30, 60)):
                partices.append(Paricles(f.pos[0], f.pos[1], f.color))
            fireworks.remove(f)

    for p in partices:
        if p.draw(WIN):
            partices.remove(p)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        if e.type == pygame.MOUSEBUTTONUP:
            fireworks.append(firework(width//2+randint(-100, 100), height))

    pygame.display.update()



