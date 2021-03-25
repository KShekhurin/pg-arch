import pygame
import sys


class Game_prefs:
    def __init__(self, size, frame_rate, name):
        self.size = size
        self.FPS = frame_rate
        self.name = name


class Game:
    def __init__(self, preferences: Game_prefs, controllers, start_route):
        self.state = dict() 
        self.state['route'] = start_route

        self.controllers = map(
            lambda controller: controller.connect_state(self.state),
            controllers
        )
        
        self.stop = False

        #I'll try to make it not depending on exactly pygame (in future)
        pygame.init()
        pygame.display.set_caption(self.name)
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
    
    def check_special_events(self, events):
        for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    def start(self):
        while not self.stop:
            self.clock.tick(self.FPS)

            controller_route = state['start_route']

            events = pygame.event.get()
            self.check_special_events(events)

            controllers[controller_route].update(events)
            controllers[controller_route].draw()

