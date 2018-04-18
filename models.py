class Aayulogic:

    # We pass in some information of Aayulogic Employee

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    @property
    def email(self):
        return "{}.{}@aayulogic.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self):
        return "Employees('{}', '{}', {})".format(self.first, self.last, self.salary)
