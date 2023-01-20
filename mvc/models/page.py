from events.event_manager import EventManager


class Page:
    PAGES = ['pending', 'open', 'complete']
    events = None

    def __init__(self):
        self.events = EventManager()

    def update(self, page: str):
        def _update(_event=None):
            for _page in Page.PAGES:
                if page != _page:
                    self.events.notify(event_type='github', key=f'{page}_prs', data=[], rerender=False)
            self.events.notify(event_type='github', key='page', data=page)
        return _update
