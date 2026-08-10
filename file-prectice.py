with open("test.txt","w") as file:
    file.write("Hello, World!")
    
with open("test.txt","r") as file:
    content = file.read()
    print(content)
    