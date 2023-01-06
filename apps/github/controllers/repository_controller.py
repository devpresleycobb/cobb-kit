from apps.github.models.repository import Repository
from apps.github.controllers.controller import Controller
from apps.github.views.view import View


class RepositoryController(Controller):

    @staticmethod
    def index():
        return Repository.all()

    @staticmethod
    def show(_id: int):
        return Repository(_id).get()

    @staticmethod
    def store(name_entry):
        def _store():
            name = name_entry.get()
            _id = Repository.create(name)
            View().render()
            return _id
        return _store

    @staticmethod
    def update(id: int, name: str):
        Repository.update(id, name)
        return Repository(id)

    @staticmethod
    def delete(id: int):
        Repository.delete(id)
        return {"message": "Organization deleted"}
