import customtkinter


class Repositories:

    repository_section_label = None
    repository_name = None
    add_button = None
    delete_button = None
    repositories = []
    commands = {}
    data = {}

    def __init__(self, view):
        self.state = view.state
        self.frame = view.frame
        self.commands = view.state['commands']
        self.data = view.state['data']

    @staticmethod
    def render(view):
        partial = Repositories(view=view)
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
                                                  width=30,
                                                  fg_color='#4BB543',
                                                  hover_color='#35912F')
        self.add_button.grid(pady=10, padx=10, row=0, column=0, sticky="nw")

    def add_repositories(self):
        for index, repository in enumerate(self.data['repositories']):
            name = repository[1]
            _id = repository[0]
            self.delete_button = customtkinter.CTkButton(master=self.frame,
                                                         text="x",
                                                         command=self.commands['delete_repository'](_id),
                                                         width=30,
                                                         fg_color="#d0342c",
                                                         hover_color="#8b0000")
            repository = customtkinter.CTkLabel(master=self.frame, text=name, cursor="pointinghand")
            repository.grid(pady=10, padx=20, sticky="nw", row=index + 4, column=0)
            self.delete_button.grid(pady=10, padx=20, sticky="nw", row=index + 4, column=1)
            command = 'show_' + self.data['page']
            repository.bind("<Button-1>", self.commands[command](name))
            self.repositories.append(repository)
