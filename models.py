class Aayulogic:

    # We pass in some information of Aayulogic Employee

    def __init__(self, first, last, salary, phone, bio, birth_date, gender, longitude, latitude, social_media):  # Image
        self.first = first
        self.last = last
        self.salary = salary
        self.phone = phone
        self.bio = bio
        self.birth_date = birth_date
        self.gender = gender
        self.longitude = longitude
        self.latitude = latitude
        self.social_media = social_media
        # Add image

    @property
    def email(self):
        return "{}.{}@aayulogic.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self):
        return "Employees('{}', '{}', {})".format(self.first, self.last, self.salary)
