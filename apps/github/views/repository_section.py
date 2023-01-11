import customtkinter


class RepositorySection:

    repository_section_label = None
    repository_name = None
    add_button = None
    delete_button = None
    repositories = []
    commands = {}
    data = {}

    def __init__(self, state, frame):
        self.state = state
        self.frame = frame

    @staticmethod
    def render(state, frame):
        partial = RepositorySection(state=state, frame=frame)
        partial.commands = state['commands']
        partial.data = state['data']
        partial.add_repository_section_label()
        partial.add_repository_entry()
        partial.add_repository_controls()
        partial.add_repositories()

    def add_repository_section_label(self):
        self.repository_section_label = customtkinter.CTkLabel(master=self.frame,
                                                               text="Repositories",
                                                               font=customtkinter.CTkFont(size=20,
                                                                                          weight="bold"))
        self.repository_section_label.grid(pady=10, padx=20, row=1, column=0, sticky="nw")

    def add_repository_entry(self):
        self.repository_name = customtkinter.CTkEntry(master=self.frame, placeholder_text="Name")
        self.repository_name.grid(padx=20, pady=10, row=2, column=0, sticky="w")

    def add_repository_controls(self):
        controls = customtkinter.CTkFrame(master=self.frame, fg_color="transparent")
        controls.grid(padx=10, sticky="nw", row=2, column=1)
        add_repository_command = self.commands['save_repository'](self.repository_name)
        self.add_button = customtkinter.CTkButton(master=controls,
                                                  text="+",
                                                  command=add_repository_command,
                                                  width=30)
        self.add_button.grid(pady=10, padx=10, row=0, column=0, sticky="nw")

    def add_repositories(self):
        repositories = self.state['commands']['show_repositories']()
        for index, repository in enumerate(repositories):
            name = repository[1]
            _id = repository[0]
            self.delete_button = customtkinter.CTkButton(master=self.frame,
                                                         text="x",
                                                         command=self.commands['delete_repository'](_id),
                                                         width=30)
            repository = customtkinter.CTkLabel(master=self.frame, text=name, cursor="pointinghand")
            repository.grid(pady=10, padx=20, sticky="nw", row=index + 4, column=0)
            self.delete_button.grid(pady=10, padx=20, sticky="nw", row=index + 4, column=1)
            repository.bind("<Button-1>", self.commands['show_prs'](name))
            self.repositories.append(repository)
