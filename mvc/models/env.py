from dotenv import dotenv_values, set_key
from mvc.views.settings.view import View


class Env:

    @staticmethod
    def get_key_by_name(name):
        return dotenv_values(".env").get(name)

    @staticmethod
    @View.rerender(update='access_token')
    def set_key_by_name(name, value):
        set_key(".env", name, value)
