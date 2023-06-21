class Task:
    def __init__(self, title: str, note: str = None):
        self.title = title
        self.note = note
        self.is_done = False

    def add_note(self, note: str):
        self.note = note

    def done(self):
        self.is_done = True

    def __str__(self):
        result = (
            f'Title: {self.title}\n'
            f'Note: {self.note}\n'
            f'Status: {"Done" if self.is_done else "Not started"}\n'
        )
        return result
