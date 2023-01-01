import customtkinter
import os
from dashboard import Dashboard
from dotenv import dotenv_values
import re


class Login:

    def __init__(self, root):
        self.root = root
        self.access_token_entry = None
        self.button = None
        self.checkbox = None
        self.frame = None

    @property
    def master(self):
        return self.root.master

    def draw(self):
        self.master.geometry("500x350")

        frame = customtkinter.CTkFrame(master=self.master)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = customtkinter.CTkLabel(master=frame, text="Login System")
        label.pack(pady=12, padx=10)

        self.access_token_entry = customtkinter.CTkEntry(master=frame, placeholder_text="Access Token", show="*")
        self.access_token_entry.pack(pady=12, padx=10)

        self.button = customtkinter.CTkButton(master=frame, text="Login", command=self.login)
        self.button.pack(pady=12, padx=10)

        self.checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
        self.checkbox.pack(pady=12, padx=10)
        self.frame = frame

    def login(self):
        self.save_credentials()
        self.frame.destroy()
        dashboard = Dashboard(root=self.root)
        dashboard.draw()

    def save_credentials(self) -> None:
        if not self.checkbox.get():
            return
        env_exists = os.path.exists(".env")
        if env_exists:
            values = dotenv_values(".env")
            token = values.get("ACCESS_TOKEN")
            if token:
                with open(".env", "r") as f:
                    contents = f.read()
                    modified_env = re.sub('ACCESS_TOKEN=[\w-]*[^\n]',
                                          f"ACCESS_TOKEN={self.access_token_entry.get()}",
                                          contents,
                                          flags=re.MULTILINE)
                self.write_credentials(modified_env)
            else:
                self.write_credentials(self.access_token_entry.get(), True)
        else:
            credentials = f"ACCESS_TOKEN={self.access_token_entry.get()}"
            self.write_credentials(credentials)

    def write_credentials(self, credentials: str, append: bool = False) -> None:
        if append:
            with open(".env", "a") as f:
                f.write(f"ACCESS_TOKEN={credentials}")
        else:
            with open(".env", "w") as f:
                f.write(credentials)
