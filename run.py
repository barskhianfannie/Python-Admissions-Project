"""
Get admissions.
"""
from data.applications import Applications
from school.admissions import get
class Run(object):
    """
    Invoking the admissions logic.
    """

    def print_list(self):
        """
        Print admitted and waitlisted candidate details.
        """
        applications = Applications(1000)
        admitted = get(applications)
        admitted_applicants = admitted[:30]
        waitlisted_applicants = admitted[30:]

        print("------------Admitted Applicants-----------------")
        for index, applicant in enumerate(admitted_applicants):
            print("%10d%22d" %(index + 1,applicant["application_id"]))
        print("-----------Waitlisted Applicants----------------")
        for index, applicant in enumerate(waitlisted_applicants):
            print("%10d%22d" %(index + 1,applicant["application_id"]))
            
if __name__ == "__main__":
    Run().print_list()
