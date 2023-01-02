from dotenv import dotenv_values
from requests import request, exceptions
from apps.github.reviewer import Reviewer


class API:

    BASE_URL = "https://api.github.com"

    @staticmethod
    def make_request(url, method="GET", data=None):
        try:
            access_token = dotenv_values(".env").get("ACCESS_TOKEN")
            headers = {"Authorization": f"Bearer {access_token}"}
            response = request(url=API.BASE_URL + url, method=method, headers=headers, data=data)
            response.raise_for_status()
            return response
        except exceptions.HTTPError as err:
            raise err

    @staticmethod
    def get_pull_requests(name):
        url = f"/repos/{name}/pulls"
        response = API.make_request(url=url)
        return response.json()
