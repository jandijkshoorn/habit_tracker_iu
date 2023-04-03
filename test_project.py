from tracker import Tracker
from db import get_db, add_tracker, increment_tracker, get_tracker_data
from analyse import calculate_count

class TestTracker:

    def setup_method(self):
        self.db = get_db("test.db")

        add_tracker(self.db, "test_tracker", "test_description")
        increment_tracker(self.db, "test_tracker", "2023-12-06")
        increment_tracker(self.db, "test_tracker", "2023-12-07")

        increment_tracker(self.db, "test_tracker", "2023-12-08")
        increment_tracker(self.db, "test_tracker", "2023-12-09")

    def test_tracker(self):
        tracker = Tracker("test_tracker_1", "test_description_1")
        tracker.store(self.db)

        tracker.increment()
        tracker.add_event(self.db)
        tracker.reset()
        tracker.increment()

    def test_db_tracker(self):
        data = get_tracker_data(self.db, "test_tracker")
        assert len(data)  == 4

        count = calculate_count(self.db, "test_tracker")
        assert count == 4

    def teardown_method(self):
        import os
        os.remove("test.db")