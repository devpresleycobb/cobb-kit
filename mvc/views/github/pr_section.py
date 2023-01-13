import customtkinter


class PRSection:

    commands = {}
    data = {}

    def __init__(self, state, frame):
        self.state = state
        self.frame = frame

    @staticmethod
    def render(state, frame):
        pr_section = PRSection(state, frame)
        pr_section.data = state['data']
        pr_section.commands = state['commands']
        pr_section.add_pr_section_label()
        pr_section.add_prs()

    def add_prs(self):
        for index, reviewer in enumerate(self.data.get('pending_reviews', [])):
            pr = customtkinter.CTkLabel(master=self.frame, text=str(reviewer), cursor="pointinghand")
            pr.grid(pady=10, padx=20, sticky="nw", row=index + 4, column=2)
            pr.bind("<Button-1>", self.commands['visit_pr'](reviewer.pull_requests_url))
        if not self.data.get('pending_reviews'):
            self.add_no_prs_label()

    def add_no_prs_label(self):
        no_prs_label = customtkinter.CTkLabel(master=self.frame,
                                              text="No pull requests to review",
                                              font=customtkinter.CTkFont(size=20,
                                                                         weight="bold"))
        no_prs_label.grid(pady=10, padx=20, row=2, column=2, sticky="nw")

    def add_pr_section_label(self):
        self.pr_section_label = customtkinter.CTkLabel(master=self.frame,
                                                       text="Pending Reviews",
                                                       font=customtkinter.CTkFont(size=20,
                                                                                  weight="bold"))
        self.pr_section_label.grid(pady=10, padx=20, row=1, column=2, sticky="nw")
