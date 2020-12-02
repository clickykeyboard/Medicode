from config import medical_main_number_of_choices


def medical_main():

    while True:

        print("""
    
        Welcome to Medical Section
        --------------------
        * Enter [1] for Medical Records Section
        * Enter [2] to go back 
        --------------------
        """)

        choice = int(input(">   "))

        if choice not in medical_main_number_of_choices:
            print("----------------")
            print("Please enter a valid choice!")
            print("----------------")

        else:

            if choice == 1:
                print("Choice 1")
            elif choice == 2:
                break
