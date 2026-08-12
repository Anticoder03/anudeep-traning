import pandas as pd

students = {
    "Name": ["John", "Jane", "Bob", "Raj"],
    "12-08-2026": ["Present", "Absent", "Present", "Present"]
}


def mark_attendance(name, date, status):

    if name not in students["Name"]:
        print("Student not found.")
        return

    # Validate status
    if status not in ["Present", "Absent"]:
        print("Invalid status. Use Present or Absent.")
        return

    # If date doesn't exist, create it with empty values
    if date not in students:
        students[date] = ["Not Marked"] * len(students["Name"])

    # Find student's index
    index = students["Name"].index(name)

    # Mark attendance
    students[date][index] = status

    print(f"Attendance marked for {name} on {date}.")


while True:

    print("\n===== Attendance Management System =====")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Export Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        date = input("Enter date (MM-DD-YYYY): ")
        status = input("Enter status (Present/Absent): ").capitalize()

        mark_attendance(name, date, status)

    elif choice == "2":

        df = pd.DataFrame(students)
        print("\n===== Attendance =====")
        print(df.to_string(index=False))

    elif choice == "3":

        df = pd.DataFrame(students)
        df.to_csv("attendance_data.csv", index=False)

        print("Attendance data exported successfully!")
        print("File: attendance_data.csv")

    elif choice == "4":

        print("Exiting Attendance Management System...")
        break

    else:

        print("Invalid choice. Please try again.")