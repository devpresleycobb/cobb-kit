import customtkinter


class Complete:

    commands = {}
    data = {}

    def __init__(self, view):
        self.state = view.state
        self.frame = view.frame

    @staticmethod
    def render(view):
        pr_section = Complete(view=view)
        pr_section.data = view.data
        pr_section.commands = view.commands
        pr_section.add_pr_section_label()
        pr_section.add_prs()

    def add_prs(self):
        for index, reviewer in enumerate(self.data.get('complete_prs', [])):
            pr = customtkinter.CTkLabel(master=self.frame, text=str(reviewer), cursor="pointinghand")
            pr.grid(pady=10, padx=20, sticky="nw", row=index + 4, column=2)
            pr.bind("<Button-1>", self.commands['visit_pr'](reviewer.pull_requests_url))
        if not self.data.get('complete_prs'):
            self.add_no_prs_label()

    def add_no_prs_label(self):
        no_prs_label = customtkinter.CTkLabel(master=self.frame,
                                              text="No completed requests",
                                              font=customtkinter.CTkFont(size=20,
                                                                         weight="bold"))
        no_prs_label.grid(pady=10, padx=20, row=2, column=2, sticky="nw")

    def add_pr_section_label(self):
        self.pr_section_label = customtkinter.CTkLabel(master=self.frame,
                                                       text="Complete Reviews",
                                                       font=customtkinter.CTkFont(size=20,
                                                                                  weight="bold"))
        self.pr_section_label.grid(pady=10, padx=20, row=1, column=2, sticky="nw")
