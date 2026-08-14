import os
print("Current Working Directory:", os.getcwd())
file_list = os.listdir()
print("Files and Directories in Current Directory:")
for item in file_list:
    print(item)


if os.mkdir("new_dir"):
    print("Directory 'new_dir' created successfully.")
else:
    print("Directory 'new_dir' already exists.")


if os.makedirs("nested_dir/sub_dir", exist_ok=True):
    print("Nested directories 'dir1/sub_dir' created successfully.")
else:
    print("Failed to create nested directories.")

if os.rmdir("new_dir"):
    print("Directory 'new_dir' removed successfully.")
else:
    print("Failed to remove directory 'new_dir'. It may not be empty or may not exist.")
    
if os.path.exists("test"):
    print("test exists")
    

print("absolute path of current directory:", os.path.abspath(os.getcwd()))

print("Base name of current directory:", os.path.basename(os.getcwd()))

print("Directory name of current directory:", os.path.dirname(os.getcwd()))

print("List of directories in path variable:", os.environ.get("PATH").split(os.pathsep))

os.system("echo Hello, World!")

os.chdir("..")
print("Changed directory to:", os.getcwd())
