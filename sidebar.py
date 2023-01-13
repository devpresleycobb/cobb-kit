from components.component import Component
import customtkinter
from apps.github.menu_item import MenuItem
from apps.github.app import Github
from apps.settings.app import Settings


class Sidebar(Component):
    title = None
    sidebar = None
    row_count = 0
    active_app = None
    apps = []

    def __init__(self, root):
        self.root = root

    @property
    def master(self):
        return self.root.master

    def create(self):
        self.master.rowconfigure(0, weight=1)
        self.sidebar = customtkinter.CTkFrame(master=self.master, fg_color="#181818")
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky='ns')
        self.add_title()
        self.set_menu_items()
        self.create_sidebar_menu()
        self.add_settings()

    def add_title(self):
        self.title = customtkinter.CTkLabel(master=self.sidebar,
                                            text="Apps",
                                            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title.grid(pady=20, row=0, column=0)
        self.row_count += 1

    def create_sidebar_menu(self):
        for index, app in enumerate(self.apps):
            row = index + 1
            button = customtkinter.CTkButton(master=self.sidebar, text=app.text, command=self.render(app))
            button.grid(pady=10, padx=10, row=row, column=0, sticky='n')
            self.sidebar.rowconfigure(row, weight=0)
            self.row_count += 1

    def render(self, app):
        def _render():
            if self.active_app:
                self.active_app.clear()
            self.active_app = app.command()
        return _render

    def add_settings(self):
        title = customtkinter.CTkButton(master=self.sidebar, text="Settings",
                                        font=customtkinter.CTkFont(size=10),
                                        command=self.go_to_settings)
        title.grid(pady=20, row=self.row_count, column=0, sticky='s')
        self.sidebar.rowconfigure(self.row_count, weight=1)

    def go_to_settings(self):
        self.active_app.clear()
        Settings.initialize(self.root)()


    def set_menu_items(self):
        self.apps = [MenuItem(text="Github", command=Github.initialize(self.root))]
        self.render(self.apps[0])()
