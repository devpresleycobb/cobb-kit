import customtkinter
from dashboard import Dashboard
from login import Login
from dotenv import dotenv_values


class Root:

    @staticmethod
    def initialize():
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        root = customtkinter.CTk()
        login = Login(root=root)
        if dotenv_values().get("ACCESS_TOKEN"):
            dashboard = Dashboard(root=root)
            dashboard.draw_dashboard()
        else:
            login.draw_login_screen()
        root.mainloop()
