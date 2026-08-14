from pathlib import Path

student_file = Path(__file__).with_name("student.txt")

with student_file.open("w") as file:
    file.write("Hello World")

with student_file.open("r") as file:
    content = file.read()
    print(content)

with student_file.open("a") as file:
    file.write("\nThis is a new line.")
    
with student_file.open("r") as file:
    content = file.read()
    print(content)