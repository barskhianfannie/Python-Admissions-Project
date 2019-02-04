# Admissions
You're asked by the Jarvard Medical School to create software that decides admissions. Here's the criteria their board has specified.

* The strength of the application depends mainly on GPA and the grade assigned to the student's professional statement submitted in the application, each carrying equal weight.
* Up to 20% of the admissions are allocated to the children of the school alumni.
* Up to 10% of the seats go to students eligible under affirmative action. If a student qualifies under both alumni and affirmative action quotas, you need to assign them the alumni quota first.
* The school does not discriminate based on age.

Your job is to process 1,000 applications to pick an admitted list of 30 and a wait list of 6. Your work should cover:
* Applying the criteria above to pick the admitted and wait listed students (school/admissions.py)
* Writing unit tests to test different aspects of the logic (tests/admissions.py)
* Processing 1,000 applications and printing out the id's of the admitted and wait listed students as two separate lists, each sorted in numerical order and accompanied by serial numbers (run.py)

An "Applications" class is available to you get the student applications. Instantiating Applications(1000) will give you an iterable that you can use to get 1,000 student applications. See data/applications.py for the keys in the dictionaries that represent the applications.