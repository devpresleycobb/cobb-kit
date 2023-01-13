import customtkinter


class Github:

    PERSONAL_ACCESS_TOKEN_KEY = "GITHUB_PERSONAL_ACCESS_TOKEN"
    settings_section = None
    github_entry = None
    add_button = None

    def __init__(self, state, frame):
        self.state = state
        self.frame = frame

    @staticmethod
    def render(state, frame):
        github = Github(state=state, frame=frame)
        github.add_settings_section()

    def add_settings_section(self):
        self.add_github_label()
        self.add_github_stared_key()
        self.add_github_entry()
        self.add_github_button()

    def add_github_label(self):
        self.settings_section = customtkinter.CTkLabel(master=self.frame,
                                                       text="Github",
                                                       font=customtkinter.CTkFont(size=15,
                                                                                  weight="bold"))
        self.settings_section.grid(pady=20, padx=20, row=1, column=1, sticky="n")

    def add_github_entry(self):
        self.github_entry = customtkinter.CTkEntry(master=self.frame, show="*")
        self.github_entry.grid(pady=20, padx=20, row=1, column=2, sticky="n")

    def add_github_button(self):
        self.add_button = customtkinter.CTkButton(master=self.frame,
                                                  text="Add",
                                                  command=self.add_github_token)
        self.add_button.grid(pady=20, padx=20, row=1, column=3, sticky="n")

    def add_github_stared_key(self):
        access_token = self.state['commands'].get('get_env_by_name')(Github.PERSONAL_ACCESS_TOKEN_KEY)
        self.settings_section = customtkinter.CTkLabel(master=self.frame,
                                                       text='*' * len(access_token),
                                                       font=customtkinter.CTkFont(size=15,
                                                                                  weight="bold"))
        self.settings_section.grid(pady=20, padx=20, row=1, column=4, sticky="n")

    def add_github_token(self):
        entry = self.github_entry.get()
        self.state['commands'].get('set_env_by_name')(Github.PERSONAL_ACCESS_TOKEN_KEY, entry)
