from config import Configuration, patient


def medical_main():
    while True:
        print(f""" 
        Welcome to the Medical History Menu
        {Configuration.medium_dashes}
        * Enter [1] to check for Medical History
        * Enter [2] to go back
        {Configuration.medium_dashes}
        """)

        choice = int(input(">   "))
        if choice not in Configuration.medical_history_number_of_choices:
            print(f"{Configuration.small_dashes}")
            print("Please enter a valid choice!")
            print(f"{Configuration.small_dashes}")

        else:
            if choice == 1:
                patient_medical_records: dict = patient.get_patient_records()
                for date, diagnosis in patient_medical_records.items():
                    print(date)
                    print(diagnosis)
                    print(f"{Configuration.small_dashes}")




            elif choice == 2:
                print("Going back...")
                print(f"{Configuration.medium_dashes}")
                break
