class Controller_base:
    def __init__(self):
        self.state = dict()
    
    def connect_state(self, state):
        self.state = state

    def update(self, events):
        pass

    def draw(self):
        pass