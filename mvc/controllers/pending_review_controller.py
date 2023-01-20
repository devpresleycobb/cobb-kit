class PendingReviewController:

    def __init__(self, pending_review):
        self.pending_review = pending_review()

    def show(self, name: str = None):
        return self.pending_review.all(name)
