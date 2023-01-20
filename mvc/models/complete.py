from apps.github.api import API
from apps.github.user import User
from events.event_manager import EventManager


class Complete:

    events = None

    def __init__(self):
        self.events = EventManager()

    def all(self, name: str = None):
        def _all(_event):
            prs = API.get_pull_requests(name)
            users = []
            for pull in prs:
                if pull['requested_reviewers'] == []:
                    users.append(User(username=pull['user']['login'],
                                      avatar_url=pull['user']['avatar_url'],
                                      profile_url=pull['user']['html_url'],
                                      pull_requests_url=pull['html_url']))
            self.events.notify(event_type='github', key='complete_prs', data=users)
        return _all
