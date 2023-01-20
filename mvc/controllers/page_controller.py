class PageController:

    def __init__(self, page):
        self.page = page()

    def update(self, page: str):
        return self.page.update(page)
