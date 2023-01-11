from components.component import Component
import customtkinter
from apps.github.menu_item import MenuItem
from apps.github.app import Github
import os


class Sidebar(Component):
    title = None
    sidebar = None
    row_count = 0

    def __init__(self, root):
        self.root = root

    @property
    def master(self):
        return self.root.master

    def create(self):
        self.master.geometry("900x700")
        self.master.rowconfigure(0, weight=1)
        self.sidebar = customtkinter.CTkFrame(master=self.master, fg_color="#181818")
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky='ns')
        self.add_title()
        self.create_sidebar_menu()
        self.add_logout()

    def add_title(self):
        self.title = customtkinter.CTkLabel(master=self.sidebar,
                                            text="Apps",
                                            font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title.grid(pady=20, row=0, column=0)
        self.row_count += 1

    def create_sidebar_menu(self):
        for index, item in enumerate(self.menu_items):
            row = index + 1
            button = customtkinter.CTkButton(master=self.sidebar, text=item.text, command=item.command)
            button.grid(pady=10, padx=10, row=row, column=0, sticky='n')
            self.sidebar.rowconfigure(row, weight=0)
            self.row_count += 1

    def add_logout(self):
        title = customtkinter.CTkButton(master=self.sidebar, text="Sign Out",
                                        font=customtkinter.CTkFont(size=10),
                                        command=self.logout)
        title.grid(pady=20, row=self.row_count, column=0, sticky='s')
        self.sidebar.rowconfigure(self.row_count, weight=1)

    def logout(self):
        try:
            os.remove(".env")
        except OSError:
            pass
        for frame in self.master.winfo_children():
            frame.destroy()
        self.root.draw_login_screen()

    @property
    def menu_items(self):
        apps = [MenuItem(text="Github", command=Github.initialize(self.root))]
        apps[0].command()
        return apps
