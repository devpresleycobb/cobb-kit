from dataclasses import dataclass


@dataclass
class Reviewer:
    username: str
    avatar_url: str
    profile_url: str
    pull_requests_url: str

    def __str__(self):
        return f"{self.username} - {self.pull_requests_url}"
