import customtkinter
from singleton import Singleton
from apps.github.views.repository_section import RepositorySection
from apps.github.views.pr_section import PRSection


class View(metaclass=Singleton):
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
        view = View()
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

    @staticmethod
    def rerender(*args, **kwargs):
        if args and callable(args[0]):
            func = args[0]
            return View.render_wrapper()(func)
        update_key = kwargs.get('update')
        return View.render_wrapper(update_key=update_key)

    @staticmethod
    def render_wrapper(update_key=None):
        def decorator(func):
            def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                view = View()
                if update_key:
                    state = view.state
                    state['data'][update_key] = result
                    view.state = state
                    view.render()
                    return result
                view.render()
                return result
            return wrapper
        return decorator

    def clear(self):
        self.frame.destroy()
        self.initialized = False

    def add_title(self):
        self.title = customtkinter.CTkLabel(master=self.frame,
                                            text=self.APP_NAME,
                                            font=customtkinter.CTkFont(size=20,
                                                                       weight="bold"))
        self.title.grid(pady=20, padx=20, row=0, column=1, sticky="n")
