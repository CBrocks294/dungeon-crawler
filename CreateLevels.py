import pygame, random, time
class makeLvls():
	def __init__(self):
		self.Background = [[0 for y in range(40)] for x in range(30)]
		self.Pngs = []
		self.Pngs.append(pygame.image.load('back brick wall.png').convert())
		self.Pngs.append(pygame.image.load('lava.png').convert())
		self.Pngs.append(pygame.image.load('spikes.png').convert())
		self.Pngs[2].set_colorkey((255,255,255))  
		self.PlaceType = 1
	def placeBlocks(self,screen):
		pygame.event.get()
		MousePressed = pygame.mouse.get_pressed()
		KeyPressed = pygame.key.get_pressed()
		if KeyPressed[pygame.K_1]:
			self.PlaceType = 1
		elif KeyPressed[pygame.K_2]:
			self.PlaceType = 2
		if KeyPressed[pygame.K_3]:
			self.PlaceType = 3
		print(self.PlaceType)
		Loc = pygame.mouse.get_pos()
		wid = screen.get_width()
		hei = screen.get_height()

		if MousePressed[0]:
			if self.Background[int((Loc[1]/20)/hei*600)][int(Loc[0]/20/wid*800)] == 0:
				self.Background[int(Loc[1]/20/hei*600)][int(Loc[0]/20/wid*800)] = self.PlaceType
		elif MousePressed[2]:
			self.Background[int(Loc[1]/20/hei*600)][int(Loc[0]/20/wid*800)] = 0
	def drawBlocks(self,screen):
		wid = screen.get_width()
		hei = screen.get_height()
		for Y, YLst in enumerate(self.Background):
			for X, ItemType in enumerate(YLst):
				if ItemType != 0:
					screen.blit(pygame.transform.scale(self.Pngs[ItemType - 1],(int(21*wid/800), int(21*hei/600))),(int(X*20*wid/800),int(Y*20*hei/600)))

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
def main():
	pygame.init()
	screen=pygame.display.set_mode((800,600),pygame.RESIZABLE)
	done = False
	clock = pygame.time.Clock()
	Squares = makeLvls()
	Backing = backing()
	#define funtions/classes

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		if event.type == pygame.VIDEORESIZE:
			screen=pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
		screen.fill((0,0,0))
		
		Squares.placeBlocks(screen)
		Backing.drawBacking(screen)  
		Squares.drawBlocks(screen)  

		pygame.display.update()
		clock.tick(100)

	pygame.quit()

main()