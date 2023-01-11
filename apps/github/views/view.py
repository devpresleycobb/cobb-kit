import customtkinter
<<<<<<< Updated upstream:apps/github/view.py
from apps.github.repository_controller import RepositoryController
import tkinter
import tkinter.messagebox
import customtkinter

=======
from singleton import Singleton
from apps.github.views.repository_section import RepositorySection
from apps.github.views.pr_section import PRSection
>>>>>>> Stashed changes:apps/github/views/view.py

class View:

    title = None
    APP_NAME = "Github"
    initialized = False
<<<<<<< Updated upstream:apps/github/view.py
    repositories = []
    __view = None
    frame = None

    def __init__(self, dependencies):
        self.master = dependencies['master']
        self.commands = dependencies['commands']
        self.data = dependencies['data']

    @staticmethod
    def render(dependencies):
        view = View(dependencies)
=======
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
>>>>>>> Stashed changes:apps/github/views/view.py
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

<<<<<<< Updated upstream:apps/github/view.py
    def draw_repository_section(self):
        self.add_repository_section_label()
        self.add_repository_entry()
        self.add_repository_controls()
        self.add_repositories()

    def draw_pr_section(self):
        self.add_pr_section_label()
        self.add_prs()

    def add_prs(self):
        for index, reviewer in enumerate(self.data['reviewers']):
            pr = customtkinter.CTkLabel(master=self.frame, text=str(reviewer), cursor="pointinghand")
            pr.grid(pady=10, padx=20, sticky="nw", row=index + 4, column=2)
            pr.bind("<Button-1>", self.commands['visit_pr'](reviewer.pull_requests_url))
        if self.data['reviewers'] == []:
            self.add_no_prs_label()

    def add_no_prs_label(self):
        no_prs_label = customtkinter.CTkLabel(master=self.frame,
                                              text="No pull requests to review",
                                              font=customtkinter.CTkFont(size=20,
                                                                         weight="bold"))
        no_prs_label.grid(pady=10, padx=20, row=4, column=2, sticky="nw")

    def add_pr_section_label(self):
        self.pr_section_label = customtkinter.CTkLabel(master=self.frame,
                                                       text="Pull Requests",
                                                       font=customtkinter.CTkFont(size=20,
                                                                                  weight="bold"))
        self.pr_section_label.grid(pady=10, padx=20, row=1, column=2, sticky="nw")
=======
    @staticmethod
    def rerender(*args, **kwargs):
        if args and callable(args[0]):
            func = args[0]
            return View.render_wrapper()(func)
        update_key = kwargs.get('update')
        return View.render_wrapper(update_key=update_key)
>>>>>>> Stashed changes:apps/github/views/view.py

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
                                            text=View.APP_NAME,
                                            font=customtkinter.CTkFont(size=20,
                                                                       weight="bold"))
        self.title.grid(pady=20, padx=20, row=0, column=1, sticky="n")
<<<<<<< Updated upstream:apps/github/view.py

    def add_repository_entry(self):
        self.repository_name = customtkinter.CTkEntry(master=self.frame, placeholder_text="Name")
        self.repository_name.grid(padx=20, pady=10, row=2, column=0, sticky="w")

    def add_repository_controls(self):
        controls = customtkinter.CTkFrame(master=self.frame, fg_color="transparent")
        controls.grid(padx=10, sticky="nw", row=3, column=0)
        add_repository_command = self.commands['save_repository'](self.repository_name)
        self.add_button = customtkinter.CTkButton(master=controls,
                                                  text="+",
                                                  command=add_repository_command,
                                                  width=30)
        self.add_button.grid(pady=10, padx=10, row=0, column=0, sticky="nw")
        self.minus_button = customtkinter.CTkButton(master=controls,
                                                    text="-",
                                                    command=self.commands['delete_repository'](self.repository_name),
                                                    width=30)
        self.minus_button.grid(pady=10, padx=10, row=0, column=1, sticky="nw")

    def add_repositories(self):
        for index, repository in enumerate(RepositoryController.index()):
            name = repository[1]
            repository = customtkinter.CTkLabel(master=self.frame, text=name, cursor="pointinghand")
            repository.grid(pady=10, padx=20, sticky="nw", row=index + 4, column=0)
            repository.bind("<Button-1>", self.commands['show_prs'](name))
            self.repositories.append(repository)
=======
>>>>>>> Stashed changes:apps/github/views/view.py
