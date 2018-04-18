class Aayulogic:

    # We pass in some information of Aayulogic Employee

    """
    first_name => First name of the employee
    last_name => Last name of the employee
    email => Employee's email
    phone_number => Employee's phone number
    text => Employee's text bio
    date => Employee's date of birth
    boolean => Employee's sex - M/F
    address => Employee's Address
    url => URL to a social account
    image_url => Display Image URL

    """

    def __init__(self, id, first_name, last_name, email, phone_number, text, date, boolean, address, url, image_url):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.text = text
        self.date = date
        self.boolean = boolean
        self.address = address
        self.url = url
        self.image_url = image_url

    def __repr__(self):
        return "Aayulogic('{}', '{}', {})".format(self.first_name, self.last_name, self.email)
