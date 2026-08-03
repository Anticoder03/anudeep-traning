# Student Record Tuple
# Format:
# (Student Name, Student ID, Marks, Grade, Status)

students = (
    ("Ashish", 101, 92.5, "A+", "Pass"),
    ("Rahul", 102, 81.0, "A", "Pass"),
    ("Priya", 103, 67.5, "B", "Pass"),
    ("Aman", 104, 34.0, "F", "Fail")
)

print("Student Records")
print("-" * 65)

for name, sid, marks, grade, status in students:
    print(f"{sid:<5} {name:<10} {marks:<6} {grade:<3} {status}")

# # Display Complete Record
# print("Student Record:")
# print(student)

# # Access Individual Elements
# print("\nStudent Details")
# print("-" * 30)
# print(f"Name   : {student[0]}")
# print(f"ID     : {student[1]}")
# print(f"Marks  : {student[2]}")
# print(f"Grade  : {student[3]}")
# print(f"Status : {student[4]}")

# # Tuple Unpacking (Recommended)
# name, sid, marks, grade, status = student

# print("\nUsing Tuple Unpacking")
# print("-" * 30)
# print(f"Student Name : {name}")
# print(f"Student ID   : {sid}")
# print(f"Marks        : {marks}")
# print(f"Grade        : {grade}")
# print(f"Result       : {status}")

# # Useful Information
# print("\nAdditional Information")
# print("-" * 30)
# print(f"Total Fields : {len(student)}")
# print(f"Data Type    : {type(student).__name__}")