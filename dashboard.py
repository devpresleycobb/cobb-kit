import customtkinter
import requests
from dotenv import dotenv_values
from reviewer import Reviewer
from typing import List
import webbrowser
from github import Github


class Dashboard:
    """
    This is one ugly class. I know. I'll refactor it later.
    """
    ORG_1 = dotenv_values(".env").get("ORG_1")
    ORG_2 = dotenv_values(".env").get("ORG_2")

    def __init__(self, root):
        self.root = root
        self.frame = None
        self.labels = []
        self.owner = Dashboard.ORG_1

    def set_org(self, org, frame):
        def combobox_callback(choice):
            print(choice)
            if choice == '--Select Repo--':
                return
            for label in self.labels:
                label.destroy()
            self.labels = []
            self.get_pull_requests(org, choice, frame)
        return combobox_callback

    def set_clearlink_org(self, org, frame):
        def entry_callback():
            for label in self.labels:
                label.destroy()
            self.labels = []
            choice = self.entry.get()
            self.get_pull_requests(org, choice, frame)
        return entry_callback

    def draw_dashboard(self):
        self.root.geometry("900x350")
        tabview = customtkinter.CTkTabview(master=self.root, width=900, height=900, fg_color="#1f1f1f")
        tabview.pack(padx=20, pady=20)

        tabview.add(Dashboard.ORG_1)
        tabview.add(Dashboard.ORG_2)
        tabview.set(Dashboard.ORG_1)

        frame = customtkinter.CTkFrame(master=tabview.tab(Dashboard.ORG_1))
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text=Dashboard.ORG_1)
        label.pack(pady=12, padx=10)

        combobox = customtkinter.CTkOptionMenu(master=frame,
                                               values=['--Select Repo--', *Github.get_all_repos(Dashboard.ORG_1)],
                                               command=self.set_org(org=Dashboard.ORG_1, frame=frame))
        combobox.pack(padx=20, pady=10)
        clearlink = customtkinter.CTkFrame(master=tabview.tab(Dashboard.ORG_2))
        clearlink.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=clearlink, text=Dashboard.ORG_2)
        label.pack(pady=12, padx=10)
        self.entry = customtkinter.CTkEntry(master=clearlink,
                                            placeholder_text="CTkEntry",
                                            width=120,
                                            height=25,
                                            border_width=2,
                                            corner_radius=10)
        self.entry.pack(padx=20, pady=10)
        button = customtkinter.CTkButton(master=clearlink, text="Find", command=self.set_clearlink_org(org=Dashboard.ORG_2, frame=clearlink))
        button.pack(pady=12, padx=10)
        self.frame = frame

    def callback(self, url):
        webbrowser.open_new_tab(url)

    def get_pull_requests(self, org, repo, frame):
        values = dotenv_values(".env")
        access_token = values.get("ACCESS_TOKEN")
        BASE_URL = "https://api.github.com"

        url = f"{BASE_URL}/repos/{org}/{repo}/pulls"
        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.get(url, headers=headers)

        data = response.json()

        reviewers: List[Reviewer] = []

        for pull in data:
            if pull['requested_reviewers']:
                for reviewer in pull['requested_reviewers']:
                    reviewers.append(Reviewer(username=reviewer['login'],
                                              avatar_url=reviewer['avatar_url'],
                                              profile_url=reviewer['html_url'],
                                              pull_requests_url=pull['html_url']))

        for reviewer in reviewers:
            label = customtkinter.CTkLabel(master=frame, text=str(reviewer))
            label.pack(pady=12, padx=10)
            label.bind(f"<Button-1>",
                       lambda e, url=reviewer.pull_requests_url: self.callback(url))
            self.labels.append(label)
