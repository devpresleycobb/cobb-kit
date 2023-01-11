from apps.github.models.pending_review import PendingReview


class PendingReviewController:

    def __init__(self, pending_review=PendingReview):
        self.pending_review = pending_review

    def show(self, name: str):
        return self.pending_review.all(name)
