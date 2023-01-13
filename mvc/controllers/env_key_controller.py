from mvc.models.env import Env


class EnvKeyController:

    def show(self, key):
        return Env.get_key_by_name(key)

    def update(self, key, value):
        Env.set_key_by_name(key, value)
