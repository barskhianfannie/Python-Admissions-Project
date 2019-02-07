"""
Admissions.
"""
from data.applications import Applications

def get(applications):
    """
    It's easier to do this step by step, first picking alumni/affirmative children as quotas permit and
    placing the rest in a general pool along with the others.
    """

    applicants =[]

    #Weighting Quoata for available spots per Alumni and Affirmative students
    alumniQuota = 0.2
    affirmativeQuota = 0.1

    #Set spots available to 36, 30 will be admitted and 6 will be waitlisted
    spots_available = 36

    #Set available Alumni and Affirmative Action spots
    alumniSpots = int(spots_available * alumniQuota)
    affirmativeSpots = int(spots_available * affirmativeQuota)

    #Calculate for equal weight to add "total_score" for sorting purposes.
    for applicant in applications:
        total_score = (applicant["personal_statement_grade"] * 0.8) + applicant["school_gpa"]
        applicant["total_score"] = total_score
        applicants.append(applicant)
        applicants.sort(key=lambda a: a["total_score"], reverse= True)

    accepted_applicants = []
    general_applicants = []
 
    for applicant in applicants:
        if spots_available > 0:
            if (applicant["has_alumni_parent"] and alumniSpots > 0):
                accepted_applicants.append(applicant)
                spots_available -= 1
                alumniSpots -= 1
            elif (applicant["affirmative_action"] and affirmativeSpots > 0):
                accepted_applicants.append(applicant)
                spots_available -= 1
                affirmativeSpots -=1
            else:
                general_applicants.append(applicant)
        else:
            break        

    for applicant in general_applicants:
        if spots_available > 0:
            accepted_applicants.append(applicant)
            spots_available -= 1
        else:
            break
    

    return accepted_applicants
