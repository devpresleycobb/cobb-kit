

class EnvKeyController:

    def __init__(self, env):
        self.env = env()

    def show(self, key):
        return self.env.get_key_by_name(key)

    def update(self, key, value):
        return self.env.set_key_by_name(key, value)
