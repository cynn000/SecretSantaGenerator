# person class for each participant name, email and who they are buying for
class Person:

    # intialize name, email, and buying for person
    def __init__(self, name, email, buying_for, lastyear_match):	# 2021 - adding another variable for last years match
        self.name = name
        self.email = email
        self.buying_for = buying_for
        self.lastyear_match = lastyear_match
   
        