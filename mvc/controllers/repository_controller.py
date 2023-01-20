class RepositoryController:

    def __init__(self, repository):
        self.repository = repository()

    def index(self):
        return self.repository.index()

    def all(self):
        return self.repository.all()

    def store(self, name_entry):
        return self.repository.create(name_entry)

    def delete(self, _id: int):
        return self.repository.delete(_id)
