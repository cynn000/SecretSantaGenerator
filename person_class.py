# person class for each participant name, email and who they are buying for
class Person:

    # intialize name, email, and buying for person
    def __init__(self, name, email, buying_for, previous_match_list):	# 2021 - adding another variable for last years match
        self.name = name
        self.email = email
        self.buying_for = buying_for
        self.previous_match_list = previous_match_list
   
    def get_name(self):
        return self.name

    def get_buying_for(self):
        return self.buying_for
    
    def get_previous_match_list(self):
        return self.previous_match_list
