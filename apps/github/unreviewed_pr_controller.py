from apps.github.api import API


class UnreviewedPRController:

    @staticmethod
    def show(name: str):
        return API.get_pull_requests(name)
