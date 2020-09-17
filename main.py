import pygame, random, time

class player:
    def __init__(self):
        pass
    def move(self):
        pass
    def draw(self):
        pass


class wizard(player):
    def __init__(self):
        super().__init__()
    def attack(self):
        pass

class knight(player):
    def __init__(self):
        super().__init__()
    def attack(self):
        pass

class shield(player):
    def __init__(self):
        super().__init__()
        pass
    def attack(self):
        pass

def main():
    pygame.init()
    screen=pygame.display.set_mode((800,600),pygame.RESIZABLE)
    done = False
    clock = pygame.time.Clock()

    Charactors = [knight(), wizard(),shield()]

    CharactorLstPos = 0
    CurrentCharactor = Charactors[CharactorLstPos]

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.VIDEORESIZE:
                screen=pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
        screen.fill((0,0,0))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            if Changed == False:
                CharactorLstPos += 1
                if CharactorLstPos == 3: CharactorLstPos = 0
                CurrentCharactor = Charactors[CharactorLstPos]
                Changed = True  
        else:
            Changed = False
        print(CurrentCharactor.__class__.__name__)
        wid = screen.get_width()
        hei = screen.get_height()
        pygame.draw.rect(screen,(0,255,0),pygame.Rect(100*wid/800,10*hei/600,10*wid/800,100*hei/600))
        pygame.display.update()
        clock.tick(100)

    pygame.quit()

main()
