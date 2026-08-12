# import pandas as pd

# students = {
#     "Name": ["John", "Jane", "Bob", "Raj"],
#     "12-08-2026": ["Present", "Absent", "Present", "Present"]
# }


# def mark_attendance(name, date, status):

#     if name not in students["Name"]:
#         print("Student not found.")
#         return

#     # Validate status
#     if status not in ["Present", "Absent"]:
#         print("Invalid status. Use Present or Absent.")
#         return

#     # If date doesn't exist, create it with empty values
#     if date not in students:
#         students[date] = ["Not Marked"] * len(students["Name"])

#     # Find student's index
#     index = students["Name"].index(name)

#     # Mark attendance
#     students[date][index] = status

#     print(f"Attendance marked for {name} on {date}.")


# while True:

#     print("\n===== Attendance Management System =====")
#     print("1. Mark Attendance")
#     print("2. View Attendance")
#     print("3. Export Attendance")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":

#         name = input("Enter student name: ")
#         date = input("Enter date (MM-DD-YYYY): ")
#         status = input("Enter status (Present/Absent): ").capitalize()

#         mark_attendance(name, date, status)

#     elif choice == "2":

#         df = pd.DataFrame(students)
#         print("\n===== Attendance =====")
#         print(df.to_string(index=False))

#     elif choice == "3":

#         df = pd.DataFrame(students)
#         df.to_csv("attendance_data.csv", index=False)

#         print("Attendance data exported successfully!")
#         print("File: attendance_data.csv")

#     elif choice == "4":

#         print("Exiting Attendance Management System...")
#         break

#     else:

#         print("Invalid choice. Please try again.")

import pandas as pd
from pathlib import Path
from mail_sender import MailSender
mail_sender = MailSender()

FILE_NAME = Path("attendance_data.csv")
VALID_STATUS = {"Present", "Absent"}


class AttendanceManager:
    def __init__(self, file_name=FILE_NAME):
        self.file_name = Path(file_name)
        self.df = self.load_data()

    # --------------------------------------------------
    # Load existing attendance data
    # --------------------------------------------------
    def load_data(self):
        if self.file_name.exists():
            try:
                return pd.read_csv(self.file_name, dtype=str).fillna("")
            except Exception as e:
                print(f"Error loading file: {e}")

        return pd.DataFrame({"Name": ["John", "Jane", "Bob", "Raj"]})

    # --------------------------------------------------
    # Save attendance data
    # --------------------------------------------------
    def save_data(self):
        try:
            self.df.to_csv(self.file_name, index=False)
            print(f"Data saved to {self.file_name}")
        except Exception as e:
            print(f"Error saving data: {e}")

    # --------------------------------------------------
    # Add student
    # --------------------------------------------------
    def add_student(self, name):
        name = name.strip()

        if not name:
            print("Student name cannot be empty.")
            return

        if name.lower() in self.df["Name"].str.lower().values:
            print("Student already exists.")
            return

        new_student = {"Name": name}

        # Add empty attendance for existing dates
        for column in self.df.columns:
            if column != "Name":
                new_student[column] = "Not Marked"

        self.df = pd.concat(
            [self.df, pd.DataFrame([new_student])],
            ignore_index=True
        )

        self.save_data()
        print(f"Student '{name}' added successfully.")

    # --------------------------------------------------
    # Remove student
    # --------------------------------------------------
    def remove_student(self, name):
        name = name.strip()

        matches = self.df["Name"].str.lower() == name.lower()

        if not matches.any():
            print("Student not found.")
            return

        self.df = self.df.loc[~matches].reset_index(drop=True)

        self.save_data()
        print(f"Student '{name}' removed successfully.")

    # --------------------------------------------------
    # Edit student name
    # --------------------------------------------------
    def edit_student(self, old_name, new_name):
        old_name = old_name.strip()
        new_name = new_name.strip()

        if not new_name:
            print("New name cannot be empty.")
            return

        matches = self.df["Name"].str.lower() == old_name.lower()

        if not matches.any():
            print("Student not found.")
            return

        if new_name.lower() in self.df["Name"].str.lower().values:
            print("A student with this name already exists.")
            return

        self.df.loc[matches, "Name"] = new_name

        self.save_data()
        print(f"Student name changed from '{old_name}' to '{new_name}'.")

    # --------------------------------------------------
    # Mark attendance
    # --------------------------------------------------
    def mark_attendance(self, name, date, status):
        name = name.strip()
        status = status.strip().capitalize()

        matches = self.df["Name"].str.lower() == name.lower()

        if not matches.any():
            print("Student not found.")
            return

        if status not in VALID_STATUS:
            print("Invalid status. Use Present or Absent.")
            return

        # Create date column if it doesn't exist
        if date not in self.df.columns:
            self.df[date] = "Not Marked"

        self.df.loc[matches, date] = status

        self.save_data()

        print(
            f"Attendance marked: {name} → {status} "
            f"on {date}"
        )

    # --------------------------------------------------
    # View attendance
    # --------------------------------------------------
    def view_attendance(self):
        if self.df.empty:
            print("\nNo students found.")
            return

        print("\n" + "=" * 70)
        print("ATTENDANCE RECORD")
        print("=" * 70)

        print(self.df.to_string(index=False))

    # --------------------------------------------------
    # Show student attendance percentage
    # --------------------------------------------------
    def attendance_analysis(self):
        if self.df.empty:
            print("No students available.")
            return

        date_columns = [
            column for column in self.df.columns
            if column != "Name"
        ]

        if not date_columns:
            print("No attendance has been recorded yet.")
            return

        print("\n" + "=" * 70)
        print("ATTENDANCE ANALYSIS")
        print("=" * 70)

        for _, student in self.df.iterrows():

            attendance = student[date_columns]

            present = (attendance == "Present").sum()
            absent = (attendance == "Absent").sum()

            total = present + absent

            if total == 0:
                percentage = 0
            else:
                percentage = (present / total) * 100

            print(
                f"{student['Name']:<20} "
                f"Present: {present:<3} "
                f"Absent: {absent:<3} "
                f"Attendance: {percentage:.2f}%"
            )

    # --------------------------------------------------
    # Export attendance
    # --------------------------------------------------
    def export_data(self):
        self.save_data()
        print("Attendance exported successfully!")


# ======================================================
# MENU
# ======================================================

def show_menu():
    print("\n")
    print("=" * 50)
    print("       ATTENDANCE MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1.  Add Student")
    print("2.  Remove Student")
    print("3.  Edit Student")
    print("4.  Mark Attendance")
    print("5.  View Attendance")
    print("6.  Attendance Analysis")
    print("7.  Export Attendance")
    print("8.  Exit")
    print("=" * 50)

# def send_mail():
#     import os
#     os.environ["SENDER_ADDR"] = "ap5351545@gmail.com"
#     os.environ["SENDER_PASS"] = "nindpbdkvpkkelhp"
#     os.environ["SMTP_PORT"]   = "587"
#     os.environ["SMTP_SERVER"] = "smtp.gmail.com"

#     mail_sender.send_mail(
#     receiver_address = "test@gmail.com", subject = "email subject",
#     content = "message content", attach_files = (("attendance_data.csv", file),)
# )
    
    
# ======================================================
# MAIN PROGRAM
# ======================================================

def main():

    manager = AttendanceManager()

    print("\nAttendance Management System Started")
    print(f"Data file: {FILE_NAME}")

    while True:

        show_menu()

        choice = input("Enter your choice: ").strip()

        # ----------------------------------------------
        # Add Student
        # ----------------------------------------------
        if choice == "1":

            name = input("Enter student name: ")
            manager.add_student(name)

        # ----------------------------------------------
        # Remove Student
        # ----------------------------------------------
        elif choice == "2":

            name = input("Enter student name to remove: ")
            manager.remove_student(name)

        # ----------------------------------------------
        # Edit Student
        # ----------------------------------------------
        elif choice == "3":

            old_name = input("Enter current student name: ")
            new_name = input("Enter new student name: ")

            manager.edit_student(old_name, new_name)

        # ----------------------------------------------
        # Mark Attendance
        # ----------------------------------------------
        elif choice == "4":

            name = input("Enter student name: ")
            date = input("Enter date (MM-DD-YYYY): ")
            status = input("Enter status (Present/Absent): ")

            manager.mark_attendance(
                name,
                date,
                status
            )

        # ----------------------------------------------
        # View Attendance
        # ----------------------------------------------
        elif choice == "5":

            manager.view_attendance()

        # ----------------------------------------------
        # Attendance Analysis
        # ----------------------------------------------
        elif choice == "6":

            manager.attendance_analysis()

        # ----------------------------------------------
        # Export
        # ----------------------------------------------
        elif choice == "7":

            manager.export_data()

        # ----------------------------------------------
        # Exit
        # ----------------------------------------------
        elif choice == "8":

            manager.save_data()

            print("\nExiting Attendance Management System...")
            print("Goodbye!")

            break

        # ----------------------------------------------
        # Invalid choice
        # ----------------------------------------------
        else:

            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()