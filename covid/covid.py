import requests
from datetime import datetime


from config import Configuration


def covid_main():

    while True:

        print(f"""
    
        Welcome to Patient Section
        {Configuration.medium_dashes}
        * Enter [1] for COVID-19 Informations
        * Enter [2] to go back 
        {Configuration.medium_dashes}
        """)

        choice = int(input(">   "))

        if choice not in Configuration.covid_19_number_of_choices:
            print(f"{Configuration.small_dashes}")
            print("Please enter a valid choice!")
            print(f"{Configuration.small_dashes}")

        else:
            if choice == 1:
                print("Requesting data... Please wait.\n")

                response = requests.get(
                    "https://api.covid19api.com/dayone/country/pakistan/status/confirmed")

                response_data = response.json()[-1]
                date_time_object = datetime.strptime(
                    response_data["Date"], "%Y-%m-%dT%H:%M:%SZ")
                new_date = date_time_object.strftime(
                    "Date: %d %B, %Y\nTime: %I:%M:%S")

                print(f"{Configuration.small_dashes}")
                print(f"""Country: {response_data["Country"]}""")
                print(f"""Country code: {response_data["CountryCode"]}""")
                print(f"""Cases: {response_data["Cases"]}""")
                print(f"""Status: {response_data["Status"]}""")
                print(f"""{new_date}""")
                print(f"{Configuration.small_dashes}")

                input("> Enter anything to proceed ")

            if choice == 2:
                print("Going back...")
                print(f"{Configuration.medium_dashes}")
                break
