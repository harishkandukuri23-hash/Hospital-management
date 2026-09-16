# 🏥 Hospital Management System

A **Python-based Hospital Management System** developed using **Object-Oriented Programming (OOP)** and **File Handling** concepts.

The system is designed to manage important hospital operations such as **user authentication, doctors, patients, appointments, prescriptions, and billing** through a structured role-based system.

---

## 📌 Project Overview

The Hospital Management System provides a simple console-based solution for managing hospital information.

The project focuses on applying Python programming concepts to a real-world application, including:

* Object-Oriented Programming
* Inheritance
* File Handling
* Authentication
* Role-Based Access
* CRUD Operations
* Data Management
* Patient and Doctor Management
* Appointment Management
* Prescription Management
* Billing Management

---

## 🎯 Objectives

The main objectives of this project are:

* To create a simple hospital management application using Python.
* To implement OOP concepts in a real-world project.
* To manage doctors and their specializations.
* To manage patient information.
* To connect patients with doctors through appointments.
* To allow doctors to diagnose patients and provide prescriptions.
* To generate and manage patient bills.
* To store application data using text files.

---

## 👥 User Roles

The system contains different user roles with different responsibilities.

### 👨‍💼 Admin

The Admin is responsible for managing hospital-related information and system operations.

### 👨‍⚕️ Doctor

Doctors can manage patient-related medical information.

Doctor records contain:

* Doctor ID
* Doctor Name
* Specialization
* Contact Number
* Consultation Fee

Example doctor records used in the project include Cardiologist and Dermatologist specializations.

### 🧑‍💼 Receptionist

The Receptionist handles administrative activities such as:

* Patient registration
* Appointment management
* Viewing doctor information
* Managing patient-related information

---

## 🩺 Doctor Specializations

The project supports doctors with different specializations.

Example:

| Doctor | Specialization | Consultation Fee |
| ------ | -------------- | ---------------: |
| Tsuki  | Cardiologist   |              450 |
| Hinata | Dermatologist  |              400 |

---

## 🧑‍🤝‍🧑 Patient Management

The system maintains patient-related information and connects patients with doctors through the appointment process.

The hospital workflow can be represented as:

```text
Patient
   ↓
Appointment
   ↓
Doctor
   ↓
Diagnosis
   ↓
Prescription
   ↓
Billing
```

---

## 📅 Appointment Management

Appointments connect patients with doctors.

The appointment workflow allows the hospital to keep track of:

* Patient
* Doctor
* Appointment
* Medical consultation

This provides a structured connection between the administrative and medical parts of the system.

---

## 💊 Diagnosis & Prescription

After consultation, the doctor can provide a diagnosis and prescription for the patient.

The medical workflow is:

```text
Patient
   ↓
Doctor Consultation
   ↓
Diagnosis
   ↓
Prescription
```

---

## 💰 Billing System

The project includes a billing system for managing patient bills.

A bill record contains information such as:

```text
Bill ID
Patient ID
Amount
Status
```

Example:

```text
B-555,100,555,4537.3,pending
```

The system can therefore maintain billing information and payment status.

---

## 📂 File Handling

The project uses text files to store application data instead of a database.

Example files include:

```text
User.txt
Doctor.txt
Patient.txt
Appointment.txt
Prescription.txt
Bill.txt
```

The exact files may vary depending on the current version of the project.

---

## 🐍 Python Concepts Used

This project demonstrates several important Python concepts.

### Object-Oriented Programming

* Classes
* Objects
* Constructors
* Instance variables
* Methods
* Inheritance
* Multilevel inheritance
* Hierarchical inheritance
* Multiple inheritance

### File Handling

* Reading files
* Writing files
* Appending data
* Updating records
* Searching records

### Other Python Concepts

* Conditional statements
* Loops
* Functions
* Lists
* Dictionaries
* Tuples
* Sets
* String manipulation
* Exception handling where implemented

---

## 🔐 Authentication

The system includes user authentication to identify users and provide access based on their role.

The basic flow is:

```text
Registration
     ↓
Login
     ↓
Role Verification
     ↓
Role-Based Menu
```

---

## ⚙️ CRUD Operations

The system applies CRUD operations to manage hospital records.

| Operation | Description              |
| --------- | ------------------------ |
| Create    | Add new hospital records |
| Read      | View existing records    |
| Update    | Modify existing records  |
| Delete    | Remove records           |

---

## 📁 Project Structure

A typical project structure is:

```text
Hospital-Management-System/
│
├── main.py
├── authentication.py
├── admin.py
├── doctor.py
├── receptionist.py
├── patient.py
│
├── User.txt
├── Doctor.txt
├── Patient.txt
├── Appointment.txt
├── Prescription.txt
├── Bill.txt
│
└── README.md
```

> File names may differ depending on the current version of the project.

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
```

### 2. Open the project

```bash
cd Hospital-Management-System
```

### 3. Run the main Python file

```bash
python main.py
```

---

## 🔄 System Workflow

```text
                 Hospital Management System
                            │
             ┌──────────────┴──────────────┐
             │                             │
        Authentication                 User Roles
             │                             │
      ┌──────┴──────┐          ┌───────────┼───────────┐
      │             │          │           │           │
   Register       Login      Admin      Doctor    Receptionist
                                      │           │
                                      │           │
                                  Patient      Appointment
                                      │
                                  Diagnosis
                                      │
                                 Prescription
                                      │
                                    Bill
```

---

## 🚀 Future Enhancements

Possible future improvements include:

* Database integration using MySQL
* Graphical User Interface
* Online appointment booking
* Automated bill generation
* Medicine inventory management
* Doctor availability tracking
* Patient medical history
* Secure password storage
* Email/SMS appointment notifications
* Hospital dashboard and reports

---

## 🛠️ Technologies Used

* **Python**
* **Object-Oriented Programming**
* **File Handling**
* **VS Code**
* **Git & GitHub**

---

## 📚 Learning Outcomes

Through this project, I practiced how to:

* Design a real-world application using Python.
* Apply OOP concepts to different entities.
* Implement inheritance and reusable classes.
* Work with files for persistent data storage.
* Build authentication and role-based access.
* Perform CRUD operations.
* Connect different modules such as patients, doctors, appointments, prescriptions, and billing.
* Structure a larger Python project.

---

## 👨‍💻 Author

**Sai Harish Kandukuri**

This project was developed as a practical implementation of Python, OOP, and file-handling concepts.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
