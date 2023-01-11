<<<<<<< Updated upstream
from menu_item import MenuItem
from database import Database
from app import Apps
import customtkinter
from apps.github.api import API
from apps.github.view import View
from apps.github.repository_controller import RepositoryController
from apps.github.repository import Repository
from apps.github.unreviewed_pr_controller import UnreviewedPRController
from typing import List
from apps.github.reviewer import Reviewer
=======
from apps.app import Apps
from apps.github.controllers.pending_review_controller import PendingReviewController
from apps.github.views.view import View
from apps.github.controllers.repository_controller import RepositoryController
from apps.github.models.repository import Repository
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
        View.render(dependencies=self.dependencies)
=======
        view = View(state=self.state)
        view.render()
>>>>>>> Stashed changes

    @property
    def state(self):
        repository_controller = RepositoryController(Repository)
        pending_review_controller = PendingReviewController()
        return {
            'master': self.master,
            'commands': {
<<<<<<< Updated upstream
                'save_repository': self.save_repository,
                'delete_repository': self.delete_repository,
                'show_prs': self.show_prs,
=======
                'save_repository': repository_controller.store,
                'delete_repository': repository_controller.delete,
                'show_repositories': repository_controller.index,
                'show_prs': pending_review_controller.show,
>>>>>>> Stashed changes
                'visit_pr': self.visit_pr
            },
            "data": {}
        }

<<<<<<< Updated upstream
    def save_repository(self, name_entry):
        def save():
            name = name_entry.get()
            RepositoryController.store(name)
            View.render(self.dependencies)
        return save

    def delete_repository(self, name_entry):
        def delete():
            name = name_entry.get()
            id = Repository.get_id_from_name(name)
            RepositoryController.delete(id[0])
            View.render(self.dependencies)
        return delete

    def show_prs(self, name):
        def show(_event):
            prs = API.get_pull_requests(name)
            self.reviewers = []
            for pull in prs:
                if pull['requested_reviewers']:
                    for reviewer in pull['requested_reviewers']:
                        self.reviewers.append(Reviewer(username=reviewer['login'],
                                                       avatar_url=reviewer['avatar_url'],
                                                       profile_url=reviewer['html_url'],
                                                       pull_requests_url=pull['html_url']))
            View.render(self.dependencies)
        return show

=======
>>>>>>> Stashed changes
    def visit_pr(self, link):
        def visit(_event):
            webbrowser.open(link)
        return visit
