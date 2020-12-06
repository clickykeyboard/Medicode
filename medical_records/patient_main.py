from config import Configuration


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

        if choice not in Configuration.medical_main_number_of_choices:
            print("----------------")
            print("Please enter a valid choice!")
            print("----------------")

        else:
            if choice == 1:
                print("Choice 1")
            elif choice == 2:
                print("Going back...")
                print("------------------------")
                break
