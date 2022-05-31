import pygame, random

pygame.init()

gameDisplay = pygame.display.set_mode((1000, 600))
farg = (255, 255, 255)

poang = 0

x, y = 0, 0
hastighet = 2

skott = False
skottx, skotty = 0, 0

def skriv(text, tx=0, ty=0, storlek=50, farg=(0, 0, 0)):
    font = pygame.font.SysFont(None, storlek)
    txt = font.render(text, True, farg)
    gameDisplay.blit(txt, (tx, ty))


class monster:
    def __init__(self, x, y, farg):
        self.x, self.y = x, y
        self.farg = farg

    def rita(self):
        pygame.draw.rect(gameDisplay, self.farg, (self.x, self.y, 50, 50))

    def ga(self):
        if self.x < x:
            self.x += random.randrange(5, 10) / 10
        if self.x > x:
            self.x -= random.randrange(5, 10) / 10
        if self.y < y:
            self.y += random.randrange(5, 10) / 10
        if self.y > y:
            self.y -= random.randrange(5, 10) / 10

        self.x += random.randint(-18, 18) / 10
        self.y += random.randint(-18, 18) / 10
    def spelare_dog(self):
        print(self.x, x, self.y, y)
        if x < self.x < x + 50 and y < self.y < y + 50:
            return True
        else:
            return False


monsters = 5

for n in range(0, monsters):
    globals()["monster" + str(n)] = monster(random.randint(-500, 1500), random.randint(-500, 1100), (255, 0, 0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            farg = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= hastighet
        hall = 0
    if keys[pygame.K_RIGHT]:
        x += hastighet
        hall = 1
    if keys[pygame.K_UP]:
        y -= hastighet
        hall = 2
    if keys[pygame.K_DOWN]:
        y += hastighet
        hall = 3

    if x > 950:
        x = 950
    if x < 0:
        x = 0
    if y > 550:
        y = 550
    if y < 0:
        y = 0

    if not skott and keys[pygame.K_SPACE]:
        skott = True
        skottx, skotty = x, y
        hallda = hall

    if skott:
        if hallda == 0:
            skottx -= 3
        if hallda == 1:
            skottx += 3
        if hallda == 2:
            skotty -= 3
        if hallda == 3:
            skotty += 3

        if skottx > 1000 or skottx < 0 or skotty > 600 or skotty < 0:
            skott = False

        for n in range(0, monsters):
            m = globals()["monster" + str(n)]
            if m.x + 50 > skottx > m.x and m.y + 50 > skotty > m.y:
                globals()["monster" + str(n)].x = random.randint(-500, 1500)
                globals()["monster" + str(n)].y = random.randint(-500, 1100)
                poang += 1

    gameDisplay.fill(farg)

    if skott:
        pygame.draw.rect(gameDisplay, (0, 0, 0), (skottx, skotty, 10, 10))

    pygame.draw.rect(gameDisplay, (0, 0, 0), (x, y, 50, 50))

    for n in range(0, monsters):
        globals()["monster" + str(n)].ga()
        globals()["monster" + str(n)].rita()
        if globals()["monster" + str(n)].spelare_dog():
            highscore = 0
            try:
                fil = open(".highscore", "r")
                highscore = int(fil.read())
                fil.close()
            except:
                pass

            extra = "High score är " + str(highscore) + "."

            if poang > highscore:
                extra = "Du fick highscore!"
                fil = open(".highscore", "w")
                fil.write(str(poang))
                fil.close()


            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                skriv("DU DOG!!! Du fick " + str(poang) + " poäng." + extra, 50, 100, 60)
                pygame.display.update()

    skriv("Poäng: " + str(poang), 0, 0)

    pygame.display.update()
