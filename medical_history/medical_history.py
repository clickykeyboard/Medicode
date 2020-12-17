from config import Configuration, patient


def medical_main():
    while True:
        print(""" 
        Welcome to the Medical History Menu
        ----------------------
        * Enter [1] to check for Medical History
        * Enter [2] to go back
        ----------------------
        """)

        choice = int(input(">   "))
        if choice not in Configuration.medical_history_number_of_choices:
            print("----------------")
            print("Please enter a valid choice!")
            print("----------------")

        else:
            if choice == 1:
                print(patient.get_patient_records())
                print("Choice 1")

            elif choice == 2:
                print("Going back...")
                print("------------------------")
                break
