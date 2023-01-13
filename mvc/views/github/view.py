import customtkinter
from mvc.views.baseview import BaseView
from singleton import Singleton
from mvc.views.github.repository_section import RepositorySection
from mvc.views.github.pr_section import PRSection


class View(BaseView, metaclass=Singleton):
    title = None
    APP_NAME = "Github"
    initialized = False
    frame = None

    def __init__(self, state=None):
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    def render(self):
        view = BaseView.get_view(view=View)
        if view.initialized:
            view.clear()
        master = view.state['master']
        view.frame = customtkinter.CTkFrame(master=master)
        view.frame.grid(row=0, column=1, sticky="nsew")
        master.grid_columnconfigure(1, weight=1)
        view.add_title()
        RepositorySection.render(state=view.state, frame=view.frame)
        PRSection.render(state=view.state, frame=view.frame)
        view.initialized = True

    def clear(self):
        self.frame.destroy()
        self.initialized = False

    def add_title(self):
        self.title = customtkinter.CTkLabel(master=self.frame,
                                            text=self.APP_NAME,
                                            font=customtkinter.CTkFont(size=20,
                                                                       weight="bold"))
        self.title.grid(pady=20, padx=20, row=0, column=1, sticky="n")
