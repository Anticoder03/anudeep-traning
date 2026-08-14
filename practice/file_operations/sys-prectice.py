import sys
import os
print("Script name:", sys.argv[0])
print("Number of arguments:", len(sys.argv))
print("Arguments passed:", sys.argv[1:])

print(sys.path)

print("test line.")

#! sys.exit("Program End.")

print(sys.platform)
print(os.name)
print(sys.version)

sys.stdout.write("Hello World.")
print("Max Cap is: ")
print(sys.maxsize)


print("Modules present in the system is: ")
print(sys.modules.keys())
