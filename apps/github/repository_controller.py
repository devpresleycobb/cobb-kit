from apps.github.repository import Repository
from apps.controller import Controller


class RepositoryController(Controller):

    @staticmethod
    def index():
        return Repository.all()

    @staticmethod
    def show(id: int):
        return Repository(id).get()

    @staticmethod
    def store(name: str):
        id = Repository.create(name)
        return Repository(id)

    @staticmethod
    def update(id: int, name: str):
        Repository.update(id, name)
        return Repository(id)

    @staticmethod
    def delete(id: int):
        Repository.delete(id)
        return {"message": "Organization deleted"}
