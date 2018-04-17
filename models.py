class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@aayulogic.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self):
        return "Employees('{}', '{}', {}, '{}')".format(self.first, self.last, self.pay, self.fullname)
