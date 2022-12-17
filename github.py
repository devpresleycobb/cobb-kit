from dotenv import dotenv_values
import requests

class Github:
    BASE_URL = "https://api.github.com"

    @staticmethod
    def get_all_repos(org):
        values = dotenv_values(".env")
        access_token = values.get("ACCESS_TOKEN")
        url = f"{Github.BASE_URL}/orgs/{org}/repos"
        headers = {"Authorization": f"Bearer {access_token}"}

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return [repo['name'] for repo in response.json()]
