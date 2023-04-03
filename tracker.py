from db import add_tracker, increment_tracker


class Tracker:

    def __init__(self, name: str, description: str):
        """Tracker class, to count events

        :param name: the name of the tracker
        :param description: the description of the tracker
        """
        self.name = name
        self.description = description
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def __str__(self):
        return f"{self.name}: {self.count}"

    def store(self, db):
        add_tracker(db, self.name, self.description)

    def add_event(self, db, date: str = None):
        increment_tracker(db, self.name, date)