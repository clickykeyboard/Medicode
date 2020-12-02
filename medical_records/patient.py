class Patient:
    def __init__(self, first_name, middle_name, last_name, age,
                 gender, email, blood_group, city, address, disability, marital_status):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = email
        self.blood_group = blood_group
        self.city = city
        self.address = address
        self.disability = disability
        self.marital_status = marital_status

    def get_first_name(self):
        return self.first_name

    def get_middle_name(self):
        return self.middle_name

    def get_last_name(self):
        return self.age

    def get_gender(self):
        return self.gender

    def get_email(self):
        return self.email

    def get_blood_group(self):
        return self.blood_group

    def get_city(self):
        return self.city

    def get_address(self):
        return self.address

    def get_disability(self):
        return self.disability

    def get_marital_status(self):
        return self.marital_status

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def set_middle_name(self, new_middle_name):
        self.middle_name = new_middle_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_email(self, new_email):
        self.email = new_email

    def set_blood_group(self, new_blood_group):
        self.blood_group = new_blood_group

    def set_city(self, new_city):
        self.city = new_city

    def set_address(self, new_address):
        self.address = new_address

    def set_disability(self, new_disability):
        self.disability = new_disability

    def set_marital_status(self, new_marital_status):
        self.marital_status = new_marital_status
