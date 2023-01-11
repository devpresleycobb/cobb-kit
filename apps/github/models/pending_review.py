from apps.github.api import API
from apps.github.views.view import View
from apps.github.reviewer import Reviewer


class PendingReview:

    @staticmethod
    def all(name):
        @View.rerender(update='pending_reviews')
        def _all(_event):
            prs = API.get_pull_requests(name)
            reviewers = []
            for pull in prs:
                if pull['requested_reviewers']:
                    for reviewer in pull['requested_reviewers']:
                        reviewers.append(Reviewer(username=reviewer['login'],
                                                  avatar_url=reviewer['avatar_url'],
                                                  profile_url=reviewer['html_url'],
                                                  pull_requests_url=pull['html_url']))
            return reviewers
        return _all
