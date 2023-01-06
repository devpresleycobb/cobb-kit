from abc import ABC

from apps.github.api import API
from apps.github.controllers.controller import Controller


class UnreviewedPRController(Controller, ABC):

    @staticmethod
    def show(name: str):
        return API.get_pull_requests(name)
