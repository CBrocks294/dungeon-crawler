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

class backing:
    def __init__(self):
        self.BackingImg = pygame.image.load('back brick wall.png').convert()
        self.BackingImg.set_colorkey((255,255,255))  
    def drawBacking(self,screen):
        wid = screen.get_width()
        hei = screen.get_height()
        ImgX = int(50*wid/800)
        ImgY = int(50*hei/600)
        for x in range(0,wid, ImgX):
            for y in range(0, hei,ImgY):
                screen.blit(pygame.transform.scale(self.BackingImg,(ImgX, ImgY)),(x,y))
        pygame.display.update()
        return screen

class mainClass:
    def __init__(self):
        pygame.init()
        screen=pygame.display.set_mode((800,600),pygame.RESIZABLE)
        done = False
        clock = pygame.time.Clock()
        Charactors = [knight(), wizard(),shield()]
        CharactorLstPos = 0
        CurrentCharactor = Charactors[CharactorLstPos]
        Changed = False
        Backing = backing()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            if event.type == pygame.VIDEORESIZE:
                screen=pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
           
            screen = Backing.drawBacking(screen)
            pressed = pygame.key.get_pressed()
            if [pygame.K_SPACE]:
                if Changed == False:
                    CharactorLstPos += 1
                    if CharactorLstPos == 3: CharactorLstPos = 0
                    CurrentCharactor = Charactors[CharactorLstPos]
                    Changed = True  
            else:
                Changed = False
            print(CurrentCharactor.__class__.__name__)
            #wid = screen.get_width()
            #hei = screen.get_height()
            #pygame.draw.rect(screen,(0,255,0),pygame.Rect(100*wid/800,10*hei/600,10*wid/800,100*hei/600))
            
            clock.tick(100)
            pygame.display.update()
            screen.fill((0,0,0))
        pygame.quit()



Main = mainClass()


