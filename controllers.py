class Controllers_manager:
    def __init__(self, controllers_with_routes, start_route):
        self.controllers_with_routes = controllers_with_routes
        self.start_route = start_route


class Controller_base:
    def __init__(self):
        self.state = dict()
    
    def connect_state(self, state):
        self.state = state

    def update(self, events):
        pass

    def draw(self):
        pass