import random

from patient_records.patient import Patient


class Configuration:

    main_number_of_choices = [1, 2, 3, 4, 5, 6, 7]
    patient_main_number_of_choices = [1, 2]
    medical_history_number_of_choices = [1, 2]
    blood_section_number_of_choices = [1, 2, 3]
    schedule_appointment_number_of_choices = [1, 2]
    covid_19_number_of_choices = [1, 2, ]
    emergency_number_of_choices = [1, 2]

    def make_dummy_patient():

        random_seven_digit = random.randint(1000000, 9999999)
        age = random.randint(1, 90)
        day = random.randint(1, 30)
        month = random.randint(1, 12)
        patient_pin = random.randint(0000, 9999)
        patient_contact = f"0{random.randint(300, 355)}-{random_seven_digit}"
        marital_status = ["M", "S"]

        patient_gender = ["Male", "Female"]

        patient_location = [
            "Lahore", "Islamabad", "Karachi",
            "Faisalabad", "Multan", "Gujranwala",
            "Okara", "Quetta", "Peshawar"
            "Khyber Pakhtunkhwa"]

        patient_blood_groups = [
            "O+", "O-",
            "A+", "A-",
            "B+", "B-",
            "AB+", "AB-"
        ]

        patient_names = [
            "Alif Bay", "Pay Tay",
            "Say Ye", "Jeem Chay", "Hay Khay"
            "Daal Daal", "Zuad Ray",
            "Aray Zay", "Say Seen",
            "Sheen Suad", "Duad Toye",
            "Zoye Ain", "Gain Fay",
            "Qaaf Kaaf", "Gaaf Laam",
            "Meem Noon", "Wao Hay"
        ]

        patient_dummy_data = {
            "patient_name": random.choice(patient_names),
            "patient_age": age,
            "patient_date_of_birth": f"{day}/{month}/{2020 - age}",
            "patient_gender": random.choice(patient_gender),
            "patient_contact": patient_contact,
            "patient_location": random.choice(patient_location),
            "patient_cnic": f"35202-{random_seven_digit}-{random.randint(0, 9)}",
            "patient_pin": patient_pin,
            "patient_blood_group": random.choice(patient_blood_groups),
            "marital_status": random.choice(marital_status),
            "records": [],
            "appointments": []
        }

        return patient_dummy_data


random_patient = Configuration.make_dummy_patient()

patient_object = Patient(
    random_patient["patient_name"],
    random_patient["patient_age"],
    random_patient["patient_date_of_birth"],
    random_patient["patient_gender"],
    random_patient["patient_contact"],
    random_patient["patient_location"],
    random_patient["patient_cnic"],
    random_patient["patient_pin"],
    random_patient["patient_blood_group"],
    random_patient["marital_status"]
)
