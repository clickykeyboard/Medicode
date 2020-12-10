from config import Configuration, patient


def patient_main():

    while True:

        print("""
    
        Welcome to Patient Section
        --------------------
        * Enter [1] for Patient Information
        * Enter [2] to go back 
        --------------------
        """)

        choice = int(input(">   "))

        if choice not in Configuration.patient_main_number_of_choices:
            print("----------------")
            print("Please enter a valid choice!")
            print("----------------")

        else:
            if choice == 1:
                print("Choice 1")
                print("Name: ", patient.get_patient_name())
                print("Gender: ", patient.get_patient_gender())
                print("Age :", patient.get_patient_age())
                print("Blood Group: ", patient.get_patient_blood_group())
                print("Date Of Birth: ", patient.get_patient_date_of_birth())
                print("Contact: ", patient.get_patient_contact())
                print("City: ", patient.get_patient_location())
                print("CNIC: ", patient.get_patient_cnic())
                print("PIN: ", patient.get_patient_pin())
                print("Marital Status: ", patient.get_marital_status())


            elif choice == 2:
                print("Going back...")
                print("------------------------")
                break

