import customtkinter
from dashboard import Dashboard


class Root:

    __instance = None
    __master = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__master = customtkinter.CTk()
        self.__master.title("Cobb Kit")

    @property
    def master(self):
        return self.__master

    @staticmethod
    def initialize():
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        root = Root()
        dashboard = Dashboard(root=root)
        dashboard.draw()
        root.master.mainloop()
