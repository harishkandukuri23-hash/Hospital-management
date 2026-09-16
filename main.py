# Hospital Management System
# OOP + File Handling Version

# -----------------------------
# File setup
# -----------------------------

FILES = [
    "user.txt",
    "Doctor.txt",
    "Patients.txt",
    "OP.txt",
    "meds.txt",
    "Prescription.txt",
    "Bill.txt",
]

for file_name in FILES:
    try:
        with open(file_name, "x"):
            pass
    except FileExistsError:
        pass


# -----------------------------
# User / Authentication
# -----------------------------

class User:
    def __init__(self, id, user_name, password, role):
        self.id = id
        self.user_name = user_name
        self.password = password
        self.role = role

    def details(self):
        return f"{self.id},{self.user_name},{self.password},{self.role}\n"


class Autheration:
    def Registeration(self):
        id = input("Enter user id : ").strip()
        user_name = input("Enter user name : ").strip()
        password = input("Enter user password : ").strip()
        role = input("Enter user role (Admin/Receptionist/Doctor) : ").strip()

        valid_roles = ["Admin", "Receptionist", "Doctor"]

        if role not in valid_roles:
            print("Invalid role. Choose Admin, Receptionist or Doctor.")
            return

        U1 = User(id, user_name, password, role)

        with open("user.txt", "r") as read:
            Data = read.readlines()

        found = False

        for line in Data:
            Details = line.strip().split(",")

            if len(Details) >= 2 and Details[1] == user_name:
                found = True
                break

        if not found:
            with open("user.txt", "a") as add:
                add.write(U1.details())

            print("Registration successfully completed")
        else:
            print("User already exists")

    def Login(self):
        user_name = input("Enter your user name : ").strip()
        password = input("Enter your password : ").strip()

        with open("user.txt", "r") as check:
            Data = check.readlines()

        for line in Data:
            Details = line.strip().split(",")

            if len(Details) < 4:
                continue

            if Details[1] == user_name:
                if Details[2] == password:
                    print("Login successfully")
                    return Details[3]
                else:
                    print("Invalid credentials")
                    return None

        print("User not found in database, please register")
        return None


# -----------------------------
# Models
# -----------------------------

class Doctor:
    def __init__(self, id, name, specialization, contact_no, consultation_fees):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.contact_no = contact_no
        self.consultation_fees = consultation_fees

    def Doc_details(self):
        return (
            f"{self.id},{self.name},{self.specialization},"
            f"{self.contact_no},{self.consultation_fees}\n"
        )


class Patient:
    def __init__(
        self,
        Patient_id,
        Patient_name,
        Age,
        Gender,
        contact_number,
        Address,
        Blood_group
    ):
        self.Patient_id = Patient_id
        self.Patient_name = Patient_name
        self.Age = Age
        self.Gender = Gender
        self.contact_number = contact_number
        self.Address = Address
        self.Blood_group = Blood_group

    def patient_details(self):
        return (
            f"{self.Patient_id},{self.Patient_name},{self.Age},"
            f"{self.Gender},{self.contact_number},{self.Address},"
            f"{self.Blood_group}\n"
        )


class Appointment:
    def __init__(
        self,
        Appointment_id,
        Patient_id,
        Doctor_id,
        Date,
        Time,
        Status
    ):
        self.Appointment_id = Appointment_id
        self.Patient_id = Patient_id
        self.Doctor_id = Doctor_id
        self.Date = Date
        self.Time = Time
        self.Status = Status

    def Appointment_details(self):
        return (
            f"{self.Appointment_id},{self.Patient_id},{self.Doctor_id},"
            f"{self.Date},{self.Time},{self.Status}\n"
        )


class Mediance:
    def __init__(self, Medicine_id, Medicine_name, Price, Quantity):
        self.Medicine_id = Medicine_id
        self.Medicine_name = Medicine_name
        self.Price = Price
        self.Quantity = Quantity

    def mediance_deltails(self):
        return (
            f"{self.Medicine_id},{self.Medicine_name},"
            f"{self.Price},{self.Quantity}\n"
        )


class Prescription:
    def __init__(
        self,
        Prescription_id,
        Patient_id,
        Doctor_id,
        Diagnosis,
        Medicines
    ):
        self.Prescription_id = Prescription_id
        self.Patient_id = Patient_id
        self.Doctor_id = Doctor_id
        self.Diagnosis = Diagnosis
        self.Medicines = Medicines

    def Prescription_details(self):
        return (
            f"{self.Prescription_id},{self.Patient_id},{self.Doctor_id},"
            f"{self.Diagnosis},{self.Medicines}\n"
        )


class Bill:
    def __init__(
        self,
        Bill_id,
        Patient_id,
        Appointment_id,
        Amount,
        Payment_status
    ):
        self.Bill_id = Bill_id
        self.Patient_id = Patient_id
        self.Appointment_id = Appointment_id
        self.Amount = Amount
        self.Payment_status = Payment_status

    def Bill_details(self):
        return (
            f"{self.Bill_id},{self.Patient_id},{self.Appointment_id},"
            f"{self.Amount},{self.Payment_status}\n"
        )


# -----------------------------
# Admin Operations
# -----------------------------

class Admin:
    def Add_Doc(self):
        id = input("Enter Doctor id : ").strip()
        name = input("Enter Doctor name : ").strip()
        specialization = input("Specialization field : ").strip()
        contact_no = input("Enter Doctor contact number : ").strip()
        consultation_fees = input("Consultation Fees Amount : ").strip()

        Doc = Doctor(
            id,
            name,
            specialization,
            contact_no,
            consultation_fees
        )

        with open("Doctor.txt", "r") as check:
            Data = check.readlines()

        found = False

        for line in Data:
            Details = line.strip().split(",")

            if len(Details) >= 2:
                if Details[0] == id or Details[1].lower() == name.lower():
                    found = True
                    break

        if found:
            print("Doctor already registered in database")
        else:
            with open("Doctor.txt", "a") as add:
                add.write(Doc.Doc_details())

            print("Doctor added to database successfully")

    def Doc_Details_update(self):
        id = input("Enter Doctor ID for updating : ").strip()

        with open("Doctor.txt", "r") as search:
            Data = search.readlines()

        is_found = False
        updated_data = []

        for line in Data:
            Details = line.strip().split(",")

            if len(Details) < 5:
                updated_data.append(line)
                continue

            if Details[0] == id:
                is_found = True

                name = input(
                    f"Enter Doctor Name [{Details[1]}] : "
                ).strip()
                specialization = input(
                    f"Enter specialization [{Details[2]}] : "
                ).strip()
                contact_no = input(
                    f"Enter contact number [{Details[3]}] : "
                ).strip()
                consultation_fees = input(
                    f"Enter consultation fees [{Details[4]}] : "
                ).strip()

                if name == "":
                    name = Details[1]

                if specialization == "":
                    specialization = Details[2]

                if contact_no == "":
                    contact_no = Details[3]

                if consultation_fees == "":
                    consultation_fees = Details[4]

                updated_data.append(
                    f"{id},{name},{specialization},"
                    f"{contact_no},{consultation_fees}\n"
                )
            else:
                updated_data.append(line)

        with open("Doctor.txt", "w") as Update:
            Update.writelines(updated_data)

        if is_found:
            print("Doctor details updated successfully!")
        else:
            print("Doctor details not found")

    def Remove_Doc(self):
        id = input(
            "Enter Doctor id to remove from the database : "
        ).strip()

        with open("Doctor.txt", "r") as check:
            Data = check.readlines()

        is_found = False

        with open("Doctor.txt", "w") as change:
            for line in Data:
                Details = line.strip().split(",")

                if len(Details) > 0 and Details[0] == id:
                    is_found = True
                else:
                    change.write(line)

        if is_found:
            print("Doctor removed from database")
        else:
            print("Doctor not found in database")

    def view_Doc(self):
        with open("Doctor.txt", "r") as view:
            Data = view.readlines()

        if not Data:
            print("Database is empty")
            return

        print("-" * 72)
        print(
            f"|{'ID':<7}|{'Name':<18}|{'Specialization':<18}|"
            f"{'Contact':<15}|{'Fees':<8}|"
        )
        print("-" * 72)

        for line in Data:
            details = line.strip().split(",")

            if len(details) < 5:
                continue

            print(
                f"|{details[0]:<7}|{details[1]:<18}|"
                f"{details[2]:<18}|{details[3]:<15}|"
                f"{details[4]:<8}|"
            )

        print("-" * 72)

    def Add_meds(self):
        id = input("Enter Medicine id : ").strip()
        name = input("Enter Medicine name : ").strip()
        Price = input("Medicine price : ").strip()
        Quantity = input("Medicine quantity : ").strip()

        try:
            float(Price)
            int(Quantity)
        except ValueError:
            print("Price must be a number and quantity must be an integer.")
            return

        med = Mediance(id, name, Price, Quantity)

        with open("meds.txt", "r") as check:
            Data = check.readlines()

        is_found = False
        updated_data = []

        for line in Data:
            details = line.strip().split(",")

            if len(details) < 4:
                updated_data.append(line)
                continue

            if details[0] == id or details[1].lower() == name.lower():
                is_found = True

                try:
                    new_quantity = int(details[3]) + int(Quantity)
                except ValueError:
                    new_quantity = int(Quantity)

                updated_data.append(
                    f"{details[0]},{details[1]},"
                    f"{details[2]},{new_quantity}\n"
                )
            else:
                updated_data.append(line)

        if is_found:
            with open("meds.txt", "w") as Add:
                Add.writelines(updated_data)

            print("Medicine quantity updated successfully.")
        else:
            with open("meds.txt", "a") as Add:
                Add.write(med.mediance_deltails())

            print("Medicine added successfully.")

    def update_meds(self):
        Id = input(
            "Enter medicine ID for checking and updating : "
        ).strip()

        with open("meds.txt", "r") as search:
            Data = search.readlines()

        is_found = False
        updated_data = []

        for line in Data:
            Details = line.strip().split(",")

            if len(Details) < 4:
                updated_data.append(line)
                continue

            if Details[0] == Id:
                is_found = True

                name = input(
                    f"Enter Medicine Name [{Details[1]}] : "
                ).strip()
                Price = input(
                    f"Enter Medicine Price [{Details[2]}] : "
                ).strip()
                Quantity = input(
                    f"Enter Medicine Quantity [{Details[3]}] : "
                ).strip()

                if name == "":
                    name = Details[1]

                if Price == "":
                    Price = Details[2]

                if Quantity == "":
                    Quantity = Details[3]

                try:
                    float(Price)
                    int(Quantity)
                except ValueError:
                    print(
                        "Invalid price or quantity. Old values retained."
                    )
                    name = Details[1]
                    Price = Details[2]
                    Quantity = Details[3]

                updated_data.append(
                    f"{Id},{name},{Price},{Quantity}\n"
                )
            else:
                updated_data.append(line)

        with open("meds.txt", "w") as Update:
            Update.writelines(updated_data)

        if is_found:
            print("Medicine updated successfully!")
        else:
            print("Medicine not found")

    def Remove_meds(self):
        Id = input(
            "Enter medicine ID you want to delete : "
        ).strip()

        with open("meds.txt", "r") as search:
            Data = search.readlines()

        is_found = False

        with open("meds.txt", "w") as change:
            for line in Data:
                Details = line.strip().split(",")

                if len(Details) > 0 and Details[0] == Id:
                    is_found = True
                else:
                    change.write(line)

        if is_found:
            print("Medicine deleted successfully")
        else:
            print("Medicine not found")

    def view_meds(self):
        with open("meds.txt", "r") as view:
            Data = view.readlines()

        if not Data:
            print("Medicine database is empty")
            return

        print("-" * 50)
        print(
            f"|{'ID':<7}|{'Name':<18}|{'Price':<10}|{'Quantity':<10}|"
        )
        print("-" * 50)

        for line in Data:
            details = line.strip().split(",")

            if len(details) < 4:
                continue

            print(
                f"|{details[0]:<7}|{details[1]:<18}|"
                f"{details[2]:<10}|{details[3]:<10}|"
            )

        print("-" * 50)


# -----------------------------
# Receptionist Operations
# -----------------------------

class Receptionist(Admin):
    def Add_Patient(self):
        id = input("Enter Patient id : ").strip()
        name = input("Enter Patient name : ").strip()
        Age = input("Enter Patient Age : ").strip()
        Gender = input("Enter Patient gender : ").strip()
        contact_no = input("Enter Patient contact number : ").strip()
        Address = input("Enter Patient Address : ").strip()
        Blood_group = input("Enter Patient Blood Group : ").strip()

        P1 = Patient(
            id,
            name,
            Age,
            Gender,
            contact_no,
            Address,
            Blood_group
        )

        with open("Patients.txt", "r") as check:
            Data = check.readlines()

        found = False

        for line in Data:
            Details = line.strip().split(",")

            if len(Details) > 0 and Details[0] == id:
                found = True
                break

        if found:
            print("Patient already registered in database")
        else:
            with open("Patients.txt", "a") as add:
                add.write(P1.patient_details())

            print("Patient added to database successfully")

    def view_patients(self):
        with open("Patients.txt", "r") as view:
            Data = view.readlines()

        if not Data:
            print("Patient database is empty")
            return

        print("-" * 102)
        print(
            f"|{'ID':<7}|{'Name':<18}|{'Age':<5}|{'Gender':<10}|"
            f"{'Contact':<15}|{'Address':<25}|{'Blood':<8}|"
        )
        print("-" * 102)

        for line in Data:
            details = line.strip().split(",")

            if len(details) < 7:
                continue

            print(
                f"|{details[0]:<7}|{details[1]:<18}|"
                f"{details[2]:<5}|{details[3]:<10}|"
                f"{details[4]:<15}|{details[5]:<25}|"
                f"{details[6]:<8}|"
            )

        print("-" * 102)

    def op(self):
        Patient_id = input("Enter the Patient ID : ").strip()
        Doctor_id = input("Enter the Doctor ID : ").strip()

        # Check Patient
        with open("Patients.txt", "r") as check:
            Data = check.readlines()

        patient_found = False

        for line in Data:
            Details = line.strip().split(",")

            if len(Details) > 0 and Details[0] == Patient_id:
                patient_found = True
                break

        if not patient_found:
            print("Patient not found")
            return

        # Check Doctor
        with open("Doctor.txt", "r") as check:
            Data = check.readlines()

        doctor_found = False

        for line in Data:
            Details = line.strip().split(",")

            if len(Details) > 0 and Details[0] == Doctor_id:
                doctor_found = True
                break

        if not doctor_found:
            print("Doctor not found")
            return

        Appointment_id = input("Appointment ID : ").strip()

        # Check duplicate appointment ID
        with open("OP.txt", "r") as check:
            appointments = check.readlines()

        for line in appointments:
            Details = line.strip().split(",")

            if len(Details) > 0 and Details[0] == Appointment_id:
                print("Appointment ID already exists")
                return

        Date = input("Date (DD-MM-YYYY) : ").strip()
        Time = input("Time : ").strip()
        Status = input(
            "Status (Scheduled/Completed/Cancelled) : "
        ).strip()

        p1 = Appointment(
            Appointment_id,
            Patient_id,
            Doctor_id,
            Date,
            Time,
            Status
        )

        with open("OP.txt", "a") as add:
            add.write(p1.Appointment_details())

        print("Appointment booked successfully")

    def view_op(self):
        with open("OP.txt", "r") as view:
            Data = view.readlines()

        if not Data:
            print("Appointment database is empty")
            return

        print("-" * 76)
        print(
            f"|{'OP ID':<9}|{'P ID':<9}|{'D ID':<9}|"
            f"{'Date':<15}|{'Time':<12}|{'Status':<15}|"
        )
        print("-" * 76)

        for line in Data:
            details = line.strip().split(",")

            if len(details) < 6:
                continue

            print(
                f"|{details[0]:<9}|{details[1]:<9}|"
                f"{details[2]:<9}|{details[3]:<15}|"
                f"{details[4]:<12}|{details[5]:<15}|"
            )

        print("-" * 76)



# -----------------------------
# Specialization / Diagnosis
# -----------------------------

SPECIALIZATION_DIAGNOSES = {
    "Cardiologist": [
        "Hypertension",
        "Heart Disease",
        "Arrhythmia",
        "Angina"
    ],
    "Dermatologist": [
        "Acne",
        "Eczema",
        "Psoriasis",
        "Fungal Infection"
    ],
    "General Physician": [
        "Fever",
        "Cold",
        "Flu",
        "Diabetes",
        "Infection"
    ],
    "Pediatrician": [
        "Fever",
        "Cold",
        "Asthma",
        "Ear Infection"
    ],
    "Orthopedic": [
        "Fracture",
        "Arthritis",
        "Back Pain",
        "Joint Pain"
    ],
    "Neurologist": [
        "Migraine",
        "Epilepsy",
        "Neuropathy",
        "Stroke"
    ],
    "Gastroenterologist": [
        "Gastritis",
        "Ulcer",
        "Acid Reflux",
        "IBS"
    ],
    "Pulmonologist": [
        "Asthma",
        "Bronchitis",
        "Pneumonia",
        "COPD"
    ],
    "ENT Specialist": [
        "Sinusitis",
        "Tonsillitis",
        "Ear Infection",
        "Sinus Allergy"
    ],
    "Gynecologist": [
        "PCOS",
        "Menstrual Disorder",
        "Pregnancy-related Condition"
    ],
    "Ophthalmologist": [
        "Cataract",
        "Glaucoma",
        "Conjunctivitis",
        "Myopia"
    ],
    "Dentist": [
        "Cavities",
        "Gingivitis",
        "Tooth Infection",
        "Toothache"
    ]
}


def get_diagnoses_for_specialization(specialization):
    """Return diagnoses for a doctor's specialization."""
    for key, diagnoses in SPECIALIZATION_DIAGNOSES.items():
        if key.lower() == specialization.strip().lower():
            return diagnoses
    return []


def choose_diagnosis(specialization):
    """Display only diagnoses related to the doctor's specialization."""
    diagnoses = get_diagnoses_for_specialization(specialization)

    if not diagnoses:
        print(
            f"\nNo diagnosis list configured for "
            f"'{specialization}'."
        )
        return input("Enter diagnosis manually : ").strip()

    print("\n" + "-" * 50)
    print(f"Diagnoses for {specialization}")
    print("-" * 50)

    for index, diagnosis in enumerate(diagnoses, start=1):
        print(f"{index}. {diagnosis}")

    print("-" * 50)

    while True:
        choice = input("Select diagnosis : ").strip()

        try:
            choice = int(choice)

            if 1 <= choice <= len(diagnoses):
                return diagnoses[choice - 1]

            print("Please select a valid diagnosis number.")

        except ValueError:
            print("Please enter a number.")



# -----------------------------
# Doctor Operations
# -----------------------------

class Doc_Operations(Receptionist):
    def view_appointments(self):
        Doc_ID = input("Doctor ID : ").strip()

        with open("OP.txt", "r") as identity:
            Data = identity.readlines()

        found = False

        print("-" * 76)
        print(
            f"|{'OP ID':<9}|{'P ID':<9}|{'D ID':<9}|"
            f"{'Date':<15}|{'Time':<12}|{'Status':<15}|"
        )
        print("-" * 76)

        for line in Data:
            Details = line.strip().split(",")

            if len(Details) < 6:
                continue

            if Details[2] == Doc_ID:
                found = True

                print(
                    f"|{Details[0]:<9}|{Details[1]:<9}|"
                    f"{Details[2]:<9}|{Details[3]:<15}|"
                    f"{Details[4]:<12}|{Details[5]:<15}|"
                )

        print("-" * 76)

        if not found:
            print("No appointments scheduled for this doctor")

    def Treat_patient(self):
        Doctor_id = input("Enter Doctor ID : ").strip()
        Appointment_id = input("Enter Appointment ID : ").strip()

        # Find appointment
        with open("OP.txt", "r") as check:
            Data = check.readlines()

        appointment_found = False
        Patient_id = None
        appointment_status = None

        for line in Data:
            Details = line.strip().split(",")

            if len(Details) < 6:
                continue

            if (
                Details[0] == Appointment_id
                and Details[2] == Doctor_id
            ):
                appointment_found = True
                Patient_id = Details[1]
                appointment_status = Details[5]
                break

        if not appointment_found:
            print("Appointment not found for this doctor.")
            return

        if appointment_status.lower() == "completed":
            print("This appointment is already completed.")
            return

        if appointment_status.lower() == "cancelled":
            print("This appointment has been cancelled.")
            return

        # Show patient details
        with open("Patients.txt", "r") as check:
            Patient_Data = check.readlines()

        patient_found = False

        for line in Patient_Data:
            Details = line.strip().split(",")

            if len(Details) < 7:
                continue

            if Details[0] == Patient_id:
                patient_found = True

                print("\n" + "-" * 45)
                print("Patient Details")
                print("-" * 45)
                print("Patient ID   :", Details[0])
                print("Name         :", Details[1])
                print("Age          :", Details[2])
                print("Gender       :", Details[3])
                print("Contact      :", Details[4])
                print("Address      :", Details[5])
                print("Blood Group  :", Details[6])
                print("-" * 45)

                break

        if not patient_found:
            print("Patient not found.")
            return

        # Find the doctor's specialization
        doctor_specialization = None

        with open("Doctor.txt", "r") as check:
            doctor_data = check.readlines()

        for doctor_line in doctor_data:
            doctor_details = doctor_line.strip().split(",")

            if len(doctor_details) >= 5 and doctor_details[0] == Doctor_id:
                doctor_specialization = doctor_details[2]
                break

        if doctor_specialization is None:
            print("Doctor details not found.")
            return

        print(f"\nDoctor Specialization: {doctor_specialization}")

        # Diagnosis is now selected according to specialization
        Diagnosis = choose_diagnosis(doctor_specialization)

        # Medicine selection
        selected_medicines = []
        medicine_total = 0.0

        while True:
            choice = input(
                "\nDo you want to prescribe medicine? (yes/no) : "
            ).strip().lower()

            if choice == "no":
                break

            if choice != "yes":
                print("Please enter yes or no.")
                continue

            self.view_meds()

            Medicine_id = input("Enter Medicine ID : ").strip()
            required_quantity = input(
                "Enter required quantity : "
            ).strip()

            try:
                required_quantity = int(required_quantity)

                if required_quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

            except ValueError:
                print("Quantity must be a valid integer.")
                continue

            with open("meds.txt", "r") as check:
                medicines_data = check.readlines()

            medicine_found = False
            updated_medicines = []
            prescribed_name = None
            prescribed_price = 0.0

            for med_line in medicines_data:
                med_details = med_line.strip().split(",")

                if len(med_details) < 4:
                    updated_medicines.append(med_line)
                    continue

                if med_details[0] == Medicine_id:
                    medicine_found = True

                    try:
                        available_quantity = int(med_details[3])
                        price = float(med_details[2])
                    except ValueError:
                        print(
                            "Invalid medicine data in meds.txt."
                        )
                        updated_medicines.append(med_line)
                        continue

                    if available_quantity < required_quantity:
                        print(
                            f"Only {available_quantity} units available."
                        )
                        updated_medicines.append(med_line)
                        prescribed_name = None
                    else:
                        new_quantity = (
                            available_quantity - required_quantity
                        )

                        updated_medicines.append(
                            f"{med_details[0]},{med_details[1]},"
                            f"{med_details[2]},{new_quantity}\n"
                        )

                        prescribed_name = med_details[1]
                        prescribed_price = (
                            price * required_quantity
                        )
                else:
                    updated_medicines.append(med_line)

            if not medicine_found:
                print("Medicine not found.")
                continue

            if prescribed_name is None:
                continue

            with open("meds.txt", "w") as update:
                update.writelines(updated_medicines)

            selected_medicines.append(
                f"{prescribed_name} x{required_quantity}"
            )

            medicine_total += prescribed_price

            print(
                f"{prescribed_name} added to prescription."
            )

        if selected_medicines:
            Medicines = "; ".join(selected_medicines)
        else:
            Medicines = "No Medicines"

        # Generate unique-ish prescription ID
        Prescription_id = (
            "PR-" + Appointment_id + "-" + Patient_id
        )

        prescription = Prescription(
            Prescription_id,
            Patient_id,
            Doctor_id,
            Diagnosis,
            Medicines
        )

        with open("Prescription.txt", "a") as add:
            add.write(prescription.Prescription_details())

        print("\nPrescription created successfully!")

        # Doctor consultation fee
        consultation_fee = 0.0

        with open("Doctor.txt", "r") as check:
            Doctor_Data = check.readlines()

        for line in Doctor_Data:
            Details = line.strip().split(",")

            if len(Details) < 5:
                continue

            if Details[0] == Doctor_id:
                try:
                    consultation_fee = float(Details[4])
                except ValueError:
                    consultation_fee = 0.0

                break

        total_amount = consultation_fee + medicine_total

        Payment_status = input(
            "Enter Payment Status (Paid/Pending) : "
        ).strip()

        Bill_id = "B-" + Appointment_id

        bill = Bill(
            Bill_id,
            Patient_id,
            Appointment_id,
            total_amount,
            Payment_status
        )

        with open("Bill.txt", "a") as add:
            add.write(bill.Bill_details())

        # Mark appointment as completed
        updated_appointments = []

        for line in Data:
            Details = line.strip().split(",")

            if len(Details) < 6:
                updated_appointments.append(line)
                continue

            if Details[0] == Appointment_id:
                Details[5] = "Completed"
                updated_appointments.append(
                    ",".join(Details) + "\n"
                )
            else:
                updated_appointments.append(line)

        with open("OP.txt", "w") as update:
            update.writelines(updated_appointments)

        print("\n" + "-" * 45)
        print("Bill Generated Successfully")
        print("-" * 45)
        print("Bill ID          :", Bill_id)
        print("Patient ID       :", Patient_id)
        print("Consultation Fee :", consultation_fee)
        print("Medicine Amount  :", medicine_total)
        print("Total Amount     :", total_amount)
        print("Payment Status   :", Payment_status)
        print("-" * 45)

    def view_prescriptions(self):
        Doctor_id = input("Enter Doctor ID : ").strip()

        with open("Prescription.txt", "r") as view:
            Data = view.readlines()

        found = False

        print("-" * 90)
        print(
            f"|{'Prescription ID':<20}|{'Patient ID':<12}|"
            f"{'Doctor ID':<12}|{'Diagnosis':<20}|"
            f"{'Medicines':<23}|"
        )
        print("-" * 90)

        for line in Data:
            details = line.strip().split(",")

            if len(details) < 5:
                continue

            if details[2] == Doctor_id:
                found = True

                print(
                    f"|{details[0]:<20}|{details[1]:<12}|"
                    f"{details[2]:<12}|{details[3]:<20}|"
                    f"{details[4]:<23}|"
                )

        print("-" * 90)

        if not found:
            print("No prescriptions found for this doctor")


# -----------------------------
# Extra Bill View
# -----------------------------

def view_bills():
    with open("Bill.txt", "r") as view:
        Data = view.readlines()

    if not Data:
        print("No bills available")
        return

    print("-" * 73)
    print(
        f"|{'Bill ID':<15}|{'Patient ID':<12}|"
        f"{'Appointment ID':<17}|{'Amount':<12}|"
        f"{'Status':<12}|"
    )
    print("-" * 73)

    for line in Data:
        details = line.strip().split(",")

        if len(details) < 5:
            continue

        print(
            f"|{details[0]:<15}|{details[1]:<12}|"
            f"{details[2]:<17}|{details[3]:<12}|"
            f"{details[4]:<12}|"
        )

    print("-" * 73)


# -----------------------------
# Menus
# -----------------------------

def admin():
    Ad = Admin()

    while True:
        print("\n========== ADMIN MENU ==========")
        print("1. Add Doctor")
        print("2. Update Doctor Details")
        print("3. Remove Doctor")
        print("4. View Doctors")
        print("5. Add Medicine")
        print("6. Update Medicine")
        print("7. Remove Medicine")
        print("8. View Medicines")
        print("9. View Bills")
        print("10. Logout")

        opt = input("Choose an option : ").strip()

        if opt == "1":
            Ad.Add_Doc()

        elif opt == "2":
            Ad.Doc_Details_update()

        elif opt == "3":
            Ad.Remove_Doc()

        elif opt == "4":
            Ad.view_Doc()

        elif opt == "5":
            Ad.Add_meds()

        elif opt == "6":
            Ad.update_meds()

        elif opt == "7":
            Ad.Remove_meds()

        elif opt == "8":
            Ad.view_meds()

        elif opt == "9":
            view_bills()

        elif opt == "10":
            print("Admin logged out")
            break

        else:
            print("Choose a valid option.")


def receptionist():
    rec = Receptionist()

    while True:
        print("\n======= RECEPTIONIST MENU =======")
        print("1. Add Patient")
        print("2. Book Appointment")
        print("3. View Appointments")
        print("4. View Doctors")
        print("5. View Medicines")
        print("6. View Patients")
        print("7. View Bills")
        print("8. Logout")

        opt = input("Choose an option : ").strip()

        if opt == "1":
            rec.Add_Patient()

        elif opt == "2":
            rec.op()

        elif opt == "3":
            rec.view_op()

        elif opt == "4":
            rec.view_Doc()

        elif opt == "5":
            rec.view_meds()

        elif opt == "6":
            rec.view_patients()

        elif opt == "7":
            view_bills()

        elif opt == "8":
            print("Receptionist logged out")
            break

        else:
            print("Choose a valid option.")


def doctor():
    doc = Doc_Operations()

    while True:
        print("\n========= DOCTOR MENU =========")
        print("1. View My Appointments")
        print("2. Treat Patient")
        print("3. View My Prescriptions")
        print("4. View Medicines")
        print("5. Logout")

        opt = input("Choose an option : ").strip()

        if opt == "1":
            doc.view_appointments()

        elif opt == "2":
            doc.Treat_patient()

        elif opt == "3":
            doc.view_prescriptions()

        elif opt == "4":
            doc.view_meds()

        elif opt == "5":
            print("Doctor logged out")
            break

        else:
            print("Choose a valid option.")


# -----------------------------
# Main Program
# -----------------------------

def run():
    A1 = Autheration()

    while True:
        print("\n====== HOSPITAL MANAGEMENT SYSTEM ======")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        opt = input("Choose an option : ").strip()

        if opt == "1":
            A1.Registeration()

        elif opt == "2":
            res = A1.Login()

            if res is not None:
                if res == "Admin":
                    admin()

                elif res == "Receptionist":
                    receptionist()

                elif res == "Doctor":
                    doctor()

                else:
                    print("Invalid role found in user database.")

        elif opt == "3":
            print("Thank you for using Hospital Management System.")
            break

        else:
            print("Choose the correct option.")


if __name__ == "__main__":
    run()
