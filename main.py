import pygame, random, time

class player:
    def __init__(self):
        self.Velocity = [0,0]
        self.X = 100
        self.Y = 300
        self.Grounded = False
        self.FacingRight = True
    def move(self):
        pygame.event.get()
        Pressed = pygame.key.get_pressed()
        if Pressed[pygame.K_w]:
            self.Velocity[1] -= 1
        if Pressed[pygame.K_a] and self.Velocity[1] >= -5:
            self.Velocity[0] -= 1
            self.FacingRight = False
        if Pressed[pygame.K_d] and self.Velocity[1] <= 5:
            self.Velocity[0] += 1
            self.FacingRight = True

        if self.Velocity[0] > 0:
            self.Velocity[0] -= 0.5
        elif self.Velocity[0] < 0:
            self.Velocity[0] += 0.5

        self.X += self.Velocity[0]/5
        self.Y += self.Velocity[1]/5


    def draw(self,screen):
        wid = screen.get_width()
        hei = screen.get_height()
        ImgX = int(60*wid/800)
        ImgY = int(60*hei/600)
        screen.blit(pygame.transform.scale(pygame.transform.flip(self.CharImg, self.FacingRight,False),(ImgX, ImgY)),(self.X,self.Y))
        


class wizard(player):
    def __init__(self):
        super().__init__()
        self.CharImg = pygame.image.load('wizard.png').convert()
        self.CharImg.set_colorkey((255,255,255))  

    def attack(self):
        pass

class knight(player):
    def __init__(self):
        super().__init__()
        self.CharImg = pygame.image.load('knight.png').convert()
        self.CharImg.set_colorkey((255,255,255))  
    def attack(self):
        pass


class shield(player):
    def __init__(self):
        super().__init__()
        self.CharImg = pygame.image.load('shield.png').convert()
        self.CharImg.set_colorkey((255,255,255))  
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
           
            Backing.drawBacking(screen)
            Pressed = pygame.key.get_pressed()
            if Pressed[pygame.K_SPACE]:
                print('space')
                if Changed == False:
                    CharactorLstPos += 1
                    if CharactorLstPos == 3: CharactorLstPos = 0
                    CurrentCharactor = Charactors[CharactorLstPos]
                    Changed = True  
            else:
                Changed = False
            CurrentCharactor.move()
            for Char in (Charactors):
                Char.draw(screen)

            #wid = screen.get_width()
            #hei = screen.get_height()
            #pygame.draw.rect(screen,(0,255,0),pygame.Rect(100*wid/800,10*hei/600,10*wid/800,100*hei/600))
            
            clock.tick(100)
            pygame.display.update()
            screen.fill((0,0,0))
        pygame.quit()



Main = mainClass()


