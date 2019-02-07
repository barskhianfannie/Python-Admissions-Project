"""
Admissions unit tests.
"""
import unittest
from data.applications import Applications
from school.admissions import get


class TestAdmissions(unittest.TestCase):
    """
    Tests for Admissions.
    """

    def test_get(self):
    #Check to make sure that only 36 total spots are being filled.
        applicants = Applications(1000)
        testing = get(applicants)
        self.assertEqual(len(testing), 36)
    #Check to make sure that first accepted applicant has alumni parent.
        alumni_parent_applicant = testing[0]
        self.assertTrue(alumni_parent_applicant)
    #Check to make sure that they are being sorted by weighted "total score".
        first_accepted = testing[0]
        second_accepted = testing[1]
        if first_accepted["total_score"] < second_accepted["total_score"]:
            raise ValueError
        else:
            print("The list is being sorted correctly")

    


if __name__ == "__main__":
    unittest.main()
