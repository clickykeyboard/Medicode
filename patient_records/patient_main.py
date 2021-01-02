from config import Configuration, patient


def patient_main():

    while True:

        print(f"""
    
        Welcome to Patient Section
        {Configuration.medium_dashes}
        * Enter [1] for Patient Information
        * Enter [2] to go back 
        {Configuration.medium_dashes}
        """)

        choice = int(input(">   "))

        if choice not in Configuration.patient_main_number_of_choices:
            print(f"{Configuration.small_dashes}")
            print("Please enter a valid choice!")
            print(f"{Configuration.small_dashes}")

        else:
            if choice == 1:
                print(f"""
        {Configuration.long_dashes}
        Name: {patient.get_patient_name()}
        Gender: {patient.get_patient_gender()}
        Age: {patient.get_patient_age()}
        Blood Group: {patient.get_patient_blood_group()}
        Date Of Birth: {patient.get_patient_date_of_birth()}
        Contact: {patient.get_patient_contact()}
        City: {patient.get_patient_location()}
        CNIC: {patient.get_patient_cnic()}
        PIN: {patient.get_patient_pin()}
        Marital Status: {patient.get_marital_status()}
        {Configuration.long_dashes}
        """)

            elif choice == 2:
                print("Going back...")
                print(f"{Configuration.medium_dashes}")
                break
