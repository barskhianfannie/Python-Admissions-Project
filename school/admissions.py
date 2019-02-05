"""
Admissions.
"""
from data.applications import Applications

def get(applications):
    """
    It's easier to do this step by step, first picking alumni/affirmative children as quotas permit and
    placing the rest in a general pool along with the others.
    """
    applications = Applications(10)
    applicants = []
    alumniQuota = 0.2
    affirmativeQuota = 0.1
    spots_available = 36
    alumniSpots = spots_available * alumniQuota
    affirmativeSpots = spots_available * spots_available
    for applicant in applications:
        total_score = (applicant["school_gpa"] + 0.8) * applicant["personal_statement_grade"]
        applicant["total_score"] = total_score
        applicants.append(applicant)
        applicants.sort(key=lambda a: a["total_score"])

    accepted_applicants = []
    general_applicants = []
    for applicant in applicants:
        if (applicant["has_alumni_parent"] and (alumniSpots > 0)):
            accepted_applicants.append(applicant)
            spots_available -= 1
            alumniSpots -= 1
        elif (applicant["affirmative_action"] and (affirmativeSpots > 0)):
            accepted_applicants.append(applicant)
            spots_available -= 1
            affirmativeSpots -=1
        else:
            accepted_applicants.append(applicant)
            spots_available -= 1

    for applicant in general_applicants:
        if spots_available > 0:
            accepted_applicants.append(applicant)
    

    return accepted_applicants
