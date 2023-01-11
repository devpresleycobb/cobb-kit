from sidebar import Sidebar


class Dashboard:
    def __init__(self, root):
        self.root = root

    def draw(self):
        width = self.master.winfo_screenwidth()
        height = self.master.winfo_screenheight()
        self.master.geometry(f"{width}x{height}")
        sidebar = Sidebar(root=self.root)
        sidebar.create()

    @property
    def master(self):
        return self.root.master

    def draw_dashboard(self):
        sidebar = Sidebar(root=self.root)
        sidebar.create()
