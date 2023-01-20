from apps.app import Apps
from mvc.controllers.page_controller import PageController
from mvc.controllers.pending_review_controller import PendingReviewController
from mvc.models.page import Page
from mvc.views.github.view import View
from mvc.controllers.repository_controller import RepositoryController
from mvc.controllers.complete_controller import CompleteController
from mvc.controllers.open_controller import OpenController
from mvc.models.open import Open
from mvc.models.pending import Pending
from mvc.models.complete import Complete
from mvc.models.repository import Repository
import webbrowser


class Github(Apps):

    DEFAULT_PAGE = 'pending'

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
        view = View(state=self.initial_state)
        view.render()
        return view

    @property
    def initial_state(self):
        repository_controller = RepositoryController(Repository)
        page_controller = PageController(Page)
        pending_review_controller = PendingReviewController(Pending)
        open_controller = OpenController(Open)
        complete_controller = CompleteController(Complete)
        return {
            'master': self.master,
            'commands': {
                'save_repository': repository_controller.store,
                'delete_repository': repository_controller.delete,
                'show_repositories': repository_controller.all,
                'pending': page_controller.update,
                'complete': page_controller.update,
                'open': page_controller.update,
                'show_pending': pending_review_controller.show,
                'show_open': open_controller.show,
                'show_complete': complete_controller.show,
                'visit_pr': self.visit_pr
            },
            "data": {
                'repositories': repository_controller.index(),
                'page': Github.DEFAULT_PAGE
            }
        }

    def visit_pr(self, link):
        def visit(_event):
            webbrowser.open(link)
        return visit
