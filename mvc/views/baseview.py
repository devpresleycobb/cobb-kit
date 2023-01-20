import customtkinter
from events.event_manager import EventManager


class BaseView:

    frame = None
    initialized = False

    def __init__(self):
        self.events = EventManager()
        self.create_frame()

    def create_frame(self):
        self.frame = customtkinter.CTkFrame(master=self.state['master'])
        self.frame.grid(row=0, column=1, sticky="nsew")
        self.master.grid_columnconfigure(1, weight=1)

    @property
    def master(self):
        return self.state['master']

    @property
    def commands(self):
        return self.state['commands']

    @property
    def data(self):
        return self.state['data']

    @property
    def page(self):
        return self.state['page']

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    def update_state(self, key, data):
        state = self.state
        state['data'][key] = data
        self.state = state

    def clear(self):
        self.frame.destroy()
        self.create_frame()
        self.initialized = False
