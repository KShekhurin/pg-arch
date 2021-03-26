import pygame
import sys
from controllers import Controllers_manager 

class Game_prefs:
    def __init__(self, size, name, fps):
        self.size = size
        self.name = name
        self.fps = fps

class Game:
    def __init__(self, preferences: Game_prefs, controllers_manager: Controllers_manager):
        self.state = dict() 
        self.state['route'] = controllers_manager.start_route
        self.state['stop'] = False

        self.controllers = controllers_manager.controllers_with_routes
        self.connect_state_to_controllers()

        self.preferences = preferences
        self.init_game()

    def connect_state_to_controllers(self):
        for route in self.controllers.keys():
            self.controllers[route].connect_state(self.state)

    def init_game(self):
        pygame.init()
        pygame.display.set_caption(self.preferences.name)
        self.screen = pygame.display.set_mode(self.preferences.size)
        self.clock = pygame.time.Clock()

    def check_special_events(self, events):
        for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    def start(self):
        while not self.state['stop']:
            self.clock.tick(self.preferences.fps)

            controller_route = self.state['route']

            events = pygame.event.get()
            self.check_special_events(events)

            self.controllers[controller_route].update(events)
            self.controllers[controller_route].draw()