from db import get_tracker_data


def calculate_count(db, tracker):
    """
    Calculate the count of the counter.

    :param db: an initialized sqlite3 database connection
    :param tracker: name of the tracker present in db
    :return: length of the tracker increment events
    """
    data = get_tracker_data(db, tracker)
    return len(data)