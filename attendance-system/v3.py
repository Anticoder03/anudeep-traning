import os
import re
import smtplib
from pathlib import Path
from email.message import EmailMessage
from datetime import datetime

import pandas as pd


# ============================================================
# CONFIGURATION
# ============================================================

FILE_NAME = Path("attendance_data.csv")

VALID_STATUS = {"Present", "Absent"}

# Gmail SMTP configuration
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))

SENDER_ADDR = "ap5381545@gmail.com"
SENDER_PASS = "sylqzotwkxwdxagv"


# ============================================================
# EMAIL FUNCTIONS
# ============================================================

def validate_email(email):
    """Validate email address."""

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return re.match(pattern, email) is not None


def send_mail(receiver_address, subject, content, attachment_path):
    """
    Send an email with a CSV attachment using Gmail SMTP.
    """

    if not SENDER_ADDR or not SENDER_PASS:
        print("\nEmail configuration is missing.")
        print("Please set SENDER_ADDR and SENDER_PASS.")
        return False

    if not validate_email(receiver_address):
        print("Invalid receiver email address.")
        return False

    attachment_path = Path(attachment_path)

    if not attachment_path.exists():
        print("Attachment file not found.")
        return False

    try:
        # Create email
        message = EmailMessage()

        message["From"] = SENDER_ADDR
        message["To"] = receiver_address
        message["Subject"] = subject

        message.set_content(content)

        # Attach CSV file
        with open(attachment_path, "rb") as file:
            file_data = file.read()

        message.add_attachment(
            file_data,
            maintype="text",
            subtype="csv",
            filename=attachment_path.name
        )

        # Connect to Gmail SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

            server.ehlo()

            # Start TLS encryption
            server.starttls()

            server.ehlo()

            # Login
            server.login(
                SENDER_ADDR,
                SENDER_PASS
            )

            # Send email
            server.send_message(message)

        print("\nEmail sent successfully!")
        print(f"Receiver: {receiver_address}")
        print(f"Attachment: {attachment_path}")

        return True

    except smtplib.SMTPAuthenticationError:
        print("\nEmail authentication failed.")
        print("Check your Gmail address and App Password.")

        return False

    except smtplib.SMTPException as e:
        print(f"\nSMTP error: {e}")

        return False

    except Exception as e:
        print(f"\nError sending email: {e}")

        return False


# ============================================================
# ATTENDANCE MANAGER
# ============================================================

class AttendanceManager:

    def __init__(self, file_name=FILE_NAME):

        self.file_name = Path(file_name)

        self.df = self.load_data()

    # --------------------------------------------------------
    # Load CSV
    # --------------------------------------------------------

    def load_data(self):

        if self.file_name.exists():

            try:

                df = pd.read_csv(
                    self.file_name,
                    dtype=str
                ).fillna("")

                # Make sure Name column exists
                if "Name" not in df.columns:

                    print(
                        "Invalid attendance file."
                    )

                    return pd.DataFrame(
                        {"Name": []}
                    )

                return df

            except Exception as e:

                print(
                    f"Error loading attendance file: {e}"
                )

        # Default students
        return pd.DataFrame(
            {
                "Name": [
                    "John",
                    "Jane",
                    "Bob",
                    "Raj"
                ]
            }
        )

    # --------------------------------------------------------
    # Save CSV
    # --------------------------------------------------------

    def save_data(self):

        try:

            self.df.to_csv(
                self.file_name,
                index=False
            )

            return True

        except Exception as e:

            print(
                f"Error saving attendance data: {e}"
            )

            return False

    # --------------------------------------------------------
    # Add student
    # --------------------------------------------------------

    def add_student(self, name):

        name = name.strip()

        if not name:

            print(
                "Student name cannot be empty."
            )

            return

        existing_names = (
            self.df["Name"]
            .astype(str)
            .str.lower()
            .values
        )

        if name.lower() in existing_names:

            print(
                "Student already exists."
            )

            return

        new_student = {
            "Name": name
        }

        # Add Not Marked to existing dates
        for column in self.df.columns:

            if column != "Name":

                new_student[column] = "Not Marked"

        new_row = pd.DataFrame(
            [new_student]
        )

        self.df = pd.concat(
            [
                self.df,
                new_row
            ],
            ignore_index=True
        )

        self.save_data()

        print(
            f"Student '{name}' added successfully."
        )

    # --------------------------------------------------------
    # Remove student
    # --------------------------------------------------------

    def remove_student(self, name):

        name = name.strip()

        matches = (
            self.df["Name"]
            .astype(str)
            .str.lower()
            == name.lower()
        )

        if not matches.any():

            print(
                "Student not found."
            )

            return

        self.df = (
            self.df.loc[~matches]
            .reset_index(drop=True)
        )

        self.save_data()

        print(
            f"Student '{name}' removed successfully."
        )

    # --------------------------------------------------------
    # Edit student
    # --------------------------------------------------------

    def edit_student(
        self,
        old_name,
        new_name
    ):

        old_name = old_name.strip()
        new_name = new_name.strip()

        if not new_name:

            print(
                "New name cannot be empty."
            )

            return

        matches = (
            self.df["Name"]
            .astype(str)
            .str.lower()
            == old_name.lower()
        )

        if not matches.any():

            print(
                "Student not found."
            )

            return

        existing_names = (
            self.df["Name"]
            .astype(str)
            .str.lower()
            .values
        )

        if new_name.lower() in existing_names:

            print(
                "A student with this name already exists."
            )

            return

        self.df.loc[
            matches,
            "Name"
        ] = new_name

        self.save_data()

        print(
            f"Student renamed from "
            f"'{old_name}' to '{new_name}'."
        )

    # --------------------------------------------------------
    # Validate date
    # --------------------------------------------------------

    def validate_date(self, date):

        try:

            datetime.strptime(
                date,
                "%m-%d-%Y"
            )

            return True

        except ValueError:

            return False

    # --------------------------------------------------------
    # Mark attendance
    # --------------------------------------------------------

    def mark_attendance(
        self,
        name,
        date,
        status
    ):

        name = name.strip()
        date = date.strip()
        status = status.strip().capitalize()

        # Validate student
        matches = (
            self.df["Name"]
            .astype(str)
            .str.lower()
            == name.lower()
        )

        if not matches.any():

            print(
                "Student not found."
            )

            return

        # Validate status
        if status not in VALID_STATUS:

            print(
                "Invalid status."
            )

            print(
                "Use: Present or Absent"
            )

            return

        # Validate date
        if not self.validate_date(date):

            print(
                "Invalid date format."
            )

            print(
                "Use MM-DD-YYYY"
            )

            return

        # Create date column
        if date not in self.df.columns:

            self.df[date] = "Not Marked"

        # Mark attendance
        self.df.loc[
            matches,
            date
        ] = status

        self.save_data()

        print(
            f"\nAttendance marked successfully!"
        )

        print(
            f"Student : {name}"
        )

        print(
            f"Date    : {date}"
        )

        print(
            f"Status  : {status}"
        )

    # --------------------------------------------------------
    # View attendance
    # --------------------------------------------------------

    def view_attendance(self):

        if self.df.empty:

            print(
                "\nNo students found."
            )

            return

        print("\n")
        print("=" * 80)
        print("                    ATTENDANCE RECORD")
        print("=" * 80)

        print(
            self.df.to_string(
                index=False
            )
        )

        print("=" * 80)

    # --------------------------------------------------------
    # Attendance analysis
    # --------------------------------------------------------

    def attendance_analysis(self):

        if self.df.empty:

            print(
                "No students available."
            )

            return

        date_columns = [
            column
            for column in self.df.columns
            if column != "Name"
        ]

        if not date_columns:

            print(
                "No attendance has been recorded yet."
            )

            return

        print("\n")
        print("=" * 80)
        print("                    ATTENDANCE ANALYSIS")
        print("=" * 80)

        for _, student in self.df.iterrows():

            attendance = student[
                date_columns
            ]

            present = (
                attendance == "Present"
            ).sum()

            absent = (
                attendance == "Absent"
            ).sum()

            not_marked = (
                attendance == "Not Marked"
            ).sum()

            total = present + absent

            if total > 0:

                percentage = (
                    present / total
                ) * 100

            else:

                percentage = 0

            print(
                f"\nStudent       : "
                f"{student['Name']}"
            )

            print(
                f"Present       : "
                f"{present}"
            )

            print(
                f"Absent        : "
                f"{absent}"
            )

            print(
                f"Not Marked    : "
                f"{not_marked}"
            )

            print(
                f"Attendance    : "
                f"{percentage:.2f}%"
            )

        print("\n" + "=" * 80)

    # --------------------------------------------------------
    # Today's summary
    # --------------------------------------------------------

    def today_summary(self):

        today = datetime.now().strftime(
            "%m-%d-%Y"
        )

        if today not in self.df.columns:

            print(
                f"\nNo attendance recorded for {today}."
            )

            return

        attendance = self.df[today]

        present = (
            attendance == "Present"
        ).sum()

        absent = (
            attendance == "Absent"
        ).sum()

        not_marked = (
            attendance == "Not Marked"
        ).sum()

        total = len(self.df)

        print("\n")
        print("=" * 50)
        print("             TODAY'S SUMMARY")
        print("=" * 50)

        print(
            f"Date       : {today}"
        )

        print(
            f"Total      : {total}"
        )

        print(
            f"Present    : {present}"
        )

        print(
            f"Absent     : {absent}"
        )

        print(
            f"Not Marked : {not_marked}"
        )

        print("=" * 50)

    # --------------------------------------------------------
    # Send attendance email
    # --------------------------------------------------------

    def send_attendance_email(self):

        # Always save latest data first
        if not self.save_data():

            print(
                "Could not save attendance data."
            )

            return

        print("\n")
        print("=" * 60)
        print("                 SEND ATTENDANCE")
        print("=" * 60)

        receiver = input(
            "Enter receiver email: "
        ).strip()

        subject = input(
            "Enter email subject "
            "(press Enter for default): "
        ).strip()

        if not subject:

            subject = (
                "Attendance Report"
            )

        content = input(
            "Enter email message "
            "(press Enter for default): "
        ).strip()

        if not content:

            content = (
                "Please find the attendance "
                "report attached."
            )

        send_mail(
            receiver_address=receiver,
            subject=subject,
            content=content,
            attachment_path=self.file_name
        )

    # --------------------------------------------------------
    # Export attendance
    # --------------------------------------------------------

    def export_data(self):

        if self.save_data():

            print(
                "\nAttendance data exported successfully!"
            )

            print(
                f"File: {self.file_name}"
            )


# ============================================================
# MENU
# ============================================================

def show_menu():

    print("\n")

    print("=" * 60)

    print(
        "             ATTENDANCE MANAGEMENT SYSTEM"
    )

    print("=" * 60)

    print("1.  Add Student")
    print("2.  Remove Student")
    print("3.  Edit Student")
    print("4.  Mark Attendance")
    print("5.  View Attendance")
    print("6.  Attendance Analysis")
    print("7.  Today's Summary")
    print("8.  Export Attendance")
    print("9.  Send Attendance by Email")
    print("10. Exit")

    print("=" * 60)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    manager = AttendanceManager()

    print("\n")
    print("=" * 60)

    print(
        "       ATTENDANCE MANAGEMENT SYSTEM"
    )

    print("=" * 60)

    print(
        f"Attendance file: {FILE_NAME}"
    )

    while True:

        show_menu()

        choice = input(
            "Enter your choice: "
        ).strip()

        # ----------------------------------------------------
        # ADD STUDENT
        # ----------------------------------------------------

        if choice == "1":

            name = input(
                "Enter student name: "
            )

            manager.add_student(name)

        # ----------------------------------------------------
        # REMOVE STUDENT
        # ----------------------------------------------------

        elif choice == "2":

            name = input(
                "Enter student name to remove: "
            )

            manager.remove_student(name)

        # ----------------------------------------------------
        # EDIT STUDENT
        # ----------------------------------------------------

        elif choice == "3":

            old_name = input(
                "Enter current student name: "
            )

            new_name = input(
                "Enter new student name: "
            )

            manager.edit_student(
                old_name,
                new_name
            )

        # ----------------------------------------------------
        # MARK ATTENDANCE
        # ----------------------------------------------------

        elif choice == "4":

            name = input(
                "Enter student name: "
            )

            date = input(
                "Enter date (MM-DD-YYYY): "
            )

            status = input(
                "Enter status "
                "(Present/Absent): "
            )

            manager.mark_attendance(
                name,
                date,
                status
            )

        # ----------------------------------------------------
        # VIEW ATTENDANCE
        # ----------------------------------------------------

        elif choice == "5":

            manager.view_attendance()

        # ----------------------------------------------------
        # ANALYSIS
        # ----------------------------------------------------

        elif choice == "6":

            manager.attendance_analysis()

        # ----------------------------------------------------
        # TODAY'S SUMMARY
        # ----------------------------------------------------

        elif choice == "7":

            manager.today_summary()

        # ----------------------------------------------------
        # EXPORT
        # ----------------------------------------------------

        elif choice == "8":

            manager.export_data()

        # ----------------------------------------------------
        # SEND EMAIL
        # ----------------------------------------------------

        elif choice == "9":

            manager.send_attendance_email()

        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        elif choice == "10":

            manager.save_data()

            print("\n")
            print(
                "Exiting Attendance Management System..."
            )

            print(
                "All data has been saved."
            )

            print(
                "Goodbye!"
            )

            break

        # ----------------------------------------------------
        # INVALID CHOICE
        # ----------------------------------------------------

        else:

            print(
                "\nInvalid choice."
            )

            print(
                "Please select a number from 1-10."
            )


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()