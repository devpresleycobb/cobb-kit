import customtkinter


class SubMenu:

    title = None
    pending_reviews_button = None
    open_prs_button = None
    reviewed_prs_button = None
    local_frame = None

    def __init__(self, state, frame):
        self.state = state
        self.frame = frame

    @staticmethod
    def render(view):
        state = view.state
        frame = view.frame
        submenu = SubMenu(state, frame)
        submenu.local_frame = customtkinter.CTkFrame(master=frame, fg_color="transparent")
        submenu.local_frame.grid(row=0, column=2, sticky="sw")
        submenu.add_submenu()

    def add_submenu(self):
        self.add_pending_reviews_button()
        self.add_open_prs_button()
        self.add_reviewed_prs_button()

    def add_pending_reviews_button(self):
        self.pending_reviews_button = customtkinter.CTkButton(master=self.local_frame,
                                                              text="Pending",
                                                              command=self.state['commands']['pending']('pending'),
                                                              width=30)
        self.pending_reviews_button.grid(pady=10, padx=20, sticky="ws", row=0, column=0)

    def add_open_prs_button(self):
        self.open_prs_button = customtkinter.CTkButton(master=self.local_frame,
                                                       text="Open",
                                                       command=self.state['commands']['open']('open'),
                                                       width=30)
        self.open_prs_button.grid(pady=10, padx=20, sticky="ws", row=0, column=1)

    def add_reviewed_prs_button(self):
        self.reviewed_prs_button = customtkinter.CTkButton(master=self.local_frame,
                                                           text="Complete",
                                                           command=self.state['commands']['complete']('complete'),
                                                           width=30)
        self.reviewed_prs_button.grid(pady=10, padx=20, sticky="ws", row=0, column=2)
