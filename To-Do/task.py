class Task:
    def __init__(self, title: str, note: str = None):
        self.title = title
        self.note = note
        self.is_done = False

    def add_note(self, note: str):
        self.note = note

    def done(self):
        self.is_done = True

