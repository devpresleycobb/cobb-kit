import customtkinter
import requests
from typing import List
from components.sidebar import Sidebar


class Dashboard:
    def __init__(self, root):
        self.root = root

    def draw(self):
        self.master.geometry("900x350")
        sidebar = Sidebar(root=self.root)
        sidebar.create()

    @property
    def master(self):
        return self.root.master

    def draw_dashboard(self):
        sidebar = Sidebar(root=self.root)
        sidebar.create()
