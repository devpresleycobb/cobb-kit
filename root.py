import customtkinter
from dashboard import Dashboard
from login import Login
from dotenv import dotenv_values


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
        root.draw_login_screen = Login(root).draw
        if dotenv_values().get("ACCESS_TOKEN"):
            dashboard = Dashboard(root=root)
            dashboard.draw()
        else:
            login = Login(root=root)
            login.draw()
        root.master.mainloop()
