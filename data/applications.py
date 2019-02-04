"""
Applications generation.
"""
import random
from data import DEFAULT_APPLICATION_COUNT


class Applications(object):
    """
    Factory for generating applications.
    """

    def __init__(self, count=DEFAULT_APPLICATION_COUNT):
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.count:
            self.index = self.index + 1

            return {
                "application_id": random.randint(10 ** 6, 10 ** 7),
                "school_gpa": round(random.uniform(3.0, 4.0), 2),
                "has_alumni_parent": bool(random.random() > 0.8),
                "foreign_exchange_student": bool(random.random() > 0.9),
                "affirmative_action": bool(random.random() > 0.8),
                "gender": bool(random.random() > 0.5),
                "personal_statement_grade": round(random.uniform(2, 5), 1),
                "first_time_applicant": bool(random.random() > 0.2),
                "age": random.randint(20, 30)
            }
        else:
            raise StopIteration

    def next(self):
        """
        Next application, randomly generated.
        """
        return self.__next__()
