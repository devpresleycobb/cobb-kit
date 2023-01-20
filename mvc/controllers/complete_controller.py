class CompleteController:

    def __init__(self, complete_prs):
        self.complete_prs = complete_prs()

    def show(self, name: str = None):
        return self.complete_prs.all(name=name)
