from apps.github.api import API
from events.event_manager import EventManager
from apps.github.user import User


class Pending:

    def __init__(self):
        self.events = EventManager()

    def all(self, name: str = None):
        def _all(_event):
            prs = API.get_pull_requests(name)
            reviewers = []
            for pull in prs:
                if pull['requested_reviewers']:
                    for reviewer in pull['requested_reviewers']:
                        reviewers.append(User(username=reviewer['login'],
                                              avatar_url=reviewer['avatar_url'],
                                              profile_url=reviewer['html_url'],
                                              pull_requests_url=pull['html_url']))
            self.events.notify(event_type='github', key='pending_prs', data=reviewers)
        return _all
