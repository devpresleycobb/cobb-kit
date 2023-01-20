import customtkinter

from events.event_listener import EventListener
from singleton import singleton
from mvc.views.baseview import BaseView
from mvc.views.settings.github import Github


@singleton
class View(BaseView, EventListener):
    title = None
    APP_NAME = "Settings"
    initialized = False
    frame = None
    key_name = "GITHUB_PERSONAL_ACCESS_TOKEN"

    def __init__(self, state=None):
        self._state = state
        super().__init__()
        self.events.subscribe(self)

    def update(self, key, data, rerender=True):
        if data is not None:
            self.update_state(key=key, data=data)
        if rerender:
            self.render()

    @property
    def event_type(self):
        return "settings"

    def render(self):
        view = View()
        if view.initialized:
            view.clear()
        view.add_title()
        Github.render(state=view.state, frame=view.frame)
        view.initialized = True

    def add_title(self):
        self.title = customtkinter.CTkLabel(master=self.frame,
                                            text=self.APP_NAME,
                                            font=customtkinter.CTkFont(size=20,
                                                                       weight="bold"))
        self.title.grid(pady=20, padx=20, row=0, column=1, sticky="n")
