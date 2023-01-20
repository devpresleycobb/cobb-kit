import customtkinter

from mvc.views.baseview import BaseView
from singleton import singleton
from mvc.views.github.repositories import Repositories
from mvc.views.github.pending import Pending
from mvc.views.github.open import Open
from mvc.views.github.complete import Complete

from mvc.views.github.submenu import SubMenu
from events.event_listener import EventListener


@singleton
class View(BaseView, EventListener):
    title = None
    APP_NAME = "Github"
    initialized = False
    frame = None

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
        return "github"

    def render(self):
        view = View()
        if view.initialized:
            view.clear()
        view.add_title()
        self.render_pr_section()
        Repositories.render(view=view)
        SubMenu.render(view=view)
        view.initialized = True

    @property
    def sections(self):
        return {
            'pending': Pending,
            'open': Open,
            'complete': Complete
        }

    def render_pr_section(self):
        section = self.sections[self.data['page']]
        section.render(view=self)

    def add_title(self):
        self.title = customtkinter.CTkLabel(master=self.frame,
                                            text=self.APP_NAME,
                                            font=customtkinter.CTkFont(size=20,
                                                                       weight="bold"))
        self.title.grid(pady=20, padx=20, row=0, column=0, sticky="nw")
