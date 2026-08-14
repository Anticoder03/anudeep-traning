from pathlib import Path

test_file = Path(__file__).with_name("test.txt")

with test_file.open("w") as file:
    file.write("Hello, World!")
    file.write("\nAnother text.")
    
with test_file.open("r") as file:
    content = file.read()
    print(content)

