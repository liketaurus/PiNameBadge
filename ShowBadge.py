import pygame
from pygame.locals import *
pygame.init()

# size of the screen
WIDTH = 480
HEIGHT = 320
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN, 32)
img = pygame.image.load("Badge-Demo.PNG")

# scale picture to screem size
img = pygame.transform.scale(img, (WIDTH, HEIGHT))

# display image, but exit on 'ESC' key
running = True
while running:
        # events = pygame.event.get()
        for event in pygame.event.get():
            if event.type == QUIT:
		running = False
                pygame.quit()
                sys.exit()
	    elif event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			running = False
        windowSurface.blit(img, (0, 0))
        pygame.display.flip()