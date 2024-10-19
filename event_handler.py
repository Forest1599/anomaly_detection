# Event handler to exit out of the continious data stream
class EventHandler:
    def __init__(self) -> None:
        self.should_stop = False

    def on_key(self, event) -> None:
        if event.key == 'q':
            self.should_stop = True