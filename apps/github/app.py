from apps.app import Apps
from mvc.controllers.pending_review_controller import PendingReviewController
from mvc.views.github.view import View
from mvc.controllers.repository_controller import RepositoryController
from mvc.models.repository import Repository
import webbrowser


class Github(Apps):

    def __init__(self, root):
        self.root = root

    @property
    def master(self):
        return self.root.master

    @staticmethod
    def initialize(root):
        def github():
            _github = Github(root)
            return _github.draw_app()
        return github

    def draw_app(self):
        view = View(state=self.state)
        view.render()
        return view

    @property
    def state(self):
        repository_controller = RepositoryController(Repository)
        pending_review_controller = PendingReviewController()
        return {
            'master': self.master,
            'commands': {
                'save_repository': repository_controller.store,
                'delete_repository': repository_controller.delete,
                'show_repositories': repository_controller.index,
                'show_prs': pending_review_controller.show,
                'visit_pr': self.visit_pr
            },
            "data": {}
        }

    def visit_pr(self, link):
        def visit(_event):
            webbrowser.open(link)
        return visit
