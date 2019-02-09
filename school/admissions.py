"""
Admissions.
"""
from data.applications import Applications

def get(applications):
    """
    It's easier to do this step by step, first picking alumni/affirmative children as quotas permit and
    placing the rest in a general pool along with the others.
    """
    #Set spots available for each quota and sort applcants by total weighted score.
    alumni_spots = 6
    affirmative_spots = 3
    applicants = list(applications)
    applicants.sort(key=lambda a: (a["personal_statement_grade"] * 0.8) + a["school_gpa"], reverse=True)

    accepted = []
    general_applicants = []
    waitlisted_applicants = []

    #Will Return a Tuple with two lists (Accepted Applicants / Waitlisted Applicants)
    accepted_applicants =(accepted, waitlisted_applicants)
    
    #Check for alumni/affirmative applicants to meet quota.
    for applicant in applicants:
        if applicant["has_alumni_parent"] and alumni_spots > 0:
            accepted.append(applicant)
            alumni_spots -= 1
        elif applicant["affirmative_action"] and affirmative_spots > 0:
            accepted.append(applicant)
            affirmative_spots -= 1
        else:
            general_applicants.append(applicant)


    #Calculate available spots after meeting alumni/affirmative quota and fill them.       
    general_spots = 27 + (9-len(accepted))
    for applicant in general_applicants:
        if len(accepted) < 30:
            accepted.append(applicant)
            general_spots -= 1

    #Fill waitlisted spots and add to waitlisted applicant list
    for applicant in general_applicants:
        if len(waitlisted_applicants) < 6:
            waitlisted_applicants.append(applicant)

    #Sort all accepted and waitlisted applicants by total weighted score.
    accepted.sort(key=lambda a: (a["personal_statement_grade"] * 0.8) + a["school_gpa"], reverse=True)
    waitlisted_applicants.sort(key=lambda a: (a["personal_statement_grade"] * 0.8) + a["school_gpa"], reverse=True)

    return accepted_applicants
