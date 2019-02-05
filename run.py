"""
Get admissions.
"""
from data.applications import Applications
class Run(object):
    """
    Invoking the admissions logic.
    """

    def print_list(self):
        """
        Print admitted and waitlisted candidate details.
        """
        hello = Applications(10)
        

if __name__ == "__main__":
    Run().print_list()
