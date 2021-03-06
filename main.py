import pygame, random, time

class player:
    def __init__(self):
        self.Velocity = [0,0]
        self.Y = 300
        self.Grounded = True
        self.FacingRight = True
        self.Attacked = False
    def move(self,screen):
        pygame.event.get()
        Pressed = pygame.key.get_pressed()
        if Pressed[pygame.K_w] and self.Grounded == True:
            self.Velocity[1] -= 50
            self.Grounded = False
        if Pressed[pygame.K_a] and self.Velocity[0] >= -30:
            self.Velocity[0] -= 1
            self.FacingRight = False
        if Pressed[pygame.K_d] and self.Velocity[0] <= 30:
            self.Velocity[0] += 1
            self.FacingRight = True
        if Pressed[pygame.K_s]:
            if not self.Attacked:
                self.attack(screen)
                self.Attacked = True
        else: self.Attacked = False

    def VeloCalcs(self):
        if (self.Velocity[0] <= 0.25 and self.Velocity[0]>= -0.25):
            self.Velocity[0] = 0
        elif self.Velocity[0] > 0:
            self.Velocity[0] -= 0.75
        elif self.Velocity[0] < 0:
            self.Velocity[0] += 0.75
        #gravity
        self.Velocity[1] += 2
        #checks for collitions
        if (self.X >= 770 and self.Velocity[0] > 0) or (self.X <= -10 and self.Velocity[0] < 0):
            self.Velocity[0] = 0
        if self.Y >= 560 and self.Velocity[1] > 0:
            self.Velocity[1] = 0
            self.Y = 560
            self.Grounded = True
            

        #adds momentum
        self.X += self.Velocity[0]/10
        self.Y += self.Velocity[1]/10
    

    def draw(self,screen):
        if (self.__class__.__name__ ==  'wizard'):
            if len(self.Attacks) > 0:
                for SpellLstPos, Spells in enumerate(self.Attacks):
                    Spells.spellMove()
                    Spells.drawSpells(screen)
                    if Spells.Collided:
                        self.Attacks.pop(SpellLstPos)
        wid = screen.get_width()
        hei = screen.get_height()
        ImgX = int(40*wid/800)
        ImgY = int(40*hei/600)
        screen.blit(pygame.transform.scale(pygame.transform.flip(self.CharImg, self.FacingRight,False),(ImgX, ImgY)),((self.X*wid/800),(self.Y*hei/600)))
        
class wizardSpell():
    def __init__(self, Right, X, Y,screen):
        self.X = X+30 if Right else X
        hei = screen.get_height()
        self.Y = (Y+20)*hei/600
        self.MovingRight = Right
        self.SpellImg = pygame.image.load('wizard spell.png').convert()
        self.SpellImg.set_colorkey((255,255,255))
        self.Collided = False
    def spellMove(self):
        if self.MovingRight: self.X += 4
        else: self.X -= 4
        if self.X > 800 or self.X < -10:
            self.Collided = True
    def drawSpells(self,screen):
        wid = screen.get_width()
        hei = screen.get_height()
        ImgX = int(10*wid/800)
        ImgY = int(10*hei/600)
        screen.blit(pygame.transform.scale(pygame.transform.flip(self.SpellImg, self.MovingRight,False),(ImgX, ImgY)),(self.X*wid/800,self.Y))


class wizard(player):
    def __init__(self):
        super().__init__()
        self.X = 50
        self.CharImg = pygame.image.load('wizard.png').convert()
        self.CharImg.set_colorkey((255,255,255))  
        self.Attacks = []

    def attack(self,screen):
        if len(self.Attacks) <= 5:
            self.Attacks.append(wizardSpell(self.FacingRight, self.X, self.Y,screen))

class knight(player):
    def __init__(self):
        self.X = 150
        super().__init__()
        self.CharImg = pygame.image.load('knight.png').convert()
        self.CharImg.set_colorkey((255,255,255))  
    def attack(self,screen):
        pass


class shield(player):
    def __init__(self):
        super().__init__()
        self.X = 100
        self.CharImg = pygame.image.load('shield.png').convert()
        self.CharImg.set_colorkey((255,255,255))  
    def attack(self, attack):
        pass

class backing:
    def __init__(self):
        self.BackingImg = pygame.image.load('new backing wall.png').convert()
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
        Charactors = [knight(),shield(), wizard()]
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
            wid = screen.get_width()
            hei = screen.get_height()
            if Pressed[pygame.K_SPACE]:
                if Changed == False:
                    CharactorLstPos += 1
                    if CharactorLstPos == 3: CharactorLstPos = 0
                    CurrentCharactor = Charactors[CharactorLstPos]
                    Changed = True  
            else:
                Changed = False
            CurrentCharactor.move(screen)
            for Char in (Charactors):
                Char.draw(screen)
                Char.VeloCalcs()
            clock.tick(100)
            pygame.display.update()
            screen.fill((0,0,0))
        pygame.quit()

Main = mainClass()