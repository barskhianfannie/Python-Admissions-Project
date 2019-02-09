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

    def setUp(self):
        applications = Applications(1000)
        self.apps =get(applications)


    def test_admitted_spots(self):
        """
        Check to make sure that only 30 admitted spots are being filled.
        """
        admitted = self.apps[0]
        self.assertEqual(len(admitted), 30)

    def test_waitlisted_spots(self):
        """
        Check to make sure that only 6 waitlisted spots are being filled.
        """
        waitlisted = self.apps[1]
        self.assertEqual(len(waitlisted), 6)
    
    def test_weighted_logic(self):
        """
        Check the top / middle / and bottom applicant total weighted scores to make 
        make sure applicants are being chosen and sorted correctly.
        """
        top_applicant = self.apps[0][0]
        middle_applicant = self.apps[0][14]
        bottom_applicant = self.apps[0][29]
        top_score = (top_applicant["personal_statement_grade"] * 0.8) + top_applicant["school_gpa"]
        middle_applicant_score = (middle_applicant["personal_statement_grade"] * 0.8) + middle_applicant["school_gpa"]
        last_applicant_score = (bottom_applicant["personal_statement_grade"] * 0.8) + bottom_applicant["school_gpa"]
        self.assertGreater(top_score, middle_applicant_score)
        self.assertGreater(middle_applicant_score, last_applicant_score)

    def test_waitlisted_weighted_logic(self):
        """
        Check the top / middle / and bottom waitlisted applicant total weighted scores to make 
        make sure applicants are being chosen and sorted correctly.
        """
        top_waitlisted = self.apps[1][0]
        middle_waitlisted = self.apps[1][2]
        bottom_waitlisted = self.apps[1][5]
        top_score = (top_waitlisted["personal_statement_grade"] * 0.8) + top_waitlisted["school_gpa"]
        middle_applicant_score = (middle_waitlisted["personal_statement_grade"] * 0.8) + middle_waitlisted["school_gpa"]
        last_applicant_score = (bottom_waitlisted["personal_statement_grade"] * 0.8) + bottom_waitlisted["school_gpa"]
        self.assertGreater(top_score, middle_applicant_score)
        self.assertGreater(middle_applicant_score, last_applicant_score)


if __name__ == "__main__":
    unittest.main()
