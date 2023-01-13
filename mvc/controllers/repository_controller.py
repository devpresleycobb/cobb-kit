from mvc.views.github.view import View


class RepositoryController:

    def __init__(self, repository):
        self.repository = repository
        self.view = View

    def index(self):
        return self.repository.all()

    def store(self, name_entry):
        return self.repository.create(name_entry)

    def delete(self, _id: int):
        return self.repository.delete(_id)