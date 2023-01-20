from apps.app import Apps
from mvc.views.settings.view import View
from mvc.controllers.env_key_controller import EnvKeyController
from mvc.models.env import Env


class Settings(Apps):

    def __init__(self, root):
        self.root = root

    @property
    def master(self):
        return self.root.master

    @staticmethod
    def initialize(root):
        def github():
            _settings = Settings(root)
            return _settings.draw_app()
        return github

    def draw_app(self):
        view = View(state=self.state)
        view.render()
        return view

    @property
    def state(self):
        env_key_controller = EnvKeyController(Env)
        return {
            'master': self.master,
            'commands': {
                'get_env_by_name': env_key_controller.show,
                'set_env_by_name': env_key_controller.update
            },
            "data": {}
        }
