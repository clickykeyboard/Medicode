class Patient:
    def __init__(self, patient_name, patient_age, patient_date_of_birth,
                 patient_gender, patient_contact, patient_location, patient_cnic,
                 patient_pin, patient_blood_group,
                 marital_status):
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.patient_date_of_birth = patient_date_of_birth
        self.patient_gender = patient_gender
        self.patient_contact = patient_contact
        self.patient_location = patient_location
        self.patient_cnic = patient_cnic
        self.patient_pin = patient_pin
        self.patient_blood_group = patient_blood_group
        self.marital_status = marital_status

    def get_patient_name(self):
        return self.patient_name

    def get_patient_age(self):
        return self.patient_age

    def get_patient_date_of_birth(self):
        return self.patient_date_of_birth

    def get_patient_gender(self):
        return self.patient_gender

    def get_patient_contact(self):
        return self.patient_contact

    def get_patient_location(self):
        return self.patient_location

    def get_patient_cnic(self):
        return self.patient_cnic

    def get_patient_pin(self):
        return self.patient_pin

    def get_patient_blood_group(self):
        return self.patient_blood_group

    def get_marital_status(self):
        return self.marital_status

    def set_patient_name(self, new_patient_name):
        self.patient_name = new_patient_name

    def set_patient_age(self, new_patient_age):
        self.patient_age = new_patient_age

    def set_patient_date_of_birth(self, new_patient_date_of_birth):
        self.patient_date_of_birth = new_patient_date_of_birth

    def set_patient_gender(self, new_patient_gender):
        self.patient_gender = new_patient_gender

    def set_patient_contact(self, new_patient_contact):
        self.patient_contact = new_patient_contact

    def set_patient_location(self, new_patient_location):
        self.patient_location = new_patient_location

    def set_patient_cnic(self, new_patient_cnic):
        self.patient_cnic = new_patient_cnic

    def set_patient_pin(self, new_patient_pin):
        self.patient_pin = new_patient_pin

    def set_blood_group(self, new_blood_group):
        self.blood_group = new_blood_group

    def set_marital_status(self, new_marital_status):
        self.marital_status = new_marital_status
