import customtkinter
from singleton import Singleton


class View(metaclass=Singleton):
    title = None
    organization_name = None
    add_button = None
    minus_button = None
    APP_NAME = "Github"
    initialized = False
    repositories = []
    frame = None

    def __init__(self, dependencies=None):
        self.dependencies = dependencies

    @property
    def master(self):
        return self.dependencies['master']

    @property
    def commands(self):
        return self.dependencies['commands']

    @property
    def data(self):
        return self.dependencies['data']

    def set_dependencies(self, dependencies):
        self.dependencies = dependencies

    @staticmethod
    def render(dependencies=None):
        view = View()
        if dependencies:
            view.set_dependencies(dependencies)
        if view.initialized:
            view.clear()
        view.frame = customtkinter.CTkFrame(master=view.master)
        view.frame.grid(row=0, column=1, sticky="nsew")
        view.master.grid_columnconfigure(1, weight=1)
        view.add_title()
        view.draw_repository_section()
        view.draw_pr_section()
        view.initialized = True

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
        no_prs_label.grid(pady=10, padx=20, row=2, column=2, sticky="nw")

    def add_pr_section_label(self):
        self.pr_section_label = customtkinter.CTkLabel(master=self.frame,
                                                       text="Pull Requests",
                                                       font=customtkinter.CTkFont(size=20,
                                                                                  weight="bold"))
        self.pr_section_label.grid(pady=10, padx=20, row=1, column=2, sticky="nw")

    def add_repository_section_label(self):
        self.repository_section_label = customtkinter.CTkLabel(master=self.frame,
                                                               text="Repositories",
                                                               font=customtkinter.CTkFont(size=20,
                                                                                          weight="bold"))
        self.repository_section_label.grid(pady=10, padx=20, row=1, column=0, sticky="nw")

    def clear(self):
        self.frame.destroy()
        self.initialized = False

    def add_title(self):
        self.title = customtkinter.CTkLabel(master=self.frame,
                                            text=self.APP_NAME,
                                            font=customtkinter.CTkFont(size=20,
                                                                       weight="bold"))
        self.title.grid(pady=20, padx=20, row=0, column=1, sticky="n")

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
        repositories = self.dependencies['commands']['show_repositories']()
        for index, repository in enumerate(repositories):
            name = repository[1]
            repository = customtkinter.CTkLabel(master=self.frame, text=name, cursor="pointinghand")
            repository.grid(pady=10, padx=20, sticky="nw", row=index + 4, column=0)
            repository.bind("<Button-1>", self.commands['show_prs'](name))
            self.repositories.append(repository)
