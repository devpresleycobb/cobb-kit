from apps.app import Apps
from apps.github.api import API
from apps.github.controllers.pending_review_controller import PendingReviewController
from apps.github.views.view import View
from apps.github.controllers.repository_controller import RepositoryController
from apps.github.models.repository import Repository
from apps.github.reviewer import Reviewer
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
            _github.draw_app()
        return github

    def draw_app(self):
        view = View(state=self.state)
        view.render()

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
