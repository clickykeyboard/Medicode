import math
import random
from datetime import datetime

from patient_records.patient import Patient


class Configuration:

    small_dashes = f"{ '-' * 20 }"
    medium_dashes = f"{ '-' * 30 }"
    long_dashes = f"{ '-' * 40 }"

    main_number_of_choices = [1, 2, 3, 4, 5, 6, 7]
    patient_main_number_of_choices = [1, 2]
    medical_history_number_of_choices = [1, 2]
    blood_section_number_of_choices = [1, 2, 3]
    schedule_appointment_number_of_choices = [1, 2]
    covid_19_number_of_choices = [1, 2]
    emergency_number_of_choices = [1, 2]

    @staticmethod
    def make_dummy_patient_record(patient):
        current_year = 2020

        record_dates = []
        history = {}

        pronoun = "He" if patient["patient_gender"] == "Male" else "She"

        diagnosis = [
            f"Patient has a fever of 103 F. {pronoun} is listless, irritable and vomits repeatedly. {pronoun} is showing signs of mental confusion. Diagnosis have shown that patient has a malignant tumor. Immediate Radiation Therapy has been suggested.",
            f"Patient has a case of Diarrhea. Patient is having headache and a rapid heart rate. However, it is nothing critical and {pronoun.lower()} has been given Loperamide for a weeks use.",
            f"Patient has pressure in their back abdomen. Tests have shown that {pronoun.lower()} has Urinary Tract Infection. Advance tests have shown that they have Cystitis.  Paracetamol has been prescribed.",
            f"Patient had a brutal car accident and was immediately shifted to the emergency room for surgery. After a successful surgery, {pronoun.lower()} is out of critical situation but will not wake up for a week at minimum.",
            f"Patient has eye irritation due to digital eye strain. {pronoun} has been prescribed eye drops."
        ]

        for _ in range(3):
            day = random.randint(1, 30)
            month = random.randint(1, 12)

            record_dates.append(
                f"""{day}/{month}/{random.randint(2020 - patient["patient_age"], current_year)}"""
            )

        for record_date in range(3):

            history[record_dates[record_date]] = random.choice(diagnosis)

        return history

    @staticmethod
    def make_dummy_patient():

        random_seven_digit = random.randint(1000000, 9999999)
        age = random.randint(1, 90)
        day = random.randint(1, 30)
        month = random.randint(1, 12)
        patient_pin = random.randint(0000, 9999)
        patient_contact = f"0{random.randint(300, 355)}-{random_seven_digit}"
        marital_status = ["Married", "Single"]

        patient_gender = ["Male", "Female"]

        patient_location = [
            "Lahore", "Islamabad", "Karachi",
            "Faisalabad", "Multan", "Gujranwala",
            "Okara", "Quetta", "Peshawar"]

        patient_blood_groups = [
            "O+", "O-",
            "A+", "A-",
            "B+", "B-",
            "AB+", "AB-"
        ]

        patient_names = [
            "Alif Bay", "Pay Tay",
            "Say Ye", "Jeem Chay", "Hay Khay",
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
            "marital_status": random.choice(marital_status) if age > 18 else "Single"
        }

        return patient_dummy_data

    @staticmethod
    def make_appointments():
        date_time_object = datetime.now()
        date_object = date_time_object
        days = ["Monday", "Tuesday", "Wednesday"]

        specialization = ["Eye Surgeon", "ENT", "Heart Specialist"]
        appointments = []

        for i in range(3):
            hour = random.randint(9, 14)
            minutes = random.randint(1, 59)
            minutes_string = str(minutes)
            doctor_name = Configuration.make_dummy_patient()["patient_name"]
            appointments.append({
                "doctor_name": doctor_name,
                "specialization": random.choice(specialization),
                "timing": f"""{hour - 12 if hour > 12 else hour}:{"0" + minutes_string if minutes < 10 else "" + minutes_string} {"PM" if hour > 11 else "AM"}, {days[i]}"""
            })

        return appointments


random_patient = Configuration.make_dummy_patient()

patient = Patient(
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

patient.set_patient_records(
    Configuration.make_dummy_patient_record(random_patient)
)
