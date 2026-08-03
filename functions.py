# def average(a,b,c):
#     print( (a + b + c) / 3)
    
# average(10, 20, 30)

# def check_pelidrome(number):
#     temp = number
#     rev = 0
#     while(number > 0):
#         n = number %10
#         rev = rev * 10 + n
#         number = number // 10
#     if(temp == rev):
#         print("The number is a palindrome")
#     else:
#         print("The number is not a palindrome")
        
        
        
# a = int(input("Enter a number: "))
# check_pelidrome(a)

bool_list = ["Yes", "No", "Yes", "No", "Yes"]
mapped_values = list(map(lambda x: 1 if x == "Yes" else 0, bool_list))

# print(bool_list)
# print(mapped_values)  


# nornal function
def check_yes(x):
    return x % 2 == 0

nums = [1,2,3,4,5,6,7,8,9,0]

even_nums = list(filter(check_yes, nums))
# print(even_nums)


# using lambda function
even_numbers = list(filter(lambda a: a%2 != 0,nums))
print(even_numbers)

yes_list = list(filter(lambda c: c == "Yes", bool_list))
print(yes_list)

def sumnums(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
sum = sumnums(1,2,3,4,5,6,7,8,9)
print(sum)


def stud_info(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")
    # print(kwargs.items())
        
        
stud_info(name="Ashish", age=21, course="Python", country="India")