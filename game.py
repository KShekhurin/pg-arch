import pygame
import sys

class Game:
    def __init__(self, size, frame_rate, name):
        self.stop = False
        self.size = size
        self.FPS = frame_rate
        self.name = name
        self.objects = []
        
        self.state = dict() 
        
        pygame.init()
        pygame.display.set_caption(self.name)
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
    
    def check_special_events(self, events):
        for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def update(self, events):
        for obj in self.objects:
            obj.update(events)
    
    def draw(self):
        for obj in self.objects:
            obj.draw(self.screen)
    
    def start(self):
        while not self.stop:
            self.clock.tick(self.FPS)
            self.screen.fill((0, 0, 0))

            events = pygame.event.get()

            self.check_special_events(events)
            self.update(events)
            self.draw()

