with open("student.txt","w") as file:
    file.write("Hello World")

with open("student.txt","r") as file:
    content = file.read()
    print(content)

with open("student.txt","a") as file:
    file.write("\nThis is a new line.")
    
with open("student.txt","r") as file:
    content = file.read()
    print(content)